class PlanoTelefone:
    def __init__(self, nome, saldo):
        self.__nome = nome
        self.__saldo = saldo

    def get_saldo(self):
        return self.__saldo

    def set_saldo(self, saldo):
        self.__saldo = saldo

    def verificar_saldo(self):
        return self.__saldo

    def mensagem_personalizada(self):
        saldo = self.verificar_saldo()
        if saldo < 10:
            return "Seu saldo está baixo. Recarregue e use os serviços do seu plano."
        elif saldo >= 50:
            return "Parabéns! Continue aproveitando seu plano sem preocupações."
        else:
            return "Seu saldo está razoável. Aproveite o uso moderado do seu plano."


class UsuarioTelefone:
    def __init__(self, nome, plano):
        self.nome = nome
        self.plano = plano

    def verificar_saldo(self):
        return self.plano.verificar_saldo()

    def mensagem_personalizada(self):
        return self.plano.mensagem_personalizada()


# Recebendo as entradas do usuário (nome, plano, saldo):
nome_usuario = input("Digite o nome do usuário: ")
nome_plano = input("Digite o nome do plano (Essencial, Prata, Premium): ")
saldo_inicial = float(input("Digite o saldo inicial: "))

# Criação de objetos do plano de telefone e usuário de telefone com dados fornecidos:
plano_usuario = PlanoTelefone(nome_plano, saldo_inicial)
usuario = UsuarioTelefone(nome_usuario, plano_usuario)

# Chamada do método para verificar_saldo sem acessar diretamente os atributos do plano:
mensagem = usuario.mensagem_personalizada()
print(mensagem)

class UsuarioTelefone:
    def __init__(self, nome, numero, plano):
        self.__nome = nome
        self.__numero = numero
        self.__plano = plano

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_numero(self):
        return self.__numero

    def set_numero(self, numero):
        self.__numero = numero

    def fazer_chamada(self, destinatario, duracao):
        custo = self.__plano.custo_chamada(duracao)
        if custo <= self.__plano.verificar_saldo():
            self.__plano.deduzir_saldo(custo)
            return f"Chamada para {destinatario} realizada com sucesso. Saldo: ${self.__plano.verificar_saldo():.2f}"
        else:
            return "Saldo insuficiente para fazer a chamada."

class Plano:
    def __init__(self, saldo_inicial):
        self.__saldo = saldo_inicial

    def verificar_saldo(self):
        return self.__saldo

    def custo_chamada(self, duracao):
        return duracao * 0.10

    def deduzir_saldo(self, valor):
        self.__saldo -= valor

# Classe UsuarioPrePago
class UsuarioPrePago(UsuarioTelefone):
    def __init__(self, nome, numero, saldo_inicial):
        super().__init__(nome, numero, Plano(saldo_inicial))

# Recebendo as informações do usuário:
nome = input()
numero = input()
saldo_inicial = float(input())

# Criando o objeto de UsuarioPrePago com os dados fornecidos:
usuario_pre_pago = UsuarioPrePago(nome, numero, saldo_inicial)
destinatario = input()
duracao = int(input())

# Chamando o método fazer_chamada do objeto usuario_pre_pago e imprimindo o resultado:
print(usuario_pre_pago.fazer_chamada(destinatario, duracao))
