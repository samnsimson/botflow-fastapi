from sqlmodel import SQLModel, Session, create_engine
from config import config

engine = create_engine(config.DATABASE_URL, echo=True)


def init_db():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
