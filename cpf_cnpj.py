from validate_docbr import CPF, CNPJ

class Documento:

    @staticmethod
    def cria_documento(documento):
        if len(documento) == 14:
            return DocCNPJ(documento)
        elif len(documento) == 11:
            return DocCpf(documento)
        else:
            raise ValueError("Documento inválido")

class DocCNPJ:
    def __init__(self, documento):        
        documento = str(documento)
        if self.cnpj_e_valido(documento):
                self.cnpj = documento
        else:
            raise ValueError("CNPJ inválido")

    def fatia_cnpj(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)

    def __str__(self):
        return f'Seu documento é: {self.fatia_cnpj()}'
        
    def cnpj_e_valido(self, cnpj):
        validador = CNPJ()
        return validador.validate(cnpj)


class DocCpf:
    def __init__(self,documento):
        if self.cpf_e_valido(documento):
            self.cpf = documento
        else:
            raise ValueError("CPF inválido")

    def __str__(self):
        return f'Seu documento é: {self.fatia_cpf()}'

    def cpf_e_valido(self,cpf):
        validador = CPF()
        return validador.validate(cpf)

    def fatia_cpf(self):
        mascara = CPF()
        return mascara.mask(self.cpf)