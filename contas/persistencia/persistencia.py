import mysql.connector

class Persistencia():
    def conectar_bd():
        return mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='myframedb'
        )