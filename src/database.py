from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

db_url = 'localhost:3306'
db_name = 'online-exam'
db_user = 'root'
db_password = ''
engine = create_engine(f'mysql+pymysql://{db_user}:{db_password}@{db_url}/{db_name}')

db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    import src.entities
    Base.metadata.create_all(bind=engine)
