import mysql.connector
import bcrypt

import bcrypt

def gerar_hash(senha: str) -> str:
    return bcrypt.hashpw(senha.encode(), bcrypt.gensalt()).decode()


def verificar_hash(senha_digitada: str, hash_salvo: str) -> bool:
    return bcrypt.checkpw(senha_digitada.encode(), hash_salvo.encode())








    

    # ----- verificação real -----
    return bcrypt.checkpw(transformador_s.encode(), transformador_e.encode())



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
    def adicionar(self, n,i,dia,mes,ano,cf,g,ed,ce,te,e, senha):
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
        # t_str = str(gerador(senha))
        # preciso puxar o token antes de enviar pro cursor.execute

        
        self.cursor.execute(f""" insert into USUARIO(nome, idade, data_de_nascimento, cpf, genero, endereco, cep, telefone, email, token)
                             values ('{nome}', {idade}, '{ano}-{mes}-{dia}', '{cpf}', '{genero}', '{endereco}', '{cep}', '{telefone}', '{email}', '{gerar_hash(senha)}')
                             """)
        self.atualizar()
        self.fechar()
        self.desconectar()
        return "dados enviados" 
    
    def verificar(self, email, senha_digitada):
    # Buscar hash do banco
        self.cursor.execute(f"SELECT token FROM USUARIO WHERE email = '{email}'")
        resultado = self.cursor.fetchall()
        

    

    # pegar hash salvo
        hash_salvo = resultado[0]['token']   # [(hash,)] → hash

    # verificar a senha
        if verificar_hash(senha_digitada, hash_salvo):
            return True
        else:
            return False
