from fastapi import FastAPI, HTTPException
from app.operations import add, subtract, multiply, divide
import logging

app = FastAPI()

logging.basicConfig(level=logging.INFO)

@app.get("/")
def read_root():
    return {"message": "Calculator API"}

@app.get("/add")
def add_numbers(a: float, b: float):
    result = add(a, b)
    logging.info(f"Add: {a} + {b} = {result}")
    return {"result": result}

@app.get("/divide")
def divide_numbers(a: float, b: float):
    try:
        result = divide(a, b)
        logging.info(f"Divide: {a} / {b} = {result}")
        return {"result": result}
    except ValueError as e:
        logging.error(str(e))
        raise HTTPException(status_code=400, detail=str(e))