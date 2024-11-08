# models/ia_data.py
import mongoengine as me
from datetime import datetime, timezone

class IAData(me.Document):
    """Modelo de dados para registro de identificação de ruídos de IA."""
    
    tipo_ruido = me.StringField(required=True)
    data_identificacao = me.DateField(default=lambda: datetime.now(timezone.utc).date())
    horario_identificacao = me.DateTimeField(default=lambda: datetime.now(timezone.utc))
    tempo_resposta = me.FloatField(required=True)
    nome_audio = me.StringField(required=True)

    def as_dict(self):
        return {
                "tipo_ruido": self.tipo_ruido,
                "data_identificacao": self.data_identificacao,
                "horario_identificacao": self.horario_identificacao,
                "tempo_resposta": self.tempo_resposta,
                "nome_audio": self.nome_audio,
            }
    
    meta = {
        'collection': 'ia_data',
    }