from abc import ABC, abstractmethod

class ICommand(ABC):
    """
    Интерфейс команды, определяющий метод execute для выполнения действия
    """

    @abstractmethod
    def execute(self) -> None:
        """Выполняет команду"""
        pass
