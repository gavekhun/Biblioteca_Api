import config

from sqlalchemy import URL
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager

engine = URL.create("mysql+pymysql",
                    host=config.MYSQL_HOST,
                    username=config.MYSQL_USER,
                    password=config.MYSQL_PASSWORD,
                    database=config.MYSQL_DATABASE,
                    port=config.MYSQL_PORT)

sess = sessionmaker(create_engine(engine, echo=True, pool_pre_ping=True), expire_on_commit=False, autoflush=False)


@contextmanager
def session_scope():
    session = sess()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()
