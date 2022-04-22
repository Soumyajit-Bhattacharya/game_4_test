from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# database url
SQLALCHEMY_DATABASE_URL = 'mysql+mysqlconnector://test_user:April2022!@localhost/test_db'

# created an engine to connect to db url
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# created a session
Sessionlocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base = declarative_base()

# Dependency
def get_db():
    db = Sessionlocal()
    try:
        yield db
    finally:
        db.close()