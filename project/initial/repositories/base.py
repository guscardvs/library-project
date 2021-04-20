import json
from abc import (
    ABC,
    abstractmethod
)

from settings import BASE_DIR


class Repository(ABC):
    @property
    @abstractmethod
    def filename(self) -> str:
        ...

    @property
    @abstractmethod
    def default_json(self) -> dict:
        ...

    def get_file(self):
        return BASE_DIR / self.filename

    def _persist_data(self, data: dict):
        with self.get_file().open("w") as buffer:
            json.dump(data, buffer, indent=2, default=str)

    def _read_data(self):
        file = self.get_file()
        if file.exists():
            return json.loads(file.read_text())
        return self.default_json
