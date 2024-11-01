# models/ia_data.py
import mongoengine as me
from datetime import datetime, timezone

class IAData(me.Document):
    """Modelo de dados para registro de identificação de ruídos de IA."""
    
    tipo_ruido = me.StringField(required=True, help_text="Tipo de ruído (ex: 'ruído branco').")
    data_identificacao = me.DateField(default=lambda: datetime.now(timezone.utc).date(), help_text="Data em que o ruído foi identificado.")
    horario_identificacao = me.DateTimeField(default=lambda: datetime.now(timezone.utc), help_text="Horário em que o ruído foi identificado.")
    tempo_resposta = me.FloatField(required=True, help_text="Tempo de resposta em segundos para identificar o ruído.")

    meta = {
        'collection': 'ia_data',
    }