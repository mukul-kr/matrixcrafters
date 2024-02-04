
from app import app
from fastapi import HTTPException, status, Query, Response


@app.get("/health_check")
def health_check():
    return {"status": "OK"}

@app.get("/read/{param}")
def read(param):
    mesasge = f"read {param} successfull"
    return {"message": mesasge}


@app.post("/create")
def create():
    mesasge = f"created successfull"
    return {"message": mesasge}

@app.put("/update/{param}")
def update(param):
    mesasge = f"udpated {param} successfull"
    return {"message": mesasge}

@app.delete("/delete/{param}")
def delete_user(param):
    mesasge = f"deleted {param} successfull"
    return {"message": mesasge}

@app.get("/search")
def search():
    mesasge = f"search successfull"
    return {"message": mesasge}