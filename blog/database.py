from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:////tmp/test.db', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def db_seed():

    # drop and recreate all
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    # insert dummy user
    from models import Post

    db_session.add(Post('Admin\'s first post', 'Post content of first post', 1))
    db_session.commit()

def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    db_seed()