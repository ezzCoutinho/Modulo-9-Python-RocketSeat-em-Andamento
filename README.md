## 03/04

Hoje implementamos a autenticação JWT (JSON Web Token) no projeto. Utilizamos a biblioteca PyJWT para gerar tokens de autenticação e criamos uma rota específica para que os usuários possam obter seus tokens. Além disso, avançamos com a implementação da conexão com o banco de dados SQLite, onde definimos e criamos a tabela de usuários (users) para armazenar informações como nome de usuário, senha e saldo.


## 07/04
Hoje realizamos testes de integração e unitários, incluindo a criação de usuários e a edição de saldo. Também implementamos a funcionalidade de busca de usuários pelo nome de usuário (get_user_by_username). Desativamos uma função do RUFF que removia automaticamente imports não utilizados. Além disso, instalamos a biblioteca bcrypt para criptografar senhas, criamos um gerenciador para ela, desenvolvemos uma interface para o user_repository e, por fim, implementamos os controllers responsáveis pela lógica de criação de usuários no banco de dados.


## 08/04
Hoje ajustamos os módulos de verificação e criação de senhas, adicionando o encode e decode em UTF-8 que estavam faltando. Criamos um controller para JWT, juntamente com seu teste unitário. Também adicionamos uma nova biblioteca, o python-dotenv, para preservar dados importantes em variáveis globais. Além disso, criamos uma pasta chamada `configs` para centralizar o carregamento das variáveis do dotenv diretamente nos arquivos. Por fim, implementamos o LoginCreatorController, responsável por realizar o login do cliente no banco de dados, garantindo verificações essenciais.


## 12/04

Hoje implementamos e executamos testes unitários para o sistema de login de usuários, verificando a autenticação correta das credenciais. Além disso, desenvolvemos o módulo de edição de saldo (balance editor), que permite atualizar o saldo dos usuários no banco de dados de forma segura e controlada.


## 14/04

Hoje implementamos as interfaces para todos os controllers do sistema (balance_editor, login_creator e user_register), padronizando a comunicação entre as camadas. Em seguida, focamos no desenvolvimento das views, criando os componentes http_types (response e request) para padronizar as requisições e respostas HTTP. Também desenvolvemos a interface base para as views e implementamos as views específicas: user_register_view, login_creator_view e balance_editor_view. Até o momento, apenas os testes unitários do user_register_view foram concluídos. Amanhã, daremos continuidade implementando os testes unitários para login_creator_view e balance_editor_view.


## 15/04

Hoje, criamos os compositores para balance_editor, login_creator e user_register. Em seguida, desenvolvemos a nossa aplicação principal, que contém o arquivo server.py, onde utilizamos o blueprint do Flask. Criamos uma rota chamada bank_account_routes, que permite o registro de usuários, criptografando as senhas antes de armazená-las no banco de dados. Também implementamos a funcionalidade de login, que gera um token. Para a atualização do saldo (new_balance), planejamos adicionar uma proteção amanhã, de modo que apenas usuários com um token de login válido possam realizar essa atualização no banco de dados.


## 16/04

Hoje, implementamos um middleware para a edição do saldo, que permite que apenas o usuário correspondente ao user_id possa modificar o new_balance de sua própria conta."