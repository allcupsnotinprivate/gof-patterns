# Use Case: Global Logger (Singleton)
#
# This class represents a centralized logging system that ensures
# all log messages are handled by the same instance throughout the application.
# By using the Singleton pattern with a metaclass, we ensure that only one
# Logger instance exists at any given time.
#
# Benefits:
# - Centralized logging: all log messages go through the same object.
# - Consistent log formatting: ensures uniform structure across the application.
# - Avoids redundant logger instances and memory usage.
#
# Common usage scenarios:
# - Writing logs to a file or console in web or server-side applications.
# - Debugging and tracking errors in large systems.
# - Ensuring that all

from singleton import SingletonMeta


class Logger(metaclass=SingletonMeta):
    def log(self, message: str):
        print(f"[{self.__hash__()}:LOG]: {message}")


if __name__ == "__main__":
    a = Logger()
    b = Logger()
    a.log("First message")
    b.log("Second message")
