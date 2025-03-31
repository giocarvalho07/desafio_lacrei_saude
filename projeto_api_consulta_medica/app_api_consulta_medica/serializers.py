from rest_framework import serializers
from .models import ProfissionalSaude, Consulta

class ProfissionalSaudeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfissionalSaude
        fields = '__all__'

class ConsultaSerializer(serializers.ModelSerializer):
    profissional_nome = serializers.CharField(source="profissional.nome_completo", read_only=True)

    class Meta:
        model = Consulta
        fields = '__all__'