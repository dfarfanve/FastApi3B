# main.py
from fastapi import FastAPI
from db.sqlite import create_db_and_tables
from src.api import rest as router
from src.job import start_scheduler

app = FastAPI()

create_db_and_tables()

app.include_router(router, prefix="/api")


@app.on_event("startup")
def startup_event():
    start_scheduler()
    print("Scheduler started")
