from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "API12346"}

@app.get("/abc")
def abc():
    return {"Hello": "ABC"}

@app.get("/xyz")
def xyz():
    return 123