import uvicorn
from fastapi import FastAPI
from starlette.responses import RedirectResponse
from app.db.database import engine, Base
from app.business_types.routes import business_type_router
from app.order_product.routes import order_product_router
from app.orders.routes import order_router
from app.product_categories.routes import product_category_router
from app.products.routes import product_router
from app.wholesaler_has_products.routes import wholesaler_has_products_router
from app.wholesalers.routes import wholesaler_router
from app.retailers.routes import retailer_router
from app.users.routes import user_router
from app.payments.routes import payment_router
from app.payment_status.routes import payment_status_router
from app.order_status.routes import order_status_router

Base.metadata.create_all(bind=engine)


def init_app():
    app = FastAPI()
    app.include_router(user_router)
    app.include_router(wholesaler_router)
    app.include_router(wholesaler_has_products_router)
    app.include_router(retailer_router)
    app.include_router(business_type_router)
    app.include_router(order_router)
    app.include_router(order_status_router)
    app.include_router(order_product_router)
    app.include_router(product_router)
    app.include_router(product_category_router)
    app.include_router(payment_router)
    app.include_router(payment_status_router)
    return app


app = init_app()


@app.get("/", include_in_schema=False)
def hello_world():
    return RedirectResponse('/docs')


if __name__ == "__main__":
    uvicorn.run(app)
