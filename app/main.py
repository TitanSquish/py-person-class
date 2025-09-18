class Person:
    # Class attribute to store all created Person instances
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        # Add instance to the class-level dictionary
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    result = []
    name_to_person = {}

    # First pass: create Person objects
    for person_dict in people:
        person = Person(person_dict["name"], person_dict["age"])
        result.append(person)
        name_to_person[person.name] = person

    # Second pass: set wife/husband relationships
    for person_dict in people:
        person = name_to_person[person_dict["name"]]

        if "wife" in person_dict and person_dict["wife"]:
            person.wife = name_to_person[person_dict["wife"]]

        if "husband" in person_dict and person_dict["husband"]:
            person.husband = name_to_person[person_dict["husband"]]

    return result
