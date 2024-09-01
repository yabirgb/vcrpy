# .. _persister_example:

from pathlib import Path
from typing import Union

from vcr.serializers.types import Serializer
from vcr.types import CassetteDict

from ..serialize import deserialize, serialize


class CassetteNotFoundError(FileNotFoundError):
    pass


class CassetteDecodeError(ValueError):
    pass


class FilesystemPersister:
    @classmethod
    def load_cassette(cls, cassette_path: Union[str, Path], serializer: Serializer):
        cassette_path = Path(cassette_path)  # if cassette path is already Path this is no operation
        if not cassette_path.is_file():
            raise CassetteNotFoundError()
        try:
            with cassette_path.open() as f:
                data = f.read()
        except UnicodeDecodeError as err:
            raise CassetteDecodeError("Can't read Cassette, Encoding is broken") from err

        return deserialize(data, serializer)

    @staticmethod
    def save_cassette(cassette_path: Path, cassette_dict: CassetteDict, serializer: Serializer):
        data = serialize(cassette_dict, serializer)
        cassette_path = Path(cassette_path)  # if cassette path is already Path this is no operation

        cassette_folder = cassette_path.parent
        if not cassette_folder.exists():
            cassette_folder.mkdir(parents=True)

        with cassette_path.open("w") as f:
            f.write(data)
