from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
DB_USERNAME = "postgres"
DB_PASSWORD = "AcademyRootPassword"
DB_HOSTNAME = "localhost"
DB_PORT = "5432"
DATABASE = "village_voice_api"

DB_URL = f"postgresql+psycopg2://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOSTNAME}:{DB_PORT}/{DATABASE}"

#create engine
engine = create_engine(DB_URL)

#create session 
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

#create your base
Base = declarative_base()