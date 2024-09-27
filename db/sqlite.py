# sqlite.py
from sqlmodel import SQLModel, create_engine

# Connect to sqlite
sqlite_file_name = "fastapi.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"
engine = create_engine(sqlite_url, echo=True)


# Create tables if not exist
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
