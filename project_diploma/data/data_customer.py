import dataclasses


@dataclasses.dataclass
class Customer:
    name: str
    email: str
    password: str