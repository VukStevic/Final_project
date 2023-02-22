from fastapi import APIRouter, Depends
from app.business_types.schemas import BusinessTypeSchema, BusinessTypeSchemaIn, BusinessTypeSchemaUpdate
from app.business_types.controllers import BusinessTypeController
from app.users.controllers import JWTBearer


business_type_router = APIRouter(prefix="/api/business-types", tags=["Business types"])


@business_type_router.post("/create-business-type", response_model=BusinessTypeSchema,
                           dependencies=[Depends(JWTBearer("super_user"))])
def create_business_type(business_type: BusinessTypeSchemaIn):
    return BusinessTypeController.create_business_type(name=business_type.name, description=business_type.description)


@business_type_router.get("/get-all-business-types", response_model=list[BusinessTypeSchema])
def get_all_business_types():
    return BusinessTypeController.get_all_business_types()


@business_type_router.get("/get-business-type-by-id", response_model=BusinessTypeSchema)
def get_business_type_by_id(business_type_id: str):
    return BusinessTypeController.get_business_type_by_id(business_type_id=business_type_id)


@business_type_router.put("/update-business-type", response_model=BusinessTypeSchema,
                          dependencies=[Depends(JWTBearer("super_user"))])
def update_business_type(business_type: BusinessTypeSchemaUpdate):
    return BusinessTypeController.update_business_type(business_type_id=business_type.id, name=business_type.name,
                                                       description=business_type.description)


@business_type_router.delete("/delete-business-type-by-id", dependencies=[Depends(JWTBearer("super_user"))])
def delete_business_type_by_id(business_type_id: str):
    return BusinessTypeController.delete_business_type_by_id(business_type_id=business_type_id)
