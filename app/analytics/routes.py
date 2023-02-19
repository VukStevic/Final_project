from fastapi import APIRouter
from app.order_product.controllers import OrderProductController
from app.orders.controllers import OrderController
from app.orders.schemas import OrderSchemaAnalytics


analytics_router = APIRouter(prefix="/api/analytics", tags=["Analytics"])


@analytics_router.get("/get-order-by-wholesaler-and-date-range", response_model=list[OrderSchemaAnalytics])
def get_order_by_wholesaler_and_date_range(wholesaler_id:str, starting_date: str, ending_date: str):
    return OrderController.get_order_by_wholesaler_and_date_range(wholesaler_id=wholesaler_id,
                                                                  starting_date=starting_date,
                                                                  ending_date=ending_date)


@analytics_router.get("/get-order-by-retailer-and-date-range", response_model=list[OrderSchemaAnalytics])
def get_order_by_retailer_and_date_range(retailer_id:str, starting_date: str, ending_date: str):
    return OrderController.get_order_by_retailer_and_date_range(retailer_id=retailer_id,
                                                                starting_date=starting_date,
                                                                ending_date=ending_date)


@analytics_router.get("/get-average-product-price")
def get_average_product_price(wholesaler_product_id: str):
    average_price = OrderProductController.get_average_product_price(wholesaler_product_id)
    return {"average price": average_price}


@analytics_router.get("/get-average-product-count-per-order")
def get_average_product_count_per_order():
    count_per_order = OrderProductController.get_average_product_count_per_order()
    return {"average product count per order": count_per_order}


@analytics_router.get("/get-total-wholesaler-revenue")
def get_total_wholesaler_revenue(wholesaler_id: str):
    total_wholesaler_revenue = OrderProductController.get_total_wholesaler_revenue(wholesaler_id)
    return {"wholesaler_id": wholesaler_id, "total wholesaler revenue": total_wholesaler_revenue}
