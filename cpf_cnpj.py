from validate_docbr import CPF, CNPJ

class CpfCnpj:
    def __init__(self,documento):
        documento = str(documento)
        if self.cpf_e_valido(documento):
            self.cpf = documento
        else:
            raise ValueError("CPF inválido")

    def __str__(self):
        return self.fatia_cpf()

    def cpf_e_valido(self,cpf):
        if len(cpf) == 11:
            validador = CPF()
            return validador.validate(cpf)
        else:
            raise ValueError("Quantidade de digitos errada")

    def fatia_cpf(self):
        mascara = CPF()
        return mascara.mask(self.cpf)

    def valida_cnpj(self, cnpj):
        if len(cnpj) == 14:
            validador = CNPJ
            return validador.validate(cnpj)
        else:
            raise ValueError("CNPJ inválido")