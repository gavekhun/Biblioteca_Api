import config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager
from src.models import Base


engine = create_engine(
    f"mysql+pymysql://{config.MYSQL_USER}:{config.MYSQL_PASSWORD}@{config.MYSQL_HOST}:{config.MYSQL_PORT}/{config.MYSQL_DATABASE}",
    echo=True,
    pool_pre_ping=True
)


SessionLocal = sessionmaker(
    bind=engine,
    expire_on_commit=False,
    autoflush=False
)


def init_db():
    Base.metadata.create_all(bind=engine)


@contextmanager
def session_scope():

    session = SessionLocal()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()
