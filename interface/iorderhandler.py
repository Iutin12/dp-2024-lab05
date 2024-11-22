from abc import ABC, abstractmethod
from typing import Dict

class IOrderHandler(ABC):
    """
    Абстрактный базовый класс для обработчиков заказа, определяющий интерфейс для обработки и установки цепочки обработчиков.
    """

    @abstractmethod
    def handle(self, order: Dict[str, any]) -> None:
        """
        Метод обработки заказа.

        :param order: Данные заказа в виде словаря
        """
        pass

    @abstractmethod
    def set_next(self, handler: 'IOrderHandler') -> 'IOrderHandler':
        """
        Метод для установки следующего обработчика в цепочку обработчиков.

        :param handler: Следующий обработчик в цепочке
        :return: Возвращает этот обработчик для дальнейшей настройки цепочки
        """
        pass
