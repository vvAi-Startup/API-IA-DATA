# models/ia_data.py
import mongoengine as me
from datetime import datetime

class IAData(me.Document):
    """Modelo de dados para registro de identificação de ruídos de IA."""
    
    tipo_ruido = me.StringField(required=True, help_text="Tipo de ruído (ex: 'ruído branco').")
    data_identificacao = me.DateField(required=True, help_text="Data em que o ruído foi identificado.")
    horario_identificacao = me.DateTimeField(required=True, help_text="Horário em que o ruído foi identificado.")
    tempo_resposta = me.FloatField(required=True, help_text="Tempo de resposta em segundos para identificar o ruído.")

    def clean(self):
        if self.data_identificacao > datetime.today().date():
            raise me.ValidationError('A data de identificação não pode ser no futuro.')

    meta = {
        'collection': 'ia_data',
        'indexes': [
            'tipo_ruido',
            'data_identificacao'
        ]
    }