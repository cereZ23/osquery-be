# handlers.py
from fastapi import APIRouter, Request, HTTPException
from auth import validate_enroll_secret, validate_node_key, save_node_key
from carving import start_carve, continue_carve
from utils import debug, RECEIVED_REQUESTS, EXAMPLE_CONFIG
from db import get_node_by_key

router = APIRouter()

@router.post("/enroll")
async def enroll(request: Request):
    data = await request.json()
    RECEIVED_REQUESTS.append({"command": "enroll", **data})
    if not validate_enroll_secret(data.get("enroll_secret")):
        raise HTTPException(status_code=403, detail="Invalid enroll secret")
    node_key = save_node_key()
    return {"node_key": node_key}

@router.post("/config")
async def config(request: Request):
    data = await request.json()
    RECEIVED_REQUESTS.append({"command": "config", **data})
    if not get_node_by_key(data.get("node_key")):
        raise HTTPException(status_code=403, detail="Invalid node key")
    return EXAMPLE_CONFIG

@router.post("/log")
async def log(request: Request):
    data = await request.json()
    RECEIVED_REQUESTS.append({"command": "log", **data})
    return {}

@router.post("/distributed_read")
async def distributed_read(request: Request):
    data = await request.json()
    if not get_node_by_key(data.get("node_key")):
        raise HTTPException(status_code=403, detail="Invalid node key")
    return {"queries": {"info": "select count(1) from osquery_info"}}

@router.post("/distributed_write")
async def distributed_write(request: Request):
    data = await request.json()
    RECEIVED_REQUESTS.append({"command": "distributed_write", **data})
    return {}

@router.post("/carve_init")
async def carve_init(request: Request):
    data = await request.json()
    return start_carve(data)

@router.post("/carve_block")
async def carve_block(request: Request):
    data = await request.json()
    return continue_carve(data)

@router.get("/test_read_requests")
async def test_read_requests():
    return RECEIVED_REQUESTS
