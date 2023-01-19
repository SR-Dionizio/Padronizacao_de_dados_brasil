from datetime import datetime, timedelta

class DatasBR:

    def __init__(self):
        self.momento_cadastro = datetime.today()

    def __str__(self):
        return self.format_data()

    def mes_cadastro(self):
        meses_ano = [
            "Janeiro", "Fevereiro", "Março", "Abril", 
            "maio", "Junho", "Julho", "Agosto", "Setembro",
            "Outubro", "Novembro", "Dezembro"
        ]
        mes_cadastro = self.momento_cadastro.month -1
        return meses_ano[mes_cadastro]

    def dia_semana(self):
        dias_semana = [
            "Segunda", "Terça", "Quarta", "Quinta", "Sexta"
            "Sábado", "Domingo"
        ]
        dia_cadastro = self.momento_cadastro.weekday()
        return dias_semana[dia_cadastro]

    def format_data(self):
        data_formatada = self.momento_cadastro.strftime("%d/%m/%Y %H:%M")
        return data_formatada