def build_person(first_name, last_name, age=""):
    """Returns a dict with a person information"""
    person = {"first": first_name, "last": last_name}
    if age:
        person["age"] = age
    return person

musician = build_person("jimi", "hendrix", age=27)
print(musician)

musician = build_person("janis", "joplin")
print(musician)