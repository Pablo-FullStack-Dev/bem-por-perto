import mysql.connector

class My:
    def __init__(self):
        try:
            self.conexao = mysql.connector.connect(
                host = '127.0.0.1',
                user = 'maq_func_prt_fac',
                password = 's5jw_@yyx_xzul_caQ',
                database = 'bem_po_perto'
            )
            if self.conexao.is_connected():
                print("\nconexão bem sucedida\n")
        except ValueError:
            print("\nErro de conexão\n")
    def desconectar(self):
        self.conexao.close()
        return "\ndesconectado\n"
    def atualizar(self):
        self.conexao.commit()
        return "dados atualizados"
    
class Cursor(My):
    def __init__(self):
        super().__init__()
        self.cursor =self.conexao.cursor(dictionary=True)
        try:
            if self.cursor:
                print("\ncurso operante\n")
        except ValueError:
            print("\nErro de conexão\n")

    def fechar(self):
        self.cursor.close()
        self.desconectar()
        return "\ncursor inoperante\n"
    

class Comandos(Cursor):
    def adicionar(self, n,i,dia,mes,ano,cf,g,ed,ce,te,e):
        nome = str(n)
        idade = int(i)
        dia = int(dia)
        mes = int(mes)
        ano = int(ano)
        cpf = str(cf)
        genero = str(g)
        endereco = str(ed)
        cep = str(ce)
        telefone = str(te)
        email = str(e)

        
        self.cursor.execute(f""" insert into USUARIO(nome, idade, data_de_nascimento, cpf, genero, endereco, cep, telefone, email)
                             values ('{nome}', {idade}, '{ano}-{mes}-{dia}', '{cpf}', '{genero}', '{endereco}', '{cep}', '{telefone}', '{email}')
                             """)
        self.atualizar()
        self.fechar()
        self.desconectar()
        return "dados enviados"