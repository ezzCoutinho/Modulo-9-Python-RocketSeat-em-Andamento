## 03/04

Hoje implementamos a autenticação JWT (JSON Web Token) no projeto. Utilizamos a biblioteca PyJWT para gerar tokens de autenticação e criamos uma rota específica para que os usuários possam obter seus tokens. Além disso, avançamos com a implementação da conexão com o banco de dados SQLite, onde definimos e criamos a tabela de usuários (users) para armazenar informações como nome de usuário, senha e saldo.


## 07/04
Hoje realizamos testes de integração e unitários, incluindo a criação de usuários e a edição de saldo. Também implementamos a funcionalidade de busca de usuários pelo nome de usuário (get_user_by_username). Desativamos uma função do RUFF que removia automaticamente imports não utilizados. Além disso, instalamos a biblioteca bcrypt para criptografar senhas, criamos um gerenciador para ela, desenvolvemos uma interface para o user_repository e, por fim, implementamos os controllers responsáveis pela lógica de criação de usuários no banco de dados.