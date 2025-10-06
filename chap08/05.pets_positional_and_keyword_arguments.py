def describe_pet(pet_name, animal_type="hamster"):
    """show information about a pet"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title())

# equivalent functions
describe_pet(pet_name="crypto", animal_type="dog")
describe_pet(animal_type="dog", pet_name="crypto")
describe_pet("crypto", "dog")
describe_pet("crypto")