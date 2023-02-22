from fastapi import APIRouter, Depends
from app.retailers.controllers import RetailerController
from app.retailers.schemas import *
from app.users.controllers import JWTBearer

retailer_router = APIRouter(prefix="/api/retailers", tags=["Retailers"])


@retailer_router.post("/add-new-retailer", response_model=RetailerSchema)
def create_retailer(retailer: RetailerSchemaIn):
    return RetailerController.create_retailer(retailer.name, retailer.hq_location, retailer.landline, 
                                              retailer.business_email, retailer.business_type_id, retailer.user_id)


@retailer_router.get("/get-all-retailers", response_model=list[RetailerSchema])
def get_all_retailers():
    return RetailerController.get_all_retailers()


@retailer_router.get("/id", response_model=RetailerSchema)
def get_retailer_by_id(retailer_id: str):
    return RetailerController.get_retailer_by_id(retailer_id)


@retailer_router.delete("/", dependencies=[Depends(JWTBearer("super_user"))])
def delete_retailer_by_id(retailer_id: str):
    return RetailerController.delete_retailer_by_id(retailer_id)


@retailer_router.put("/update/name", response_model=RetailerSchema)
def update_retailer_name(retailer_id: str, name: str):
    return RetailerController.update_retailer_name(retailer_id, name)


@retailer_router.put("/update/landline", response_model=RetailerSchema)
def update_retailer_landline(retailer_id: str, landline: str):
    return RetailerController.update_retailer_landline(retailer_id, landline)


@retailer_router.put("/update/business-email", response_model=RetailerSchema)
def update_retailer_business_email(retailer_id: str, business_email: str):
    return RetailerController.update_retailer_business_email(retailer_id, business_email)


@retailer_router.put("/update-retailer", response_model=RetailerSchema)
def update_retailer(retailer: RetailerSchemaUpdate):
    return RetailerController.update_retailer(retailer_id=retailer.retailer_id, name=retailer.name,
                                              hq_location=retailer.hq_location, landline=retailer.landline,
                                              business_email=retailer.business_email)
