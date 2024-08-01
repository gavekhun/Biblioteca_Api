from src.models import Base
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy import String, DateTime
from typing import List
from datetime import datetime
from src.models.book import Book


class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30), nullable=False)
    full_name: Mapped[str] = mapped_column(String(64), nullable=False)
    number_phone: Mapped[str] = mapped_column(String(15), nullable=False)
    email: Mapped[str] = mapped_column(String(30), nullable=False, unique=True)
    creation_date: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    books: Mapped[List["Book"]] = relationship(back_populates="user")

    def __repr__(self) -> str:
        return (f"User(id={self.id!r}, name={self.name!r}, full_name={self.full_name!r},"
                f" number_phone={self.number_phone!r}, email={self.email!r}, creation_date={self.creation_date!r})")
