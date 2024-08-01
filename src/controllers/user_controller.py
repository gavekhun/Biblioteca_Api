import http
from sqlalchemy import select, delete, update, insert
from sqlalchemy.exc import SQLAlchemyError
from src.models import User


class UserController:
    def __init__(self, session):
        self.session = session

    def get_users(self):
        try:
            users = self.session.scalars(select(User)).all()
            return users
        except SQLAlchemyError as e:
            #
            raise Exception(f"An error occurred while retrieving users: {str(e)}")

    def get_user_by_name(self, name):
        try:
            query = select(User).where(User.name == name)
            return self.session.execute(query).scalar_one_or_none()
        except SQLAlchemyError as e:

            raise Exception(f"An error occurred while retrieving user by name: {str(e)}")

    def create_user(self, user):
        try:
            query = insert(User).values(name=user.name, email=user.email, full_name=user.full_name,
                                        number_phone=user.number_phone, books=user.books)
            result = self.session.execute(query)
            self.session.commit()
            return result.inserted_primary_key
        except SQLAlchemyError as e:
            self.session.rollback()

            raise Exception(f"An error occurred while creating user: {str(e)}")
