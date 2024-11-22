from typing import Dict, Optional
from interface.iorderhandler import IOrderHandler

class BaseOrderHandler(IOrderHandler):
    """
    Базовый класс для обработчиков заказов. Реализует общую логику установки следующего обработчика
    """

    def __init__(self):
        self.next_handler: Optional[IOrderHandler] = None

    def set_next(self, handler: IOrderHandler) -> IOrderHandler:
        """
        Устанавливает следующий обработчик в цепочкe

        :param handler: Следующий обработчик в цепочке
        :return: Возвращает текущий обработчик для дальнейшей настройки цепочки
        """
        self.next_handler = handler
        return handler

    def handle_next(self, order: Dict[str, any]) -> None:
        """
        Если есть следующий обработчик, передает выполнение следующему хендлеру
        """
        if self.next_handler:
            self.next_handler.handle(order)
