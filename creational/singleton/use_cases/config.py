# Use Case: Global Application Configuration (Singleton)
#
# This class represents a centralized configuration manager for an application.
# By applying the Singleton pattern via a decorator, we ensure that all modules
# share the same configuration instance during runtime.
#
# Benefits:
# - Settings are loaded once and stay consistent across the entire app.
# - Avoids the need to pass config objects between modules.
# - Simplifies global access to configuration values.
#
# Common usage scenarios:
# - Loading environment-specific settings (e.g., dev/staging/prod).
# - Centralizing feature flags or debug toggles.
# - Accessing config in large apps without tight coupling.

from singleton import singleton_decorator


@singleton_decorator
class Config:

    def __init__(self):
        self.settings = {}

    def load(self, data: dict):
        self.settings.update(data)


if __name__ == "__main__":
    config1 = Config()
    config1.load({"debug": True, "port": 8000})

    config2 = Config()
    print(config2.settings)
