"""8.8 – Álbuns dos usuários: Comece com o seu programa do Exercício 8.7.
Escreva um laço while que permita aos usuários fornecer o nome de um artista e
o título de um álbum. Depois que tiver essas informações, chame make_album()
com as entradas do usuário e apresente o dicionário criado. Lembre-se de incluir
um valor de saída no laço while"""

def make_album(album_title, artist_name, number_tracks=0):
    album = {"title": album_title, "artist": artist_name}
    if number_tracks > 0:
        album["tracks"] = number_tracks

    return album

print("Album information.\n Type 'q' to quit")
while True:
    album_title = input("\nAlbum title: ")
    if album_title == "q":
        break

    artist_name = input("Artist name: ")
    if artist_name == "q":
        break

    number_tracks = input("Number of tracks: ")
    if number_tracks == "q":
        break

    number_tracks = int(number_tracks)    
    
    album = make_album(album_title, artist_name, number_tracks)

    print(album)



