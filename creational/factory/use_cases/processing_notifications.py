# Use Case: Notification System via Factory Method Pattern
#
# This module demonstrates a flexible notification system using
# the Factory Method design pattern. It defines a common interface
# for different types of notifiers (Email, SMS, Push) and allows
# runtime selection of the appropriate notification channel.
#
# Benefits:
# - Open/Closed Principle: new notification types can be added without
#   modifying existing code.
# - Decouples client logic from specific implementations of notifiers.
# - Centralized control of object creation logic.
#
# Common usage scenarios:
# - Sending alerts or status updates across multiple communication channels.
# - Integrating external services (e.g., Twilio, SMTP) behind unified interfaces.
# - Configurable or dynamic notification routing based on user settings or context.

from abc import ABC, abstractmethod


class Notifier(ABC):
    @abstractmethod
    def send(self, user: str, message: str) -> str:
        raise NotImplementedError


class EmailNotifier(Notifier):
    def send(self, user: str, message: str) -> str:
        return f"[EMAIL] To {user}: {message}"


class SMSNotifier(Notifier):
    def send(self, user: str, message: str) -> str:
        return f"[SMS] To {user}: {message}"


class PushNotifier(Notifier):
    def send(self, user: str, message: str) -> str:
        return f"[PUSH] To {user}: {message}"


class NotifierFactory(ABC):
    @abstractmethod
    def create_notifier(self) -> Notifier:
        raise NotImplementedError


class EmailFactory(NotifierFactory):
    def create_notifier(self) -> Notifier:
        return EmailNotifier()


class SMSFactory(NotifierFactory):
    def create_notifier(self) -> Notifier:
        return SMSNotifier()


class PushFactory(NotifierFactory):
    def create_notifier(self) -> Notifier:
        return PushNotifier()


def notify_user(factory: NotifierFactory, user: str, message: str):
    notifier = factory.create_notifier()
    print(notifier.send(user, message))


if __name__ == "__main__":
    notify_user(EmailFactory(), "alice@example.com", "Your report is ready")
    notify_user(SMSFactory(), "+123456789", "Your code is 1234")
