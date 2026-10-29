from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def root_read():
    return "hello"

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str):
    return {"item_id": item_id, "q": q}