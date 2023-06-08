import mysql.connector
import persistencia.persistencia as persistencia


class PersistenciaContas():
    #Usado apenas pela função de excluir registro
    def conectar_bd():
        persistencia.Persistencia.conectar_bd()
    # Função para buscar as contas cadastradas no banco de dados
    def buscar_contas():
        cnx = persistencia.Persistencia.conectar_bd()
        cursor = cnx.cursor()

        query = "SELECT * FROM contas"
        cursor.execute(query)

        contas = []
        for nome, valor in cursor.fetchall():
            contas.append(f'Descrição | Valor')
            contas.append(f'{nome} | R${valor}')

        cursor.close()
        cnx.close()

        return contas

    # Função para inserir uma conta no banco de dados
    def inserir_conta(nome, valor):
        cnx = persistencia.Persistencia.conectar_bd()
        cursor = cnx.cursor()

        query = "INSERT INTO contas (nome, valor) VALUES (%s, %s)"
        values = (nome, valor)
        cursor.execute(query, values)

        cnx.commit()
        cursor.close()
        cnx.close()

    # Função para buscar as contas cadastradas no banco de dados
    def buscar_contas_Tabela():
        cnx = persistencia.Persistencia.conectar_bd()
        cursor = cnx.cursor()

        query = "SELECT nome, valor FROM contas"

        cursor.execute(query)

        contas = cursor.fetchall()

        cursor.close()
        cnx.close()

        return contas
    
    def getLastCodigo():
        cnx = persistencia.Persistencia.conectar_bd()
        cursor = cnx.cursor()

        query = "SELECT salcodigo FROM tbsaldo ORDER BY salcodigo DESC LIMIT 1"

        cursor.execute(query)
        
        iCodigo =  cursor.fetchall()
            # iCodigo = salcodigo

        cursor.close()
        cnx.close()   

        return iCodigo
