
def conectar():
    import psycopg
    conn = psycopg.connect(
        dbname="SEU-BANCO-AQUI",
        host="localhost",
        user="postgres",
        password="SUA-SENHA-AQUI",
    )
    return conn

def clientes():
    conn = conectar()
    cur = conn.cursor()

    cur.execute("SELECT * FROM cliente")
    tabela = cur.fetchall()
    cur.close()
    conn.close()
    return tabela

def funcao_filto(idade, date1, date2):
    conn = conectar()
    cur = conn.cursor()

    cur.execute("SELECT c.nome_cliente, c.idade FROM cliente c inner join viagem v on c.id_cliente = v.id_cliente where c.idade >= %s and v.data_viagem between %s and %s",(idade,date1,date2))
    tabela = cur.fetchall()
    cur.close()
    conn.close()
    return tabela

