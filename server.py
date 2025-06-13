from fastapi import FastAPI, Request, HTTPException, status
from fastapi.responses import JSONResponse
from handlers import router as handlers_router
import uvicorn
from db import init_db
app = FastAPI(title="Osquery TLS Server")

init_db()
app.include_router(handlers_router)

@app.get("/")
async def root():
    return {"status": "ok"}

if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=8443, ssl_certfile="cert.pem", ssl_keyfile="key.pem")
