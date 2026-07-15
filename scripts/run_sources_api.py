import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

# Init DB
from deeptutor.services.sources import init_sources_db
init_sources_db()
print("[sources] DB initialized with seed providers")

# Run API
from fastapi import FastAPI
from deeptutor.services.sources.api import router
import uvicorn

app = FastAPI(title="Source Providers API", version="0.1.0")
app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
