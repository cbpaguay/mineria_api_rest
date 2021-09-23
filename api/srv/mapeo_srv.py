from api.entity.noticia_dto import Noticia

noticia = Noticia()


def mapeo_one(item):
    noticia.id = item[0]
    noticia.rol_user = item[1]
    noticia.nombre = item[2]
    noticia.edad = item[3]
    noticia.sector = item[4]
    noticia.coordenadas = item[5]
    noticia.titulo = item[6]
    noticia.noticia = item[7]
    noticia.is_fake = item[8]
    noticia.fecha = item[9]
    return noticia.serialize()


def mapeo_all(items):
    lista = list()
    for item in items:
        noticia.id = item[0]
        noticia.rol_user = item[1]
        noticia.nombre = item[2]
        noticia.edad = item[3]
        noticia.sector = item[4]
        noticia.coordenadas = item[5]
        noticia.titulo = item[6]
        noticia.noticia = item[7]
        noticia.is_fake = item[8]
        noticia.fecha = item[9]
        lista.append(noticia.serialize())
    return lista
