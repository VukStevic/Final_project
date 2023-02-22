from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.users.exceptions import UserNotFound
from app.users.models import User


class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_user(self, username, email, password):
        """
        It creates a new user and adds it to the database
        """
        try:
            user = User(username, email, password)
            self.db.add(user)
            self.db.commit()
            self.db.refresh(user)
            return user
        except IntegrityError as e:
            raise e

    def create_super_user(self, username, email, password):
        """
        It creates a superuser
        """
        try:
            user = User(username=username, email=email, password=password, is_superuser=True)
            self.db.add(user)
            self.db.commit()
            self.db.refresh(user)
            return user
        except IntegrityError as e:
            raise e

    def get_all_users(self):
        """
        It returns all the users in the database
        """
        users = self.db.query(User).all()
        return users

    def get_user_by_id(self, user_id: str):
        """
        It returns a user object from the database, given a user id
        """
        user = self.db.query(User).filter(User.id == user_id).first()
        return user

    def get_user_by_email(self, email: str):
        """
        It returns the first user in the database whose email matches the email passed in as an argument
        """
        user = self.db.query(User).filter(User.email == email).first()
        return user

    def get_user_by_username(self, username: str):
        """
        It returns the first user in the database whose username matches the username passed in as an argument
        """
        user = self.db.query(User).filter(User.username == username).first()
        return user

    def delete_user_by_id(self, user_id: str):
        """
        It deletes a user from the database by their id
        """
        try:
            user = self.db.query(User).filter(User.id == user_id).first()
            self.db.delete(user)
            self.db.commit()
            return True
        except Exception as e:
            raise e

    def update_user(self, user_id: str, username: str, password: str, is_active: bool):
        """
        It updates a user's username, password, and is_active status if the user exists
        """
        user = self.db.query(User).filter(User.id == user_id).first()
        if not user:
            raise UserNotFound(code=400, message=f"User with provided id: {user_id} not found.")
        if username is not None:
            user.username = username
        if password is not None:
            user.password = password
        if is_active is not None:
            user.is_active = is_active
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user
