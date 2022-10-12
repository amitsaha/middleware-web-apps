from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from auth_header_check import AuthHeaderCheck

app = FastAPI()
app.add_middleware(AuthHeaderCheck, include_patterns=["/api"])


@app.get("/")
async def index():
    return HTMLResponse("Hello world")

@app.get("/api/protected")
async def protected():
    return HTMLResponse("This is a protected resource")
