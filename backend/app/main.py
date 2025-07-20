from fastapi import FastAPI
from app.database import create_db
from app.routes import user
from app.routes import campaign
#import uvicorn

create_db()

app = FastAPI()
app.include_router(user.router)
app.include_router(campaign.router)

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI"}

#if __name__ == '__main__':
#    uvicorn.run(app, host='0.0.0.0', port=8000)
