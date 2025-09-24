favorite_languages = {
    "sarah": "c",
    "jen": "python",
    "edward": "ruby",
    "phil": "php",
}

for name in favorite_languages.keys():
    print(name.title())

# equivalent
for name in favorite_languages:
    print(name.title())
    