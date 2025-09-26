favorite_languages = {
    "sarah": "c",
    "jen": "python",
    "edward": "ruby",
    "phil": "php",
}

people_to_vote = [
    "sarah", "luke", "obi", "han", "jen"
]

for person in people_to_vote:
    if person in favorite_languages:
        print("Hi, " + person + " thanks for voting!")
    else:
        print(person + ", would do you like to vote on your favorite language?")