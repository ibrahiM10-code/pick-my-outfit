import sqlite3, random

class BaseDatos:
    def __init__(self):
        self.conn = sqlite3.connect(database="my_database.db")
        self.cursor = self.conn.cursor()

    # Metodo para devolver todos los outfits.
    def lista_outfits(self) -> list:
        resultados = self.cursor.execute("SELECT o.nombre_outfit, r.nombre_ropa, c.outfit_id FROM Outfit o JOIN Outfit_Ropa c ON (o.outfit_id = c.outfit_id) JOIN Ropa r ON (r.ropa_id = c.ropa_id)")
        outfits = resultados.fetchall()
        return outfits

    # Metodo para devolver todos los outfits de acuerdo a criterios de busqueda.
    def elige_outfit(self, clima: str, ocasion: str) -> list:
        # Primero, buscamos los outfits que cumplan con los criterios.
        filtro_outfits = self.cursor.execute(f"SELECT * FROM Outfit WHERE ocasion_outfit = '{ocasion}' AND clima_outfit = '{clima}'")
        outfits_encontrados = filtro_outfits.fetchall()

        # Segundo, elegimos uno al azar. (guardar el id del outfit que salga)
        outfit_random = random.choice(outfits_encontrados)
        outfit_id = (outfit_random[0],)

        # Tercero, hacemos la consulta JOIN para conseguir la ropa que conforma el outfit. (filtramos la consulta con el id del outfit que salio)
        consulta_ropa = self.cursor.execute("SELECT r.nombre_ropa FROM Outfit_Ropa c LEFT OUTER JOIN Ropa r ON (c.ropa_id = r.ropa_id) WHERE c.outfit_id = ?", outfit_id)
        outfit_elegido = consulta_ropa.fetchall()
        outfit_final = [outfit[0] for outfit in outfit_elegido]
        return outfit_final

    # Metodo para devolver todas las categorias.
    def categorias_ropa(self) -> list:
        resultados = self.cursor.execute("SELECT * FROM Categoria")
        categorias = [categoria for (id_categoria, categoria) in resultados.fetchall()]
        return categorias

    # Metodo para devolver la ropa de acuerdo a la categoria.
    def filtro_ropa(self, categoria: int) -> list:
        resultados = self.cursor.execute("SELECT nombre_ropa FROM Ropa WHERE id_categoria = ?", (categoria,))
        ropa_filtrada = resultados.fetchall()
        lista_ropa = [ropa[0] for ropa in ropa_filtrada]
        return lista_ropa
    
    # Metodo para insertar nueva ropa.
    def agregar_ropa(self, nombre: str, categoria: int):
        datos_ropa = (nombre, categoria)
        self.cursor.execute("INSERT INTO Ropa (nombre_ropa, id_categoria) VALUES (? ,?)", datos_ropa)
        self.conn.commit()

    # Metodo para insertar nuevos outfits.
    def agregar_outfit(self, nombre: str, clima: str, ocasion: str):
        datos_outfit = (nombre, clima, ocasion)
        self.cursor.execute("INSERT INTO Outfit (nombre_outfit, clima_outfit, ocasion_outfit) VALUES (?, ?, ?)", datos_outfit)
        self.conn.commit()

    # Metodo para insertar en la tabla Outfit_Ropa.
    def agregar_conjunto(self, id_outfit: int, id_ropa: int):
        datos_conjunto = (id_outfit, id_ropa, )
        self.cursor.execute("INSERT INTO Outfit_Ropa VALUES (?, ?)", datos_conjunto)
        self.conn.commit()

    # Metodo para retornar los id's de las categorias:
    def numero_categoria(self, categoria: str) -> int:
        if categoria == "POLERAS":
            return 1
        elif categoria == "PANTALONES":
            return 2
        elif categoria == "POLERONES":
            return 3
        elif categoria == "CAMISAS":
            return 4
        elif categoria == "PARKAS":
            return 5

    # Metodo que retorna el id del ultimo outfit agregado.
    def ultimo_outfit(self): 
        res = self.cursor.execute("SELECT outfit_id FROM Outfit ORDER BY outfit_id DESC")
        outfit_id = res.fetchall()[0][0]
        return outfit_id

    # Metodo que retorna los id de las ropas elegidas para el outfit.
    def ropas_id(self, lista_ropas: list) -> list:
        query = "SELECT ropa_id FROM Ropa WHERE "
        where_clause = " OR ".join(["nombre_ropa = ?"] * len(lista_ropas))
        query += where_clause
        res = self.cursor.execute(query, lista_ropas)
        lista_ids = [ids[0] for ids in res.fetchall()]
        return lista_ids
    
    # Metodo que retorna el outfit de acuerdo al nombre especificado.
    def filtro_outfit(self, nombre_outfit: str) -> list:
        res = self.cursor.execute("SELECT o.nombre_outfit, r.nombre_ropa FROM Outfit o JOIN Outfit_Ropa c ON (o.outfit_id = c.outfit_id) JOIN Ropa r ON (r.ropa_id = c.ropa_id) WHERE o.nombre_outfit = ?", (nombre_outfit,))
        resultados = res.fetchall()
        lista_conjunto = [ropa[1] for ropa in resultados]
        return lista_conjunto
        
