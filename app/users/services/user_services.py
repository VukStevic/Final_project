import hashlib
from app.db.database import SessionLocal
from app.users.exceptions import UserInvalidPassword, UserNotFound
from app.users.repositories.user_repository import UserRepository


class UserServices:
    @staticmethod
    def create_user(username, email, password: str):
        with SessionLocal() as db:
            try:
                user_repository = UserRepository(db)
                hashed_password = hashlib.sha256(bytes(password, "utf-8")).hexdigest()
                return user_repository.create_user(username, email, hashed_password)
            except Exception as e:
                raise e

    @staticmethod
    def create_super_user(username, email, password):
        with SessionLocal() as db:
            try:
                user_repository = UserRepository(db)
                hashed_password = hashlib.sha256(bytes(password, "utf-8")).hexdigest()
                return user_repository.create_super_user(username, email, hashed_password)
            except Exception as e:
                raise e

    @staticmethod
    def login_user(email: str, password: str):
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
        try:
            with SessionLocal() as db:
                user_repository = UserRepository(db)
                return user_repository.get_all_users()
        except Exception as e:
            raise e

    @staticmethod
    def get_user_by_id(user_id: str):
        try:
            with SessionLocal() as db:
                user_repository = UserRepository(db)
                return user_repository.get_user_by_id(user_id)
        except Exception:
            raise UserNotFound(code=400, message=f"User with provided id: {user_id} does not exist.")

    @staticmethod
    def get_user_by_username(username: str):
        with SessionLocal() as db:
            user_repository = UserRepository(db)
            return user_repository.get_user_by_username(username)

    @staticmethod
    def get_user_by_email(email: str):
        try:
            with SessionLocal() as db:
                user_repository = UserRepository(db)
                return user_repository.get_user_by_email(email)
        except Exception:
            raise UserNotFound(code=400, message=f"User with provided email: {email} does not exist.")

    @staticmethod
    def update_user_is_active(user_id: str, is_active: bool):
        with SessionLocal() as db:
            try:
                user_repository = UserRepository(db)
                return user_repository.update_user_is_active(user_id, is_active)
            except Exception:
                raise UserNotFound(code=400, message=f"User with provided id: {user_id} does not exist.")

    @staticmethod
    def delete_user_by_id(user_id: str):
        try:
            with SessionLocal() as db:
                user_repository = UserRepository(db)
                return user_repository.delete_user_by_id(user_id)
        except Exception:
            raise UserNotFound(code=400, message=f"User with provided id: {user_id} does not exist.")
