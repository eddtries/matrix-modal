from dataclasses import dataclass


@dataclass
class PersonalData:
    name: str
    age: int


class Person:
    def __init__(self, bio, personal_data: PersonalData) -> None:
        self._bio = bio
        self._personal_data = personal_data


if __name__ == '__main__':
    personal_data = PersonalData("Neo", 37)
    neo = Person(bio="You are the protagonist.", personal_data=personal_data)
