
from fastapi import FastAPI
from routers import users, complaints, actions
from db.database import Base, engine
app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(users.router)
app.include_router(complaints.router)
app.include_router(actions.router)

