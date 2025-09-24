favorite_languages = {
    "sarah": "c",
    "jen": "python",
    "edward": "ruby",
    "phil": "python",
}

print("The following languages have been mentioned:")

for language in favorite_languages.values():
    print(language.title())
print("---")
for language in set(favorite_languages.values()):
    print(language.title())
