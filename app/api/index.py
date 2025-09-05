import os
import json
from typing import List
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

@app.post("/swap-colour")
async def swap_colour(request: Request):
    data = await request.json()
    colour = data.get("colour")
    if colour == "red":
        return JSONResponse({"colour": "green"})
    elif colour == "green":
        return JSONResponse({"colour": "red"})
    else:
        return JSONResponse({"error": "Invalid colour"}, status_code=400)