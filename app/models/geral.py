
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
        Usuario = {
                "nome": self.nome,
                "data": self.nascimento,
                "cpf": self.pc,
                "genero": self.gene,
                "endereco": self.end,
                "telefone": self.contato

            }
        from config import dados
        dados.append(Usuario)
        return True

    
        