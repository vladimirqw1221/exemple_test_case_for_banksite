from dataclasses import dataclass


@dataclass
class Person:
    first_name: str = None
    zip_code: str = None
    email: str = None
