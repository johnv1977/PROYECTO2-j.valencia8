from abc import ABC, abstractmethod


class ISalable(ABC):
    '''
    (Abstracto). Representa un elemento que se puede vender.
    '''

    @abstractmethod
    def is_available(self) -> bool:
        '''
        Comprueba si el elemento está disponible para vender.
        Returns:
            bool: True si el elemento está disponible, False en caso contrario.
        '''
        pass

    @abstractmethod
    def register_sale(self) -> None:
        '''
        Registra la venta de un elemento.
        Returns:
            None
        '''
        pass

    @abstractmethod
    def supply(self) -> None:
        '''
        Abastecer el ingrediente.
        Returns:
            None
        '''
        pass
