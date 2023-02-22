import hashlib
from app.db.database import SessionLocal
from app.users.exceptions import UserInvalidPassword, UserNotFound
from app.users.repositories.user_repository import UserRepository


class UserServices:
    @staticmethod
    def create_user(username, email, password: str):
        """
        It creates a user in the database
        """
        with SessionLocal() as db:
            try:
                user_repository = UserRepository(db)
                hashed_password = hashlib.sha256(bytes(password, "utf-8")).hexdigest()
                return user_repository.create_user(username, email, hashed_password)
            except Exception as e:
                raise e

    @staticmethod
    def create_super_user(username, email, password):
        """
        It creates a superuser
        """
        with SessionLocal() as db:
            try:
                user_repository = UserRepository(db)
                hashed_password = hashlib.sha256(bytes(password, "utf-8")).hexdigest()
                return user_repository.create_super_user(username, email, hashed_password)
            except Exception as e:
                raise e

    @staticmethod
    def login_user(email: str, password: str):
        """
        > This function takes an email and password, and returns a user object if the password is correct
        """
        with SessionLocal() as db:
            try:
                user_repository = UserRepository(db)
                user = user_repository.get_user_by_email(email)
                if hashlib.sha256(bytes(password, "utf-8")).hexdigest() != user.password:
                    raise UserInvalidPassword(message="Invalid password for user", code=401)
                return user
            except Exception as e:
                raise e

    @staticmethod
    def get_all_users():
        """
        It gets all users from the database
        """
        try:
            with SessionLocal() as db:
                user_repository = UserRepository(db)
                return user_repository.get_all_users()
        except Exception as e:
            raise e

    @staticmethod
    def get_user_by_id(user_id: str):
        """
        Get a user by id
        """
        try:
            with SessionLocal() as db:
                user_repository = UserRepository(db)
                return user_repository.get_user_by_id(user_id)
        except Exception:
            raise UserNotFound(code=400, message=f"User with provided id: {user_id} does not exist.")

    @staticmethod
    def get_user_by_username(username: str):
        """
        Get a user by username
        """
        with SessionLocal() as db:
            user_repository = UserRepository(db)
            return user_repository.get_user_by_username(username)

    @staticmethod
    def get_user_by_email(email: str):
        """
        > This function gets a user by email
        """
        try:
            with SessionLocal() as db:
                user_repository = UserRepository(db)
                return user_repository.get_user_by_email(email)
        except Exception:
            raise UserNotFound(code=400, message=f"User with provided email: {email} does not exist.")

    @staticmethod
    def update_user(user_id: str, username: str, password: str, is_active: bool):
        """
        Update a user in the database
        """
        with SessionLocal() as db:
            try:
                user_repository = UserRepository(db)
                return user_repository.update_user(user_id, username, password, is_active)
            except UserNotFound as e:
                raise e
            except Exception as e:
                raise e

    @staticmethod
    def delete_user_by_id(user_id: str):
        """
        > This function deletes a user from the database by their id
        """
        try:
            with SessionLocal() as db:
                user_repository = UserRepository(db)
                return user_repository.delete_user_by_id(user_id)
        except Exception:
            raise UserNotFound(code=400, message=f"User with provided id: {user_id} does not exist.")
