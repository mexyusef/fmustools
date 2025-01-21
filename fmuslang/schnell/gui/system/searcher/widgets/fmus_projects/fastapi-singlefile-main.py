from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/todos")
def get_todos():
    # Implement logic to fetch todos from a database or any other source
    todos = []
    # Return the todos as a JSON response
    return {"todos": todos}

@app.post("/todos")
def create_todo(todo: str):
    # Implement logic to create a new todo
    # You can use a database or any other storage mechanism
    # Return the created todo as a JSON response
    return {"todo": todo, "status": "created"}
