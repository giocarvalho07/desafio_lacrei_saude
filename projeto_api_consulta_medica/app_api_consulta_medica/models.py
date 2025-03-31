import uuid
from django.db import models

class ProfissionalSaude(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome_completo = models.CharField(max_length=255)
    nome_social = models.CharField(max_length=255, blank=True, null=True)
    profissao = models.CharField(max_length=100)
    endereco = models.TextField()
    contato = models.CharField(max_length=50)

    def __str__(self):
        return self.nome_completo

class Consulta(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    data_consulta = models.DateTimeField()
    profissional = models.ForeignKey(
        ProfissionalSaude, on_delete=models.CASCADE, related_name="consultas"
    )

    def __str__(self):
        return f"Consulta com {self.profissional.nome_completo} em {self.data_consulta}"
