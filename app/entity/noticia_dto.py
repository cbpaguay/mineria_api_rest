class Noticia:

    def __init__(self):
        self.id = None
        self.rol_user = None
        self.nombre = None
        self.edad = None
        self.sector = None
        self.coordenadas = None
        self.titulo = None
        self.noticia = None
        self.is_fake = None

    def serialize(self):
        return {
            "id": self.id,
            "rol_user": self.rol_user,
            "nombre": self.nombre,
            "edad": self.edad,
            "sector": self.sector,
            "coordenadas": self.coordenadas,
            "titulo": self.titulo,
            "noticia": self.noticia,
            "is_fake": self.is_fake

        }
