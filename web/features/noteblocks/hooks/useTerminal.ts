"use client";

import { useCallback, useEffect, useRef, useState } from "react";

export function useTerminal() {
  const [output, setOutput] = useState<string[]>([]);
  const [connected, setConnected] = useState(false);
  const wsRef = useRef<WebSocket | null>(null);

  useEffect(() => {
    const apiBase = process.env.NEXT_PUBLIC_API_BASE || `http://${window.location.host}`;
    const wsBase = apiBase.replace(/^http/, "ws");
    const url = `${wsBase}/api/v1/noteblocks/terminal/ws`;

    const ws = new WebSocket(url);
    wsRef.current = ws;

    ws.onopen = () => setConnected(true);

    ws.onmessage = (event) => {
      try {
        const msg = JSON.parse(event.data);
        if (msg.type === "output") {
          setOutput((prev) => [...prev, msg.data]);
        }
      } catch {
        // ignore
      }
    };

    ws.onclose = () => setConnected(false);

    return () => {
      ws.close();
    };
  }, []);

  const sendInput = useCallback((data: string) => {
    if (wsRef.current?.readyState === WebSocket.OPEN) {
      wsRef.current.send(JSON.stringify({ type: "input", data }));
    }
  }, []);

  const clear = useCallback(() => setOutput([]), []);

  return { output, connected, sendInput, clear };
}
