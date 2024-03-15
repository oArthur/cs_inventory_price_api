from database.conexao import conexao


def get_list_ignorados():
    cursor = conexao.cursor()

    cursor.execute('SELECT nome FROM itens_ignorados')

    itens = cursor.fetchall()
    ignorados = []
    for item in itens:
        ignorados.append(item[0])
    conexao.close()

    return ignorados


def add_ignorado(nome):
    cursor = conexao.cursor()
    cursor.execute('INSERT INTO itens_ignorados (nome) VALUES (?)', (nome,))
    conexao.commit()
    conexao.close()