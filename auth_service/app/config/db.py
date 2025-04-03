from sqlalchemy import create_engine
from colorama import init, Fore
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv
load_dotenv()
run_mode = os.getenv("RUN_MODE")
from sqlalchemy.ext.declarative import declarative_base


DATABASE_NAME = os.getenv(f"DATABASE_NAME_{run_mode.upper()}")
DATABASE_PASSWORD = os.getenv(f"DATABASE_PASSWORD_{run_mode.upper()}")
DATABASE_USER_NAME = os.getenv(f"DATABASE_USER_NAME_{run_mode.upper()}")
DATABASE_HOST = os.getenv(f"DATABASE_HOST_{run_mode.upper()}") 
DATABASE_PORT = os.getenv(f"DATABASE_PORT_{run_mode.upper()}") 

DATABASE_URL = f"mysql+pymysql://{DATABASE_USER_NAME}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"
print(Fore.YELLOW +DATABASE_URL)

Base = declarative_base()
def get_connection():
    try:
        engine = create_engine(DATABASE_URL, pool_pre_ping=True)
        print(Fore.GREEN + f"Connection to the {DATABASE_HOST} for user {DATABASE_USER_NAME} created successfully.")
        return engine
    except Exception as e:
        print(Fore.RED +f"Connection could not be made due to the following error: \n{e}")
        return None

engine = get_connection()
if engine:
    Base.metadata.create_all(bind=engine)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    print(Fore.GREEN + "Session manager initialized successfully.")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()