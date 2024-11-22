from programs.exceptions import MissingOrderDataError
from typing import Dict
from handlers.basehendler import BaseOrderHandler

class OrderHandler(BaseOrderHandler):
    def __init__(self):
        super().__init__()

    def handle(self, order: Dict[str, any]) -> None:
        """
        Выполняет начальную обработку заказа. Проверяет наличие всех обязательных данных
        """
        print("Начальная обработка заказа...")

        if 'item' not in order or 'payment' not in order or 'address' not in order:
            raise MissingOrderDataError("Не все данные заказа предоставлены.")

        self.handle_next(order)
