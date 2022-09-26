import psycopg2


def cria_conexao():
    print('conectando...')
    conexao = psycopg2.connect(
        host='localhost',
        port=5432,
        user='postgres',
        database='crud_',
        password=12345,
    )
    print('conectado')
    return conexao


def insere_bd(insere_sql: str) -> None:
    conecta_bd = cria_conexao()
    cursor = conecta_bd.cursor()
    cursor.execute(insere_sql)
    conecta_bd.commit()
    cursor.close()
    conecta_bd.close()


def busca_bd(insere_sql: str) -> list[tuple]:
    conecta_bd = cria_conexao()
    cursor = conecta_bd.cursor()
    cursor.execute(insere_sql)
    retorno_bd = cursor.fetchall()
    conecta_bd.commit()
    cursor.close()
    conecta_bd.close()
    return retorno_bd
