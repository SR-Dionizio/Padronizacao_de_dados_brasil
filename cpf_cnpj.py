from validate_docbr import CPF, CNPJ

class CpfCnpj:
    def __init__(self,documento, tipo_documento):
        self.tipo_documento = tipo_documento
        documento = str(documento)

        if tipo_documento == "cpf":
            if self.cpf_e_valido(documento):
                self.cpf = documento
            else:
                raise ValueError("CPF inválido")
        elif tipo_documento == "cnpj":
            if self.cnpj_e_valido(documento):
                self.cnpj = documento
            else:
                raise ValueError("CNPJ inválido")
        else:
            raise ValueError("Documento inválido")

    def __str__(self):
        if self.tipo_documento == "cpf":
            return self.fatia_cpf()
        elif self.tipo_documento == "cnpj":
            return self.fatia_cnpj()

    def cpf_e_valido(self,cpf):
        if len(cpf) == 11:
            validador = CPF()
            return validador.validate(cpf)
        else:
            raise ValueError("Quantidade de digitos errada")

    def fatia_cpf(self):
        mascara = CPF()
        return mascara.mask(self.cpf)

    def fatia_cnpj(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)

    def cnpj_e_valido(self, cnpj):
        if len(cnpj) == 14:
            validador = CNPJ()
            return validador.validate(cnpj)
        else:
            raise ValueError("Quantidade de digitos errada")