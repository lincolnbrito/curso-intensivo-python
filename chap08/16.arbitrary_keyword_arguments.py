def build_profile(first, last, **user_info):
    """Build a dictionary with all we know about the user"""
    profile = {}
    profile["first_name"] = first
    profile["last_name"] = last
    profile + user_info
    print(type(user_info))
    for key,value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile("Alber", "Einstein", location="Princeton", field="Physics")

print(user_profile)