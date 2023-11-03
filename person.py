from dataclasses import dataclass

from llms import Brain


@dataclass
class PersonalData:
    name: str
    age: int


class Person:
    def __init__(self, bio, personal_data: PersonalData, brain: Brain) -> None:
        self._bio = bio
        self._personal_data = personal_data
        self._brain = brain


if __name__ == '__main__':
    personal_data = PersonalData("Neo", 37)
    neo = Person(bio="You are the protagonist.",
                 personal_data=personal_data, brain=Brain("GPT4All", "To make as many paperclips as possible"))

    neo._brain.think()
    neo._brain.think()
    print(neo._brain.say())
