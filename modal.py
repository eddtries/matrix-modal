from person import Person, PersonalData
from world import World

if __name__ == '__main__':
    personal_data = PersonalData("Neo", 37)
    neo = Person(bio="You are the protagonist.", personal_data=personal_data)

    personal_data = PersonalData("Morpheus", 50)
    morpheus = Person(
        bio="Morpheus is a Zion operative who serves in the city's defense force against attack from the Machines.", personal_data=personal_data)

    world = World("The world is bleak, ran by machines...", [neo, morpheus])
