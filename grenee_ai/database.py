from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessinmaker

DATABASE_URL="postgresql://postgres:bluemoon@localhost/grenee_db"

engine=create_engine(DATABASE_URL)
SessionLocal=sessinmaker(bind=engine)
metadata=MetaData()