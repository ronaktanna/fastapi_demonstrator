"""
@author: ronaktanna
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the database URL - SQLite in this case
SQLALCHEMY_DATABASE_URL = "sqlite:///sql_app.db"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    echo=True  # allow logging of SQL commands
)

# Create local session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
db = SessionLocal()
Base = declarative_base()


