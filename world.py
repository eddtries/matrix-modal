from person import Person


class World:
    def __init__(self, world_description: str, people: [Person]) -> None:
        self._world_description = world_description
        self._people = people


if __name__ == '__main__':
    pass
