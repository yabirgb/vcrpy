from typing import Any, TypedDict, Union

class ResponseDict(TypedDict):
    body: dict[str, Union[str, bytes]]
    headers: dict[str, Any]
    status: dict[str, Any]


class CassetteDict(TypedDict):
    requests: dict[str, Any]
    response: ResponseDict