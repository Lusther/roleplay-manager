from database import Base, engine
import models.campaign
import models.user
import models.user_campaign
import models.character
import models.classe
import models.map
import models.object
import models.statistic
import models.token
import models.character_object
import models.character_statistic
import models.classe_statistic
from fastapi import FastAPI

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI"}
