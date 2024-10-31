# models/ia_data.py

import mongoengine as me

class IAData(me.Document):
    tipo_ruido = me.StringField(required=True)  # Tipo de ruído
    data_identificacao = me.DateField(required=True)  # Data em que foi identificado
    horario_identificacao = me.DateTimeField(required=True)  # Horário em que foi identificado
    tempo_resposta = me.FloatField(required=True)  # Tempo de resposta para identificar o ruído

    meta = {
        'collection': 'ia_data'  # Nome da coleção no MongoDB
    }
