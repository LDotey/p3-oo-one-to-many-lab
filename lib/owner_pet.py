class Pet:
    all = []
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    def __init__(self, name, pet_type, owner = ""):
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"{pet_type} must be in PET_TYPES")
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)
    pass

class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
    
    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception()
        pet.owner = self

    # def get_sorted_pets(self):
    #     pets_list = self.pets()
    #     sorted_pets = sorted(pets_list, key=lambda pet: pet.name)
    #     return sorted_pets
    # def get_pet_name(pet):
    #     return pet.name

    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)