from fastapi import APIRouter
from app.business_types.schemas import BusinessTypeSchema, BusinessTypeSchemaIn
from app.business_types.controllers import BusinessTypeController


business_type_router = APIRouter(prefix="/api/business-types", tags=["Business types"])


@business_type_router.post("/create-business-type", response_model=BusinessTypeSchema)
def create_business_type(business_type: BusinessTypeSchemaIn):
    return BusinessTypeController.create_business_type(name=business_type.name, description=business_type.description)


@business_type_router.get("/get-all-business-types", response_model=list[BusinessTypeSchema])
def get_all_business_types():
    return BusinessTypeController.get_all_business_types()


@business_type_router.get("/get-business-type-by-id", response_model=BusinessTypeSchema)
def get_business_type_by_id(business_type_id: str):
    return BusinessTypeController.get_business_type_by_id(business_type_id=business_type_id)


@business_type_router.put("/update-business-type-name", response_model=BusinessTypeSchema)
def update_business_type_name(business_type_id: str, name: str):
    return BusinessTypeController.update_business_type_name(business_type_id=business_type_id,
                                                            name=name)


@business_type_router.put("/update-business-type-description", response_model=BusinessTypeSchema)
def update_business_type_description(business_type_id: str, description: str):
    return BusinessTypeController.update_business_type_description(business_type_id=business_type_id,
                                                                   description=description)


@business_type_router.delete("/delete-business-type-by-id")
def delete_business_type_by_id(business_type_id: str):
    return BusinessTypeController.delete_business_type_by_id(business_type_id=business_type_id)
