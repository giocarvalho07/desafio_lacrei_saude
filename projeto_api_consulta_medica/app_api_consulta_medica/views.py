from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import ProfissionalSaude, Consulta
from .serializers import ProfissionalSaudeSerializer, ConsultaSerializer

# 🔹 Criar profissional
class CriarProfissionalSaude(generics.CreateAPIView):
    queryset = ProfissionalSaude.objects.all()
    serializer_class = ProfissionalSaudeSerializer

# 🔹 Editar profissional
class EditarProfissionalSaude(generics.UpdateAPIView):
    queryset = ProfissionalSaude.objects.all()
    serializer_class = ProfissionalSaudeSerializer

# 🔹 Deletar profissional
class DeletarProfissionalSaude(generics.DestroyAPIView):
    queryset = ProfissionalSaude.objects.all()
    serializer_class = ProfissionalSaudeSerializer

# 🔹 Criar consulta
class CriarConsulta(generics.CreateAPIView):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer

# 🔹 Editar consulta
class EditarConsulta(generics.UpdateAPIView):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer

# 🔹 Deletar consulta
class DeletarConsulta(generics.DestroyAPIView):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer

# 🔹 Buscar Consultas por ID do Profissional
class ConsultaPorProfissional(APIView):
    def get(self, request, profissional_id):
        consultas = Consulta.objects.filter(profissional_id=profissional_id)
        serializer = ConsultaSerializer(consultas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
