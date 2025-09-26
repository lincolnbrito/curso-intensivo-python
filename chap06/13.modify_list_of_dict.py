aliens = []

for alien_number in range(30):
    new_alien = {"color": "green", "points": 5, "speed": "slow"}
    aliens.append(new_alien)

# modify the 3 first aliens
for alien in aliens[:3]:
    if alien["color"] == "green":
        alien["color"] = "yellow"
        alien["points"] = 10
        alien["speed"] = "fast"

# show the first 5 aliens
for alien in aliens[:5]:
    print(alien)