from app.database import Base, engine
from fastapi import FastAPI
from app.routes import user

Base.metadata.create_all(bind=engine)

print("Ok")

app = FastAPI()
app.include_router(user.router)

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI"}
