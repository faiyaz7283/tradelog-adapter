from pydantic import BaseModel


class OrderScheme(BaseModel):
    order_id: str
    symbol: str
    quantity: float
    asset_type: str
    strike: float
    expiration_date: str
    average_cost: float
    commission: float
    filled_time: str
