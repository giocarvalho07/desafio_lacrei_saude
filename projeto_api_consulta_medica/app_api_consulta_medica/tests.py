from rest_framework.test import APITestCase
from rest_framework import status
from .models import ProfissionalSaude

class ProfissionalSaudeTestCase(APITestCase):
    def test_criar_profissional(self):
        url = '/profissionais/criar/'
        data = {
            "nome_completo": "Dr. João Silva",
            "nome_social": "Dr. João",
            "profissao": "Médico",
            "endereco": "Rua das Flores, 123",
            "contato": "(11) 99999-9999"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ProfissionalSaude.objects.count(), 1)
        self.assertEqual(ProfissionalSaude.objects.get().nome_completo, "Dr. João Silva")
