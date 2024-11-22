from programs.exceptions import DeliveryError
from typing import Dict
from handlers.basehendler import BaseOrderHandler

class DeliveryHandler(BaseOrderHandler):
    def handle(self, order: Dict[str, any]) -> None:
        """
        Осуществляет доставку товара. Если адрес не указан, вызывает исключение
        """
        print(f"Доставка товара на адрес {order.get('address')}...")

        if not order.get('address'):
            raise DeliveryError("Адрес доставки не указан.")

        print(f"Заказ доставлен по адресу {order['address']}.")

        self.handle_next(order)
