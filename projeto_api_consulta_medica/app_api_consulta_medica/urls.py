from django.urls import path
from .views import (
    CriarProfissionalSaude,
    EditarProfissionalSaude,
    DeletarProfissionalSaude,
    CriarConsulta,
    EditarConsulta,
    DeletarConsulta,
    ConsultaPorProfissional
)

urlpatterns = [
    # 🔹 Endpoints Profissionais de Saúde
    path('profissionais/criar/', CriarProfissionalSaude.as_view(), name='criar-profissional'),
    path('profissionais/editar/<int:pk>/', EditarProfissionalSaude.as_view(), name='editar-profissional'),
    path('profissionais/deletar/<int:pk>/', DeletarProfissionalSaude.as_view(), name='deletar-profissional'),

    # 🔹 Endpoints Consultas
    path('consultas/criar/', CriarConsulta.as_view(), name='criar-consulta'),
    path('consultas/editar/<int:pk>/', EditarConsulta.as_view(), name='editar-consulta'),
    path('consultas/deletar/<int:pk>/', DeletarConsulta.as_view(), name='deletar-consulta'),

    # 🔹 Buscar Consultas por ID do Profissional
    path('consultas/profissional/<int:profissional_id>/', ConsultaPorProfissional.as_view(), name='consulta-por-profissional'),
]
