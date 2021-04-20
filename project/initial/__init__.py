from datetime import date

from initial.repositories.book import BookRepository
from initial.repositories.error_codes import ErrorCodes
from initial.utils import generate_id

book_repository = BookRepository()

def get_value(string: str, warn: str = "Valor Inválido",validation_func = lambda v: v):
    try:
        result = validation_func(input(string).strip())
        if not result:
            raise ValueError
    except ValueError:
        print(warn)
        result = get_value(string, warn, validation_func)
    return result

def get_integer(string: str, warn: str, validation_func):
    return get_value(string, warn, lambda v: validation_func(int(v)))

def create_book():

    today = date.today()
    name = get_value("Digite o nome do livro: ")
    has_id = get_value("O livro possui identificador? (S/n)", validation_func= lambda v: v if v in ["S", "n"] else False) == "S"
    if has_id:
        id_ = get_value("Digite o identificador do livro: ")
    else:
        id_ = generate_id()
    author = get_value("Digite o nome do autor: ")
    year = get_integer(
        "Digite o ano do livro: ",
        "Ano Inválido",
        lambda result: result if 0 < result <= today.year else False,
    )
    publisher = get_value("Digite a publicadora do livro: ")

    book_dict = {
        "name": name,
        "_id": id_,
        "author": author,
        "year": year,
        "publisher": publisher,
    }

    status = book_repository.create_book(book_dict)
    if status == ErrorCodes.successful:
        print("Livro Criado com Sucesso")
    elif status == ErrorCodes.already_exists:
        print("Livro já existe")
    elif status == ErrorCodes.unexpected_error:
        print("Erro inexperado")
    else:
        raise NotImplementedError

def run():
    create_book()
