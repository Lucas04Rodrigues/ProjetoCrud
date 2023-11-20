import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='150618',
    database='academiaturmab',
)

cursor = conexao.cursor()

#INSERIR

nome = input("Digite o Nome: ")
telefone = input("Telefone:  ")
end = input("Endereço: ")
cpf = input("CPF: ")
email = input("Email: ")

comando = f'INSERT INTO alunos (nome, telefone, end, cpf,  email) VALUES ("{nome}", {telefone})'

cursor.execute(comando)
conexao.commit() #editar banco de dados


#CONSULTAR

comando = f'SELECT*FROM alunos'
cursor.execute(comando)
resultado = cursor.fetchall() #ler o banco de dados
print(resultado)

#DELETAR
matricula = "1717"
comando = f'DELETE FROM alunos WHERE matricula = "{nome}"'
cursor.execute(comando)
conexao.commit() #editar banco de dados


#ATUALIZAR

nome = "lucas"
comando = f'UPDATE alunos SET nome = "{nome}"  WHERE nome = "{nome}"'
cursor.execute(comando)
conexao.commit() #editar banco de dados

cursor.close()
conexao.close()