import uuid
from db import save_node, get_node_by_key

HTTP_SERVER_ENROLL_SECRET = "supersecret"

def validate_enroll_secret(secret):
    return secret == HTTP_SERVER_ENROLL_SECRET

def save_node_key():
    node_key = str(uuid.uuid4())
    save_node(node_key)
    return node_key

def validate_node_key(key):
    return get_node_by_key(key) is not None
