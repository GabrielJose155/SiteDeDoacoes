import psycopg2

def conectardb():

     con = psycopg2.connect(

         #host='localhost',
         #database='postgres',
         #user='postgres',
         #password='12345'

         host='dpg-cue2gbt2ng1s7381b27g-a.oregon-postgres.render.com',
         database='doarr',
         user='doarr_user',
         password='qFzL2xvxw57vvWkghOUACBN00VpJMrDJ'
     )
     return con


def login(email,senha):
    con= conectardb()
    cur = con.cursor()
    sql = f"SELECT * from usuarios where email='{email}' and senha='{senha}'"
    cur.execute(sql)
    saida = cur.fetchall()
    cur.close()
    con.close()
    return saida


def inserir_user(nome,telefone,email,senha):

    conn = conectardb()
    cur = conn.cursor()
    try:
        sql = f"INSERT INTO usuarios (nome, telefone, email, senha) VALUES ('{nome}','{telefone}','{email}','{senha}')"
        cur.execute(sql)

    except psycopg2.IntegrityError:
        #volta que deu ruim
        conn.rollback()
        exito = False
    else:
        conn.commit()
        exito = True

    cur.close()
    conn.close()

    return exito

def inserir_roupa(tipo, tamanho, estado, descricao, email):
    conn = conectardb()
    cur = conn.cursor()

    try:
        sql = f"INSERT INTO cadastroderoupas (tipo, tamanho, estado, descricao, email) VALUES ('{tipo}','{tamanho}','{estado}','{descricao}', '{email}')"
        cur.execute(sql)

    except psycopg2.IntegrityError:
        conn.rollback()
        exito = False
    else:
        conn.commit()
        exito = True

    cur.close()
    conn.close()

    return exito



def listar_roupas():
    con = conectardb()
    cur = con.cursor()
    sql = f"SELECT  tipo, tamanho, estado, descricao, email  from cadastroderoupas"
    cur.execute(sql)
    saida = cur.fetchall()

    cur.close()
    con.close()

    return saida