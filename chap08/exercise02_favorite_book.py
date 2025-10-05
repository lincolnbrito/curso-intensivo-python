"""8.2 – Livro favorito: Escreva uma função chamada favorite_book() que aceite
um parâmetro title. A função deve exibir uma mensagem como Um dos meus
livros favoritos é Alice no país das maravilhas. Chame a função e não se
esqueça de incluir o título do livro como argumento na chamada da função."""

def favorite_book(title):
    print("One of my favorite books is " + title.title())

favorite_book("1984")
favorite_book("The Lord Of The Rings")
favorite_book("The Hobbit")
