from fastapi import APIRouter, Depends
from app.users.controllers import UserController
from app.users.controllers.user_auth_controller import JWTBearer
from app.users.schemas import *


user_router = APIRouter(prefix="/api/users", tags=["Users"])


@user_router.post("/add-new-user", response_model=UserSchema)
def create_user(user: UserSchemaIn):
    return UserController.create_user(user.username, user.email, user.password)


@user_router.post("/add-new-super-user", response_model=UserSchema, dependencies=[Depends(JWTBearer("super_user"))])
def create_super_user(user: UserSchemaIn):
    return UserController.create_super_user(user.username, user.email, user.password)


@user_router.post("/login")
def login_user(user: UserSchemaIn):
    return UserController.login_user(user.email, user.password)


@user_router.get("/id", response_model=UserSchema)
def get_user_by_id(user_id: str):
    return UserController.get_user_by_id(user_id)


@user_router.get("/email", response_model=UserSchema)
def get_user_by_email(email: str):
    return UserController.get_user_by_email(email)


@user_router.get("/username", response_model=UserSchema)
def get_user_by_username(username: str):
    return UserController.get_user_by_username(username)


@user_router.get("/get-all-users", response_model=list[UserSchema])
def get_all_users():
    return UserController.get_all_users()


@user_router.put("/update/is_active", response_model=UserSchema, dependencies=[Depends(JWTBearer("super_user"))])
def update_user_is_active(user: UserSchemaUpdate):
    return UserController.update_user_is_active(user_id=user.user_id, is_active=user.is_active)


@user_router.delete("/", dependencies=[Depends(JWTBearer("super_user"))])
def delete_user_by_id(user_id: str):
    return UserController.delete_user_by_id(user_id)
