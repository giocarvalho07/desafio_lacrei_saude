Arquitetura e Decisões de Implementação
Django foi escolhido para gerenciar as rotas e a lógica do servidor, aproveitando sua robustez e facilidade de implementação de APIs RESTful.

Django Rest Framework (DRF) foi utilizado para construir os endpoints da API de maneira eficiente e rápida, além de facilitar a serialização dos objetos do banco de dados para JSON.

O PostgreSQL foi escolhido como banco de dados pela sua robustez e escalabilidade.

Poetry foi utilizado para gerenciar as dependências, proporcionando um controle melhor sobre versões e garantindo que todas as dependências sejam instaladas corretamente.

Testes unitários com APITestCase foram escritos para garantir que os endpoints estão funcionando corretamente e que qualquer alteração no código não afete as funcionalidades existentes.


<br>
<br>
------------------------------------
<br>
<br>


Rodando o Servidor
Com o ambiente configurado e as migrações realizadas, execute o servidor local para rodar a API:

bash
Copiar
Editar
python manage.py runserver
A API estará disponível em http://127.0.0.1:8000/


<br>
<br>
------------------------------------
<br>
<br>


Testando a API
Endpoints:

Cadastrar Profissional de Saúde: POST /profissionais/criar/

Editar Profissional de Saúde: PUT /profissionais/editar/<id>/

Deletar Profissional de Saúde: DELETE /profissionais/deletar/<id>/

Cadastrar Consulta: POST /consultas/criar/

Editar Consulta: PUT /consultas/editar/<id>/

Deletar Consulta: DELETE /consultas/deletar/<id>/

Buscar Consultas por Profissional: GET /consultas/profissional/<id_profissional>/



<br>
<br>
------------------------------------
<br>
<br>



Como Executar os Testes Unitários, utilize o comando abaixo:

bash
Copiar
Editar
python manage.py test
Ou se estiver utilizando o Poetry, execute o comando dentro do ambiente do Poetry:

bash
Copiar
Editar
poetry run pytest
