from typing import Any


class Serializer:
    
    @staticmethod
    def deserialize(cassette_string: str) -> dict[str, Any]:
        ...

    @staticmethod
    def serialize(cassette_dict: dict[str, Any]) -> str:
        ...
