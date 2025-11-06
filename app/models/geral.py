from app import mysql

#classe para cadastro do idoso
class Cadastro:
    def __init__(self, no, da, cp,ge, en, te): # , se
        self.nome = no
        self.nascimento = da #Isso seria a Data de nascimento
        self.pc = cp # pc seria o CPF
        self.gene = ge #isso seria o  genero
        self.end = en #isso seria o endereço
        self.contato = te # Telefone
        # self.sei = se # Senha (terá que ser removido por questões de segurança)
    
    def adicionar(self):
        """
        Insere os dados do IDOSO no banco MySQL.
        Caso alterem o nome da tabela ou as colunas,
        atualizar aqui no comando INSERT INTO.
        """
        cur = mysql.connection.cursor()
        sql = """
            INSERT INTO cadastro_idoso (nome, data_nascimento, cpf, genero, endereco, telefone)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        valores = (self.nome, self.nascimento, self.cpf, self.genero, self.endereco, self.telefone)
        cur.execute(sql, valores)
        mysql.connection.commit()
        cur.close()
        return True

# classe para cadastro de cuidadores
class Cuidador:
    def __init__(self, nome, data, email, genero, endereco, telefone, formacao):
        self.nome = nome
        self.nascimento = data
        self.email = email
        self.genero = genero
        self.endereco = endereco
        self.telefone = telefone
        self.formacao = formacao

    def adicionar(self):
        """
        Insere os dados do CUIDADOR no banco MySQL.
        Caso alterem o nome da tabela ou as colunas,
        atualizar aqui no comando INSERT INTO.
        """
        cur = mysql.connection.cursor()
        sql = """
            INSERT INTO cadastro_cuidador (nome, data_nascimento, email, genero, endereco, telefone, formacao)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        valores = (self.nome, self.nascimento, self.cpf, self.genero, self.endereco, self.telefone)
        cur.execute(sql, valores)
        mysql.connection.commit()
        cur.close()
        return True

#classe para o login
class Login:
    def __init__(self, cpf, senha, tipo):
        self.cpf = cpf
        self.senha = senha  # A senha deve ser armazenada já criptografada
        
    def adicionar(self):
        """
        Insere um novo login no banco MySQL.
        Os devs de banco devem confirmar o nome da tabela (login)
        e as colunas (cpf, senha, tipo).
        """
        cur = mysql.connection.cursor()
        sql = """
            INSERT INTO login (cpf, senha)
            VALUES (%s, %s)
        """
        valores = (self.cpf, self.senha, self.tipo)
        cur.execute(sql, valores)
        mysql.connection.commit()
        cur.close()
        return True

        
