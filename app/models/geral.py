from app import mysql

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
        """Insere um novo cadastro no banco de dados"""
        try:
            cur = mysql.connection.cursor()
            #insere um novo cadastro na tabela 'cadastro'
            sql = """
                INSERT INTO cadastro (nome, data_nascimento, cpf, genero, endereco, telefone)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            cur.execute(sql, (self.nome, self.nascimento, self.cpf, self.genero, self.endereco, self.telefone))
            mysql.connection.commit()
            cur.close()
            return True
        except Exception as e:
            print(f"Erro ao adicionar cadastro: {e}")
            return False
    
        
