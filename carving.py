# carving.py
import base64, os, random, string
from fastapi.responses import JSONResponse

FILE_CARVE_DIR = "/tmp/"
FILE_CARVE_MAP = {}

def start_carve(data):
    sid = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
    FILE_CARVE_MAP[sid] = {
        "block_count": int(data["block_count"]),
        "block_size": int(data["block_size"]),
        "blocks_received": {},
        "carve_size": int(data["carve_size"]),
        "carve_guid": data["carve_id"]
    }
    return {"session_id": sid}

def continue_carve(data):
    session_id = data["session_id"]
    block_id = int(data["block_id"])
    if block_id in FILE_CARVE_MAP[session_id]["blocks_received"]:
        return {}
    FILE_CARVE_MAP[session_id]["blocks_received"][block_id] = data["data"]

    if len(FILE_CARVE_MAP[session_id]["blocks_received"]) < FILE_CARVE_MAP[session_id]["block_count"]:
        return {}

    out_file_name = os.path.join(FILE_CARVE_DIR, FILE_CARVE_MAP[session_id]["carve_guid"])
    out_file_name += ".zst" if base64.b64decode(FILE_CARVE_MAP[session_id]["blocks_received"][0])[:4] == b"\x28\xB5\x2F\xFD" else ".tar"

    with open(out_file_name, "wb") as f:
        for i in range(FILE_CARVE_MAP[session_id]["block_count"]):
            f.write(base64.b64decode(FILE_CARVE_MAP[session_id]["blocks_received"][i]))

    FILE_CARVE_MAP[session_id] = {}
    return {"status": "success"}
