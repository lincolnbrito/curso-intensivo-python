def describe_pet(animal_type="hamster", pet_name="hamtaro"):
    """show information about a pet"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title())

# the order of keyword arguments does not matter, because Python knows waht each value is.
describe_pet(pet_name="crypto", animal_type="dog")
describe_pet(animal_type="dog", pet_name="crypto")