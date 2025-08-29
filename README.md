Sistema acadêmico em Python para gerenciamento de cursos, módulos, usuários e emissão de certificados. Inclui autenticação com permissões diferenciadas (usuário x administrador), registro de logs e interface interativa em terminal.

Principais Funcionalidades:

🔐 Autenticação de usuários com cadastro, login, logout e persistência de dados em JSON.

👨‍🏫 Níveis de acesso (Admin / Usuário) com menus e permissões diferenciadas.

🎓 Gerenciamento de cursos e módulos, restritos a administradores.

📜 Emissão de certificados simulados para usuários.

🛡 Camada de segurança com logs de atividades (login, logout, erros).

🎨 Interface em terminal com personalização de cores (ANSI escape codes).

Tecnologias / Conhecimentos aplicados:

Python (estrutura modular com pacotes e imports organizados).

Arquitetura em camadas: separação por módulos (usuarios, cursos, modulos, certificados, security).

Persistência de dados em JSON (armazenamento de usuários, cursos e logs).

Controle de acesso (ACL) diferenciando admins e usuários.

Tratamento de erros e logging.

Boas práticas de clean code (funções organizadas, código legível).
