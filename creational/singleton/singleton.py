
# Metaclass implementation

class SingletonMeta(type):
    """A metaclass that ensures only one instance of a class is created.

    This metaclass controls the instantiation of classes. When a class
    uses `SingletonMeta` as its metaclass, it ensures that only one instance
    of the class is created throughout the application's lifecycle.

    Attributes:
        _instances (dict): A dictionary holding the singleton instances of classes.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """Returns the single instance of the class.

        If the class has already been instantiated, returns the existing instance.
        If not, creates a new instance and stores it for future use.

        Args:
            *args: Arguments to pass to the class constructor.
            **kwargs: Keyword arguments to pass to the class constructor.

        Returns:
            object: The singleton instance of the class.
        """
        instance = cls._instances.get(cls)
        if not instance:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return instance


# Decorator implementation

def singleton_decorator(cls):
    """A decorator that ensures only one instance of a class is created.

    This decorator ensures that only one instance of the decorated class is created.
    The first time the class is instantiated, it stores the instance and returns it
    for subsequent calls, avoiding the creation of new instances.

    Args:
        cls (type): The class to decorate with the singleton behavior.

    Returns:
        type: The decorated class with singleton behavior.
    """
    instances = {}

    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return wrapper
