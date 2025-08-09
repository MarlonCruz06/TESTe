# README do Projeto Igreja Gestor

Este projeto é um sistema de gerenciamento para igrejas, permitindo a administração de membros, eventos, finanças e inscrições, além de fornecer um dashboard com informações relevantes.

## Estrutura do Projeto

O projeto é organizado em módulos, cada um responsável por uma funcionalidade específica:

- **usuarios**: Gerenciamento de usuários e autenticação.
- **membros**: Cadastro e gerenciamento de membros da igreja.
- **igrejas**: Cadastro e gerenciamento de informações sobre igrejas.
- **eventos**: Gerenciamento de eventos, incluindo criação, edição e inscrições.
- **financeiro**: Controle financeiro, incluindo entradas e saídas.
- **inscricoes**: Gerenciamento de inscrições para eventos.
- **dashboard**: Resumo das informações e gráficos relevantes.

## Requisitos

- Python 3.x
- Django 3.x ou superior
- Banco de dados (SQLite, PostgreSQL, etc.)
- Bibliotecas adicionais (Chart.js ou Plotly para gráficos)

## Instalação

1. **Clone o repositório:**
   ```
   git clone <URL_DO_REPOSITORIO>
   cd igreja_gestor
   ```

2. **Crie um ambiente virtual:**
   ```
   python -m venv venv
   ```

3. **Ative o ambiente virtual:**
   - No Windows:
     ```
     venv\Scripts\activate
     ```
   - No Linux/Mac:
     ```
     source venv/bin/activate
     ```

4. **Instale as dependências:**
   ```
   pip install -r requirements.txt
   ```

5. **Configure o banco de dados:**
   Edite o arquivo `settings.py` para configurar as informações do banco de dados.

6. **Realize as migrações:**
   ```
   python manage.py migrate
   ```

7. **Crie um superusuário para acessar o painel administrativo:**
   ```
   python manage.py createsuperuser
   ```

8. **Inicie o servidor:**
   ```
   python manage.py runserver
   ```

## Acesso

Após iniciar o servidor, você pode acessar o sistema através do navegador em `http://127.0.0.1:8000/`.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

## Licença

Este projeto está licenciado sob a MIT License - veja o arquivo [LICENSE](LICENSE) para mais detalhes.