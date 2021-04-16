from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass()
class User(ABC):
    schedule_url: str = ''

    @abstractmethod
    def get_schedule(self) -> str:
        pass
