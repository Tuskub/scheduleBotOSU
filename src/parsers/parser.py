from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Dict


@dataclass()
class Parser(ABC):
    def parse(self, path, params):
        file = self._open_file(path, params)
        raw_data = self._extract_data(file)
        return self._parse_data(raw_data)

    @abstractmethod
    def _open_file(self, path: str, params: Dict[str, str]) -> 'file':
        pass

    @abstractmethod
    def _extract_data(self, file):
        pass

    @abstractmethod
    def _parse_data(self, raw_data) -> []:
        pass
