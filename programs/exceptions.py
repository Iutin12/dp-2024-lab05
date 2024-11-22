class OutOfStockError(Exception):
    """
    Исключение, которое выбрасывается, когда товар отсутствует на складе
    """
    pass


class PaymentProcessingError(Exception):
    """
    Исключение, которое выбрасывается, когда возникает ошибка при обработке платежа
    """
    pass


class DeliveryError(Exception):
    """
    Исключение, которое выбрасывается, когда возникает ошибка при доставке
    """
    pass

class MissingOrderDataError(Exception):
    """
    Исключение, которое выбрасывается, когда в заказе отсутствуют обязательные данные
    """
    pass
