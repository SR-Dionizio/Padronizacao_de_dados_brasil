class Cpf:
    def __init__(self,documento):
        documento = str(documento)
        if self.cpf_e_valido(documento):
            self.cpf = documento
        else:
            raise ValueError("CPF inválido")

    def __str__(self):
        return self.fatia_cpf()

    def cpf_e_valido(self,documento):
        if len(documento) == 11:
            return True
        else:
            return False

    def fatia_cpf(self):
        parte_1 = self.cpf[:3]
        parte_2 = self.cpf[3:6]
        parte_3 = self.cpf[6:9]
        parte_4 = self.cpf[9:]

        return f'{parte_1}.{parte_2}.{parte_3}-{parte_4}'