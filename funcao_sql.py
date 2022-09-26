from executa_bd import insere_bd, busca_bd


def insere_cliente_bd(corpo_requisicao: dict) -> None:
    nome: str = corpo_requisicao['nome'].upper()
    cpf: str = corpo_requisicao['cpf']
    if corpo_requisicao['email']:
        email = corpo_requisicao['email']
    else:
        email = None
    datanas: str = corpo_requisicao['datanas']
    telefone: str = corpo_requisicao['telefone']
    insere_sql = f"""INSERT INTO CLIENTES (NOME, CPF, EMAIL, DATANAS, TELEFONE)
                    VALUES ('{nome}', '{cpf}', '{email}', '{datanas}', '{telefone}');"""
    insere_bd(insere_sql=insere_sql)


def busca_cliente_bd(parametro_query: str) -> dict:
    retorno_cliente_bd: dict = {'dados_cliente': []}
    codigo_cliente = parametro_query
    print(codigo_cliente)
    busca_sql = f"""SELECT CODIGO, NOME, CPF, EMAIL, DATANAS
                    FROM CLIENTES
                    WHERE CODIGO = {codigo_cliente};"""
    dados_retorno_bd: list[tuple] = busca_bd(insere_sql=busca_sql)
    for dados in dados_retorno_bd:
        codigo: int = dados[0]
        nome: str = dados[1]
        cpf: str = dados[2]
        email: str = dados[3]
        datanas = dados[4].strftime('%d.%m.%Y')
        dados_cliente = {"codigo": codigo, "nome": nome, "cpf": cpf, "email": email, "datanas": datanas}
        retorno_cliente_bd['dados_cliente'].append(dados_cliente)
    return retorno_cliente_bd


def busca_clientes_bd() -> dict:
    retorno_cliente_bd: dict = {'quantidade_clientes': [], 'dados_clientes': []}
    busca_sqls = """SELECT CODIGO, NOME, CPF, EMAIL, DATANAS
                    FROM CLIENTES"""
    dados_retorno_bd: list[tuple] = busca_bd(insere_sql=busca_sqls)
    retorno_cliente_bd['quantidade_clientes'].append(len(dados_retorno_bd))
    for dados in dados_retorno_bd:
        codigo: int = dados[0]
        nome: str = dados[1]
        cpf: str = dados[2]
        email: str = dados[3]
        datanas = dados[4].strftime('%d.%m.%Y')
        dados_clientes = {"codigo": codigo, "nome": nome, "cpf": cpf, "email": email, "datanas": datanas}
        retorno_cliente_bd['dados_clientes'].append(dados_clientes)
    return retorno_cliente_bd


def modifica_cliente(corpo_requisicao: dict) -> None:
    chave_novo_dado = None
    novo_dado = None
    novo_update: str = ''
    codigo_cliente = corpo_requisicao["codigo"]
    atualiza_cliente: str = f"""UPDATE CLIENTES
                                SET /*CHAVE = VALOR*/
                                WHERE CODIGO = {codigo_cliente}"""
    for chave in corpo_requisicao['dados'].keys():
        chave_novo_dado = chave.upper()
        novo_dado = corpo_requisicao["dados"][chave]
        if type(novo_dado) == str:
            novo_dado = novo_dado.upper()
            novo_update = f"{chave_novo_dado} = '{novo_dado}', /*CHAVE = VALOR*/"
        else:
            novo_update = f"{chave_novo_dado} = {novo_dado}, /*CHAVE = VALOR*/"
        atualiza_cliente = atualiza_cliente.replace("/*CHAVE = VALOR*/", novo_update)
    atualiza_cliente = atualiza_cliente.replace(", /*CHAVE = VALOR*/", "")
    insere_bd(insere_sql=atualiza_cliente)


def deleta_cliente(codigo_cliente: str) -> None:
    remove_cliente_bd: str = f"""DELETE FROM CLIENTES
                                WHERE CODIGO = {codigo_cliente}"""
    insere_bd(insere_sql=remove_cliente_bd)
