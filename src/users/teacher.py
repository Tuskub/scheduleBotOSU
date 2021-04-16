from dataclasses import dataclass
import requests

from src.users.user import User


@dataclass()
class Teacher(User):
    full_name: str = ''
    cathedra: str = ''

    def get_schedule(self) -> str:
        pass
