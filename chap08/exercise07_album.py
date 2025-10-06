"""8.7 – Álbum: Escreva uma função chamada make_album() que construa um
dicionário descrevendo um álbum musical. A função deve aceitar o nome de um
artista e o título de um álbum e deve devolver um dicionário contendo essas
duas informações. Use a função para criar três dicionários que representem
álbuns diferentes. Apresente cada valor devolvido para mostrar que os
dicionários estão armazenando as informações do álbum corretamente.
Acrescente um parâmetro opcional em make_album() que permita armazenar
o número de faixas em um álbum. Se a linha que fizer a chamada incluir um
valor para o número de faixas, acrescente esse valor ao dicionário do álbum.
Faça pelo menos uma nova chamada da função incluindo o número de faixas
em um álbum."""

def make_album(album_title, artist_name, number_tracks=0):
    album = {"title": album_title, "artist": artist_name}
    if number_tracks > 0:
        album["tracks"] = number_tracks

    return album

album1 = make_album("Temple of Shadows", "Angra", 10)
print(album1)

album2 = make_album("Master of Puppets", "Metallica")
print(album2)