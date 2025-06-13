# 🛡️ Osquery TLS Server (FastAPI Edition)

A modular, production-ready **TLS server** for [osquery](https://osquery.io) written in Python using **FastAPI**, with support for:

- 🔐 Secure enrollment via enroll secret
- 📋 Config distribution (`/config`)
- 🧾 TLS logging (`/log`)
- 🧠 Distributed queries
- 🧩 File carving
- 🗃️ SQLite tracking for enrolled nodes

---

## 🚀 Features

- ✅ Fully compatible with osquery's TLS plugin
- 🔐 TLS with self-signed or real certificates
- 🧠 Node tracking using SQLite
- 🪵 Request debug history (`/test_read_requests`)
- ⚙️ Modular Python layout (handlers, DB, auth, carving, utils)

---

## 📦 Requirements

- Python 3.10–3.13
- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/)
- `sqlite3` (included with Python)
- OpenSSL (for local certs)

Install dependencies:
```bash
pip install -r requirements.txt
