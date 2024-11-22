from interface.iorderhandler import IOrderHandler
from programs.exceptions import OutOfStockError
from programs.inventory import inventory
from typing import Dict
from handlers.basehendler import BaseOrderHandler

class StockCheckHandler(BaseOrderHandler):
    def handle(self, order: Dict[str, any]) -> None:
        """
        Проверяет наличие товара на складе. Если товар отсутствует, вызывает исключение
        """
        print("Проверка наличия товара на складе...")
        if inventory.get(order['item'], 0) == 0:
            raise OutOfStockError(f"Товар {order['item']} отсутствует на складе")
        print(f"Товар {order['item']} в наличии.")

        self.handle_next(order)

    def set_next(self, handler: IOrderHandler) -> IOrderHandler:
        """
        Устанавливает следующий обработчик в цепочку.
        """
        self.next_handler = handler
        return handler
