from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

import numpy as np
from input import input
from echo import echo
from gridgen import gridgen

app = FastAPI()

cases = []

class InitializeRequest(BaseModel):
    cases_file: str

class ProcessCaseRequest(BaseModel):
    case_number: int

@app.post("/initialize")
def initialize(request: InitializeRequest):
    global cases
    cases = []

    with open(request.cases_file, 'r') as casefile:
        ncase = int(casefile.readline().strip())

        for _ in range(ncase):
            data = casefile.readline().split()
            cases.append(data[:4])

    return {"message": "Initialized", "num_cases": ncase}

@app.post("/processCase")
def process_case(request: ProcessCaseRequest):
    case_number = request.case_number
    if case_number < 1 or case_number > len(cases):
        raise HTTPException(status_code=400, detail="Invalid case number")

    case = cases[case_number - 1]
    datafn, outpfn1, outpfn2, _ = case

    outpfn4, xl, yl, nx, ny = input(datafn)

    ib, jb = 1, 1
    id, jd = 99, 99
    ie = (ib - 1) + nx
    je = (jb - 1) + ny

    echo(outpfn1, datafn, ib, ie, jb, je, id, jd, xl, yl, nx, ny)
    dx, dy, *grid_data = gridgen(ib, ie, jb, je, nx, ny, xl, yl, 1.0)

    return {"message": f"Processed case {case_number}"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
