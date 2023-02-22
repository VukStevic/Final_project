from fastapi import APIRouter, Depends
from app.users.controllers import JWTBearer
from app.wholesalers.controllers import WholesalerController
from app.wholesalers.schemas import *


wholesaler_router = APIRouter(prefix="/api/wholesalers", tags=["Wholesalers"])


@wholesaler_router.post("/add-new-wholesaler", response_model=WholesalerSchema)
def create_wholesaler(wholesaler: WholesalerSchemaIn):
    return WholesalerController.create_wholesaler(wholesaler.name, wholesaler.hq_location, wholesaler.landline,
                                                  wholesaler.business_email, wholesaler.business_type_id,
                                                  wholesaler.user_id)


@wholesaler_router.get("/get-all-wholesalers", response_model=list[WholesalerSchema])
def get_all_wholesalers():
    return WholesalerController.get_all_wholesalers()


@wholesaler_router.get("/id", response_model=WholesalerSchema)
def get_wholesaler_by_id(wholesaler_id: str):
    return WholesalerController.get_wholesaler_by_id(wholesaler_id)


@wholesaler_router.delete("/", dependencies=[Depends(JWTBearer("super_user"))])
def delete_wholesaler_by_id(wholesaler_id: str):
    return WholesalerController.delete_wholesaler_by_id(wholesaler_id)


@wholesaler_router.put("/update/name", response_model=WholesalerSchema)
def update_wholesaler_name(wholesaler_id: str, name: str):
    return WholesalerController.update_wholesaler_name(wholesaler_id, name)


@wholesaler_router.put("/update/landline", response_model=WholesalerSchema)
def update_wholesaler_landline(wholesaler_id: str, landline: str):
    return WholesalerController.update_wholesaler_landline(wholesaler_id, landline)


@wholesaler_router.put("/update/business-email", response_model=WholesalerSchema)
def update_wholesaler_business_email(wholesaler_id: str, business_email: str):
    return WholesalerController.update_wholesaler_business_email(wholesaler_id, business_email)


@wholesaler_router.put("/update-wholesaler", response_model=WholesalerSchema)
def update_wholesaler(wholesaler: WholesalerSchemaUpdate):
    return WholesalerController.update_wholesaler(wholesaler_id=wholesaler.wholesaler_id, name=wholesaler.name,
                                                  landline=wholesaler.landline, hq_location=wholesaler.hq_location,
                                                  business_email=wholesaler.business_email)
