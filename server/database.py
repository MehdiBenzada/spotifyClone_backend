from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


database_url="postgresql://postgres:mimilala5@localhost:5432/fluttermusicapp"
 
engine= create_engine(database_url)
sessionlocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)
def get_db():
    db=sessionlocal()
    try:
        yield db
    finally:
        db.close()
    