import sqlite3


def init():
    con = sqlite3.connect("./data/db_news.db")
    cur = con.cursor()
    return con,cur

def insert_new(item):
    con , cur = init()
    sql = f"""
    INSERT INTO news(id_new,rol_user,nombre,edad,sector,coordenadas,titulo,noticia,is_fake) 
     VALUES (NULL,'ROL_USUARIO','{item['nombre']}',{item['edad']},
     '{item['sector']}','{item['coordenadas']}','{item['titulo']}','{item['noticia']}',{item['etiqueta']})
    """
    cur.execute(sql)
    con.commit()
    con.close()
    pass

def delete_new():
    
    pass

def find_all_news():
    con , cur = init()
    sql = f"""
    SELECT * FROM news
    """
    cur.execute(sql)
    lista = cur.fetchall()
    print("lista :: " , lista)
    print(" typo lista :: " , type(lista))
    con.close()
    return lista

def find_new(id):
    con , cur = init()
    sql = f"""
    SELECT * FROM news where id_new = ?
    """
    cur.execute(sql,[id])
    noticia = cur.fetchone()
    con.close()
    return noticia 

def update_new():
    pass
