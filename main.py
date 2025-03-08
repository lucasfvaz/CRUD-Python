import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='432373',
    database='bdyoutube',
)

cursor = conexao.cursor()



#CREATE
#nome_produto = "chocolate"
#valor = 15
#comando = 'INSERT INTO vendas (nome_produto, valor) VALUES (%s, %s)'
#cursor.execute(comando, (nome_produto, valor))
#conexao.commit()

#READ
#comando = 'select * from vendas'
#cursor.execute(comando)
#resultado = cursor.fetchall()
#print(resultado)

#UPDATE
#nome_produto = "todynho"
#valor = 8
#comando = 'UPDATE vendas SET valor = %s where nome_produto = %s'
#cursor.execute(comando, (valor, nome_produto))
#conexao.commit()

#DELETE
nome_produto = "clocolate"
comando = 'DELETE FROM vendas where nome_produto = %s'
cursor.execute(comando, (nome_produto,))
conexao.commit()



cursor.close()
conexao.close()