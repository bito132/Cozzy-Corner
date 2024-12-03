import mysql.connector

def open_connection(host, user, password, database):
    return mysql.connector.connect(host=host, user=user, password=password, database=database)

def close_connection(connection):
    connection.close()

#Método genérico para inserir dados em uma tabela
def insert_into(connection, table: str, *fields : str):
    cursor = connection.cursor()

    campos = '(' + fields[0]
    qtde_campos = len(fields)
    for i in range(1, qtde_campos):
        campo = fields[i]
        if(campo.__class__ == str):
            campos += f", '{fields[i]}'"
        else:
            campos += f", {fields[i]}"

    campos += ')'

    sql = f'INSERT INTO {table} VALUES {campos}'

    cursor.execute(sql)
    connection.commit()
    cursor.close()

#Método para pegar todos os dados do usuário
def select_user(connection, email: str, senha:str):
    cursor = connection.cursor(dictionary=True)

    sql = f"SELECT * FROM usuarios WHERE email = '{email}' AND senha = '{senha}'"
    resposta = None

    cursor.execute(sql)
    for result in cursor:
        resposta = result
    cursor.close()

    return resposta