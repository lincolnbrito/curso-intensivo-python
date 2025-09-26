aliens = []

for alien_number in range(30):
    new_alien = {"color": "green", "points": 5, "speed": "slow"}
    aliens.append(new_alien)

# show the first 5 aliens
for alien in aliens[:5]:
    print(alien)

print("Total number of aliens: " + str(len(aliens)))    