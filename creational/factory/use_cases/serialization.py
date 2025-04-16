# Use Case: Data Serialization Engine (Factory Method)
#
# This module provides a flexible mechanism to serialize and deserialize
# data using interchangeable strategies (e.g., JSON, Pickle). The Factory
# Method pattern enables easy extension and runtime selection of the
# serialization format without modifying client code.
#
# Benefits:
# - Pluggable format support: easily add new serializers (e.g., YAML, XML).
# - Separation of concerns: serialization logic is isolated from usage logic.
# - Consistent interface for all formats.
#
# Common usage scenarios:
# - Persisting user or application state to disk or database.
# - Transferring structured data between services or components.
# - Choosing serialization strategy based on configuration, environment, or user input.

import json
import pickle
from abc import ABC, abstractmethod
from typing import Any


class Serializer(ABC):
    @abstractmethod
    def serialize(self, data: Any) -> bytes:
        pass

    @abstractmethod
    def deserialize(self, raw_data: bytes) -> Any:
        pass


class JSONSerializer(Serializer):
    def serialize(self, data: Any) -> bytes:
        return json.dumps(data).encode('utf-8')

    def deserialize(self, raw_data: bytes) -> Any:
        return json.loads(raw_data.decode('utf-8'))


class PickleSerializer(Serializer):
    def serialize(self, data: Any) -> bytes:
        return pickle.dumps(data)

    def deserialize(self, raw_data: bytes) -> Any:
        return pickle.loads(raw_data)


class SerializerFactory(ABC):
    @abstractmethod
    def create_serializer(self) -> Serializer:
        pass


class JSONSerializerFactory(SerializerFactory):
    def create_serializer(self) -> Serializer:
        return JSONSerializer()


class PickleSerializerFactory(SerializerFactory):
    def create_serializer(self) -> Serializer:
        return PickleSerializer()


def save_and_load(factory: SerializerFactory, data: Any):
    serializer = factory.create_serializer()
    raw = serializer.serialize(data)
    restored = serializer.deserialize(raw)
    print(f"Original: {data}")
    print(f"Restored: {restored}")
    print(f"Same: {data == restored}")


if __name__ == "__main__":
    example_data = {"user": "Alice", "age": 30, "active": True}

    print("> Using JSON")
    save_and_load(JSONSerializerFactory(), example_data)

    print("> Using Pickle")
    save_and_load(PickleSerializerFactory(), example_data)
