from chalice import Chalice, Response
from funcao_sql import busca_cliente_bd, insere_cliente_bd,\
    busca_clientes_bd, modifica_cliente, deleta_cliente


app = Chalice(app_name='projeto_crud')


@app.route('/cliente', methods=['POST'])
def cadastra_cliente():
    request_dados: dict = {}
    request_dados = app.current_request.json_body
    insere_cliente_bd(request_dados)
    return Response(
        body={"message": "cliente inserido com sucesso"},
        status_code=201
    )


@app.route('/cliente', methods=['GET'])
def retorna_cliente():
    request_codigo: dict = {}
    request_codigo = app.current_request.query_params['codigo']
    resposta_body = busca_cliente_bd(parametro_query=request_codigo)
    return Response(
        body=resposta_body,
        status_code=200
    )


@app.route('/clientes', methods=['GET'])
def retorna_clientes():
    resposta_body = busca_clientes_bd()
    return Response(
        body=resposta_body,
        status_code=200
    )


@app.route('/cliente', methods=['PATCH'])
def atualiza_cliente():
    requisicao_dados: dict = {}
    codigo_cliente: str = app.current_request.query_params['codigo']
    requisicao_dados["codigo"] = codigo_cliente
    requisicao_dados["dados"] = app.current_request.json_body
    modifica_cliente(corpo_requisicao=requisicao_dados)
    resposta_body = busca_cliente_bd(parametro_query=codigo_cliente)
    return Response(
        body=resposta_body,
        status_code=200
    )


@app.route('/cliente', methods=['DELETE'])
def remove_cliente():
    codigo_cliente: str = app.current_request.query_params['codigo']
    deleta_cliente(codigo_cliente=codigo_cliente)
    resposta_corpo_requisicao: dict = {"message": "Cliente deletado."}
    return Response(
        body=resposta_corpo_requisicao,
        status_code=200
    )
