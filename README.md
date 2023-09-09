# API de Gerenciamento de Tarefas com Flask

Esta é uma API simples desenvolvida em **Flask** para gerenciar um cadastro de tarefas. A API permite listar todas as tarefas, incluir novas tarefas, consultar tarefas por ID, alterar o status de uma tarefa e excluir tarefas.

## 🔧 Ferramentas

- Python:
- Flask (Framework Web):
- JSON (Formato de dados):

## ⚙️ Como Funciona

- Listar todas as tarefas
- Incluir novas tarefas
- Consultar tarefas por ID
- Alterar o status de uma tarefa
- Excluir tarefas

## 🚀 Endpoints

- `GET /lisad/`: Retorna a lista de todas as tarefas cadastradas.
- `POST /lisad/`: Cria uma nova tarefa com os campos: id, responsável, tarefa e status.
- `GET /lisad/{id}/`: Consulta uma tarefa específica pelo ID.
- `PUT /lisad/{id}/`: Altera o status de uma tarefa específica pelo ID.
- `DELETE /lisad/{id}/`: Exclui uma tarefa específica pelo ID.

## 📜 Exemplos de Requisições

### Listar todas as tarefas

- GET /lisad/

### Incluir uma nova tarefa

- POST /lisad/

### Consultar uma tarefa por ID
- GET /lisad/1

### Alterar o status de uma tarefa por ID
- PUT /lisad/1

{
    "status": "Concluída"
}



{
    "responsável": "João",
    "tarefa": "Concluir relatório",
    "status": "Pendente"
}

### Excluir uma tarefa por ID
- DELETE /api/tasks/1


## 💻 Como Executar o Código

- Clone o repositório para sua máquina local.
- Instale as dependências usando o comando pip install -r requirements.txt.
- Execute o aplicativo com o comando python app.py.
- Acesse a API em http://localhost:5000.

## 🤝 Contribuindo

Contribuições são bem-vindas! Se você deseja contribuir para este projeto, por favor, siga estas etapas:

- Fork do projeto.
- Crie uma branch para sua contribuição (git checkout -b feature/sua-contribuicao).
- Faça suas alterações e commit (git commit -m 'Adiciona nova funcionalidade').
- Faça push para a branch (git push origin feature/sua-contribuicao).
- Abra um Pull Request explicando suas alterações.