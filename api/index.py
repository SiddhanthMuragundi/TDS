from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import json
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

file_path = os.path.join(os.path.dirname(__file__), "q-vercel-python.json")
with open(file_path, "r") as f:
    student_records = json.load(f)

student_data = {student["name"]: student["marks"] for student in student_records}

@app.get("/")
def get_marks(request: Request):
    names = request.query_params.getlist("name")
    marks = [student_data.get(name, None) for name in names]
    return JSONResponse(content={"marks": marks})
