from __future__ import annotations

import asyncio
import json
import uuid

from fastapi import APIRouter, WebSocket, WebSocketDisconnect

router = APIRouter()

_sessions: dict[str, "TerminalSession"] = {}


class TerminalSession:
    def __init__(self, session_id: str) -> None:
        self.id = session_id
        self._proc: asyncio.subprocess.Process | None = None
        self._buffer: asyncio.Queue[str] = asyncio.Queue()

    async def start(self) -> None:
        self._proc = await asyncio.create_subprocess_shell(
            "powershell.exe",
            stdin=asyncio.subprocess.PIPE,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.STDOUT,
        )

        asyncio.create_task(self._read_stdout())

    async def _read_stdout(self) -> None:
        assert self._proc is not None and self._proc.stdout is not None
        while True:
            line = await self._proc.stdout.readline()
            if not line:
                break
            await self._buffer.put(line.decode("utf-8", errors="replace"))
        await self._buffer.put("[process terminated]")

    async def write(self, data: str) -> None:
        assert self._proc is not None and self._proc.stdin is not None
        self._proc.stdin.write(data.encode("utf-8"))
        await self._proc.stdin.drain()

    async def read_line(self) -> str:
        return await self._buffer.get()

    async def stop(self) -> None:
        if self._proc is not None:
            self._proc.kill()
            await self._proc.wait()


@router.websocket("/api/v1/noteblocks/terminal/ws")
async def terminal_websocket(ws: WebSocket) -> None:
    await ws.accept()

    session_id = uuid.uuid4().hex[:12]
    session = TerminalSession(session_id)
    _sessions[session_id] = session

    try:
        await session.start()

        await ws.send_text(json.dumps({"type": "init", "session_id": session_id}))

        async def reader() -> None:
            while True:
                line = await session.read_line()
                await ws.send_text(json.dumps({"type": "output", "data": line}))

        async def writer() -> None:
            while True:
                raw = await ws.receive_text()
                msg = json.loads(raw)
                if msg.get("type") == "input":
                    await session.write(msg["data"])

        await asyncio.gather(reader(), writer())

    except WebSocketDisconnect:
        pass
    finally:
        await session.stop()
        _sessions.pop(session_id, None)
