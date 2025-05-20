class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        self.name = name

        if pet_type in Pet.PET_TYPES:
            self.pet_type = pet_type
        else:
            raise Exception("Invalid pet type.")

        if owner is not None and not isinstance(owner, Owner):
            raise Exception("Owner must be an instance of Owner.")
        self._owner = owner

        Pet.all.append(self)

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, owner):
        if not isinstance(owner, Owner):
            raise Exception("Owner must be an instance of Owner.")
        self._owner = owner


class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("Argument must be a Pet instance.")
        pet.owner = self

    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)
