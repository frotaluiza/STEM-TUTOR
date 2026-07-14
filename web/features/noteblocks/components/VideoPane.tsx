"use client";

import { useState, useCallback } from "react";

interface VideoPaneProps {
  onPause?: () => void;
}

export function VideoPane({ onPause }: VideoPaneProps) {
  const [url, setUrl] = useState("");
  const [activeUrl, setActiveUrl] = useState("");
  const [showInput, setShowInput] = useState(!activeUrl);

  const handleLoad = useCallback(() => {
    if (url.trim()) {
      setActiveUrl(url);
      setShowInput(false);
    }
  }, [url]);

  const handlePause = useCallback(() => {
    onPause?.();
  }, [onPause]);

  return (
    <div className="flex flex-col h-full bg-black">
      {showInput && !activeUrl ? (
        <div className="flex-1 flex items-center justify-center p-4">
          <div className="w-full max-w-md">
            <p className="text-xs text-gray-300 mb-2">Insira uma URL de video (YouTube, Vimeo, ou arquivo local)</p>
            <div className="flex gap-2">
              <input
                value={url}
                onChange={(e) => setUrl(e.target.value)}
                placeholder="https://youtube.com/watch?v=..."
                className="flex-1 bg-[#0a0a0a] text-sm text-gray-300 border border-[#222] rounded px-3 py-2 outline-none placeholder-gray-700"
                onKeyDown={(e) => e.key === "Enter" && handleLoad()}
              />
              <button
                onClick={handleLoad}
                disabled={!url.trim()}
                className="px-3 py-2 text-xs bg-[#00ff80]/10 text-[#00ff80] border border-[#00ff80]/20 rounded hover:bg-[#00ff80]/20 disabled:opacity-30"
              >
                Carregar
              </button>
            </div>
          </div>
        </div>
      ) : (
        <div className="relative flex-1">
          {activeUrl.includes("youtube") || activeUrl.includes("youtu.be") ? (
            <iframe
              src={activeUrl.replace("watch?v=", "embed/").split("&")[0]}
              className="w-full h-full"
              allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
              allowFullScreen
              onPause={handlePause}
            />
          ) : activeUrl.includes("vimeo") ? (
            <iframe
              src={activeUrl.replace("vimeo.com/", "player.vimeo.com/video/")}
              className="w-full h-full"
              allow="autoplay; fullscreen"
              allowFullScreen
            />
          ) : (
            <video
              src={activeUrl}
              controls
              className="w-full h-full"
              onPause={handlePause}
            />
          )}

          <button
            onClick={() => { setActiveUrl(""); setShowInput(true); }}
            className="absolute top-2 right-2 px-2 py-1 text-xs text-gray-300 hover:text-gray-100 bg-black/60 rounded"
          >
            Trocar video
          </button>
        </div>
      )}
    </div>
  );
}
