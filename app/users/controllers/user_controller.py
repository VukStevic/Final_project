from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from app.users.exceptions import UserInvalidPassword, UserNotFound
from app.users.services import UserServices, signJWT


class UserController:
    @staticmethod
    def create_user(username, email, password):
        """
        It creates a user
        """
        try:
            user = UserServices.create_user(username, email, password)
            return user
        except IntegrityError:
            raise HTTPException(
                status_code=400,
                detail=f"User with provided email - {email} already exists.",
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def create_super_user(username, email, password):
        """
        It creates a superuser
        """
        try:
            user = UserServices.create_super_user(username, email, password)
            return user
        except IntegrityError as e:
            raise HTTPException(
                status_code=400,
                detail=f"User with provided email - {email} already exists.",
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def login_user(email, password):
        """
        It tries to log in a user with the given email and password, if it succeeds, it returns a JWT token,
        otherwise it raises an exception
        """
        try:
            user = UserServices.login_user(email, password)
            if user.is_superuser:
                return signJWT(user.id, "super_user")
            return signJWT(user.id, "classic_user")
        except UserInvalidPassword as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_all_users():
        """
        It returns all users
        """
        users = UserServices.get_all_users()
        return users

    @staticmethod
    def get_user_by_id(user_id: str):
        """
        It gets a user by id.
        """
        user = UserServices.get_user_by_id(user_id)
        if user:
            return user
        else:
            raise HTTPException(
                status_code=400,
                detail=f"User with provided id {user_id} does not exist",
            )

    @staticmethod
    def get_user_by_email(email: str):
        """
        If the user exists, return the user, otherwise raise an exception
        """
        user = UserServices.get_user_by_email(email)
        if user:
            return user
        else:
            raise HTTPException(
                status_code=400,
                detail=f"User with provided email {email} does not exist",
            )

    @staticmethod
    def get_user_by_username(username: str):
        """
        If the user exists, return the user, otherwise raise an exception
        """
        user = UserServices.get_user_by_username(username)
        if user:
            return user
        else:
            raise HTTPException(
                status_code=400,
                detail=f"User with provided username {username} does not exist",
            )

    @staticmethod
    def update_user(user_id: str, username: str, password: str, is_active: bool):
        """
        It updates a user.
        """
        try:
            return UserServices.update_user(user_id, username, password, is_active)
        except UserNotFound as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def delete_user_by_id(user_id: str):
        """
        It deletes a user by id
        """
        try:
            UserServices.delete_user_by_id(user_id)
            return {"message": f"User with provided id, {user_id}, is deleted."}
        except UserNotFound:
            raise HTTPException(status_code=400, detail=f"User with provided id: {user_id} does not exist.")
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
