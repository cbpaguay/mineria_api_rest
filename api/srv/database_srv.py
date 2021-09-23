import sqlite3
import os
import datetime

directorio = os.path.dirname(__file__).replace("srv", "data")


def init():
    con = sqlite3.connect(directorio + "/db_news.db")
    cur = con.cursor()
    return con, cur


def insert_new(item):
    con, cur = init()
    nombre = item['nombre'].upper().strip()
    edad = item['edad']
    sector = item['sector'].upper().strip()
    coordenadas = item['coordenadas'].upper().strip()
    titulo = item['titulo'].upper().strip()
    noticia = item['noticia'].upper().strip()
    etiqueta = item['etiqueta']
    fecha = datetime.date.today().strftime("%d-%m-%Y")
    sql = f"""
    INSERT INTO news(id_new,rol_user,nombre,edad,sector,coordenadas,titulo,noticia,is_fake,fecha) 
     VALUES (NULL,'ROL_USUARIO','{nombre}',{edad},'{sector}','{coordenadas}','{titulo}','{noticia}',{etiqueta},'{fecha}')
    """
    cur.execute(sql)
    con.commit()
    con.close()
    pass


def delete_new():
    pass


def find_all_news():
    con, cur = init()
    sql = f"""
    SELECT * FROM news
    """
    cur.execute(sql)
    lista = cur.fetchall()
    con.close()
    return lista


def find_new(id):
    con, cur = init()
    sql = f"""
    SELECT * FROM news where id_new = ?
    """
    cur.execute(sql, [id])
    noticia = cur.fetchone()
    con.close()
    return noticia


def update_new():
    pass

def find_news_reals():
    con, cur = init()
    sql = f"""
    SELECT * FROM news where is_fake = 0
    """
    cur.execute(sql)
    lista = cur.fetchall()
    con.close()
    return lista

def find_news_fakes():
    con, cur = init()
    sql = f"""
    SELECT * FROM news where is_fake = 1
    """
    cur.execute(sql)
    lista = cur.fetchall()
    con.close()
    return lista