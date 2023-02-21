import pytest
from sqlalchemy.exc import IntegrityError
from app.business_types.repositories import BusinessTypeRepository
from app.tests import TestClass, TestingSessionLocal


class TestBusinessTypeRepo(TestClass):

    def test_business_type(self):
        with TestingSessionLocal() as db:
            business_type_repository = BusinessTypeRepository(db)
            business_type = business_type_repository.create_business_type("name", "description")
            assert business_type.name == "name"
            assert business_type.description == "description"

    def test_business_type_err(self):
        with TestingSessionLocal() as db:
            business_type_repository = BusinessTypeRepository(db)
            business_type_repository.create_business_type("name", "description")
            with pytest.raises(IntegrityError):
                business_type_repository.create_business_type("name", "description")

    def test_get_all_business_types(self):
        with TestingSessionLocal() as db:
            business_type_repository = BusinessTypeRepository(db)
            business_type_repository.create_business_type("name1", "desc")
            business_type_repository.create_business_type("name2", "desc")
            business_type_repository.create_business_type("name3", "desc")
            all_courses = business_type_repository.get_all_business_types()
            assert len(all_courses) == 3

    def test_get_all_business_types_list(self):
        with TestingSessionLocal() as db:
            business_type_repository = BusinessTypeRepository(db)
            result = business_type_repository.get_all_business_types()
            assert isinstance(result, list)
