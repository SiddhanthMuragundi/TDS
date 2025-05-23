from typing import List
from fastapi import FastAPI, Query
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

file_path = "q-vercel-python.json"
with open(file_path, "r") as f:
    student_records = json.load(f)

student_data = {student["name"]: student["marks"] for student in student_records}

@app.get("/")
def get_marks(name: List[str] = Query([])):
    marks = [student_data.get(n, None) for n in name]
    return JSONResponse(content={"marks": marks})