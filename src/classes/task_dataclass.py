from dataclasses import dataclass


@dataclass
class Task:
    id: str
    payload: str
