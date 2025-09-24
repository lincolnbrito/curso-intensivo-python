favorite_languages = {
    "sarah": "c",
    "jen": "python",
    "edward": "ruby",
    "phil": "php",
}

friends = ["phil", "sarah"]

for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        print("Hi " + name.title() + ", I see your favorite langage is " + favorite_languages[name].title())


if 'jonh' not in favorite_languages.keys():
    print("\nJohn, please take our poll!")