import uvicorn
from fastapi import FastAPI
from starlette.responses import RedirectResponse
from app.db.database import engine, Base
from app.business_types.routes import business_type_router
from app.order_product.routes import order_product_router
from app.orders.routes import order_router

Base.metadata.create_all(bind=engine)


def init_app():
    app = FastAPI()
    app.include_router(business_type_router)
    app.include_router(order_product_router)
    app.include_router(order_router)
    return app


app = init_app()


@app.get("/", include_in_schema=False)
def hello_world():
    return RedirectResponse('/docs')


if __name__ == "__main__":
    uvicorn.run(app)
