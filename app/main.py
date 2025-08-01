from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from redis import Redis
from starlette.requests import Request

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")
rdb = Redis(host="redis", port=6379, decode_responses=True)

@app.get("/", response_class=HTMLResponse)
async def get_clipboard(request: Request):
    value = rdb.get("shared_clipboard") or ""
    return templates.TemplateResponse("index.html", {"request": request, "value": value})

@app.post("/update")
async def update_clipboard(value: str = Form(...)):
    rdb.set("shared_clipboard", value)
    return RedirectResponse("/", status_code=303)