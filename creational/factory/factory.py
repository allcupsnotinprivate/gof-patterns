import abc


class Product(abc.ABC):
    """Abstract Product class that defines the interface for concrete products.

    This is the common interface that all concrete products will implement.
    """

    @abc.abstractmethod
    def operation(self) -> str:
        """Method that performs an operation defined by the concrete product.

        Returns:
            str: The result of the operation.
        """
        raise NotImplementedError


class CProductA(Product):
    """Concrete implementation of Product A.

    This class provides the implementation for the `operation` method
    for Product A.
    """

    def operation(self) -> str:
        """Performs the operation specific to Product A.

        Returns:
            str: The result of the operation for Product A.
        """
        return "Result of Concrete Product A"


class CProductB(Product):
    """Concrete implementation of Product B.

    This class provides the implementation for the `operation` method
    for Product B.
    """

    def operation(self) -> str:
        """Performs the operation specific to Product B.

        Returns:
            str: The result of the operation for Product B.
        """
        return "Result of Concrete Product B"


class Fabric(abc.ABC):
    """Abstract Fabric class that defines the factory method.

    This class declares the factory method that will return instances of
    different products. Concrete fabric classes must implement this method.
    """

    @abc.abstractmethod
    def factory_method(self) -> Product:
        """Creates and returns a product instance.

        Returns:
            Product: A concrete product instance.
        """
        pass

    def some_operation(self) -> str:
        """Performs some operation using the created product.

        This method calls the `factory_method` to get a product and
        then uses its `operation` method.

        Returns:
            str: The result of the operation using the created product.
        """
        product = self.factory_method()
        result = f"Creator: use {product.operation()}"
        return result


class CFabricA(Fabric):
    """Concrete Fabric A that creates Product A.

    This class implements the `factory_method` to create an instance of
    Product A.
    """

    def factory_method(self) -> Product:
        """Creates and returns Product A.

        Returns:
            Product: An instance of CProductA.
        """
        return CProductA()


class CFabricB(Fabric):
    """Concrete Fabric B that creates Product B.

    This class implements the `factory_method` to create an instance of
    Product B.
    """

    def factory_method(self) -> Product:
        """Creates and returns Product B.

        Returns:
            Product: An instance of CProductB.
        """
        return CProductB()


def fabric_client(creator: Fabric) -> None:
    """Client function that interacts with a Fabric instance.

    The client works through the interface without knowing the specific
    type of the product created by the factory.

    Args:
        creator (Fabric): A fabric instance that creates products.
    """
    print("Client: does not know the class, but works through the interface:")
    print(creator.some_operation())
