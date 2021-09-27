import os
import urllib.parse as up
import psycopg2
import datetime

directorio = os.path.dirname(__file__).replace("srv", "data")


# up.uses_netloc.append("postgres")
# url = up.urlparse(os.environ["DATABASE_URL"])


def init():
    url = up.urlparse("postgres://gyutvztx:lGKJECUp4FX7nFDWCanx13Mjm6zcO_hB@fanny.db.elephantsql.com/gyutvztx")
    con = psycopg2.connect(database=url.path[1:],
                           user=url.username,
                           password=url.password,
                           host=url.hostname,
                           port=url.port
                           )
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
    sql = """
    INSERT INTO news(rol_user,nombre,edad,sector,coordenadas,titulo,noticia,is_fake,fecha) 
     VALUES ('ROL_USUARIO',%s,%s,%s,%s,%s,%s,%s,%s)
    """
    cur.execute(sql, (nombre, edad, sector, coordenadas, titulo, noticia, etiqueta, fecha))
    con.commit()
    cur.close()
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
    cur.close()
    con.close()
    return lista


def find_new(id):
    con, cur = init()
    sql = """
    SELECT * FROM news where id_new = %s 
    """
    cur.execute(sql, (id,))
    noticia = cur.fetchone()
    cur.close()
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
    cur.close()
    con.close()
    return lista


def find_news_fakes():
    con, cur = init()
    sql = f"""
    SELECT * FROM news where is_fake = 1
    """
    cur.execute(sql)
    lista = cur.fetchall()
    cur.close()
    con.close()
    return lista
