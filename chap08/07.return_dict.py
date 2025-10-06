def build_person(first_name, last_name):
    """Returns a dict with person information"""
    person = {"first": first_name, "last": last_name}
    return person

musician = build_person("jimi", "hendrix")

print(musician)