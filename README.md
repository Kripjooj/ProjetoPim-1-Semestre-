🎓 PIM – Sistema Acadêmico em Python

Sistema acadêmico desenvolvido em Python como projeto integrador da faculdade.
Permite gerenciamento de cursos, módulos, usuários e emissão de certificados, com autenticação diferenciada para administradores e usuários.

🚀 Funcionalidades

🔐 Autenticação de usuários: cadastro, login, logout e persistência em JSON

👨‍🏫 Níveis de acesso: menus e permissões diferentes para Admin e Usuário

🎓 Gerenciamento de cursos e módulos (restrito a administradores)

📜 Emissão de certificados simulados para usuários

🛡 Registro de logs de atividades (login, logout, erros)

🎨 Interface no terminal com cores personalizadas (ANSI escape codes)

🛠 Tecnologias e Conceitos

Python 3 – Estrutura modular com pacotes

Arquitetura em camadas – separação por módulos (usuarios, cursos, modulos, certificados, security)

JSON – persistência de dados e logs

ACL (Access Control List) – diferenciação de permissões

Clean Code – código organizado, modular e legível

▶️ Como Executar

Clone o repositório:

git clone https://github.com/Kripjooj/ProjetoPim-1-Semestre-.git
cd ProjetoPim-1-Semestre-


Execute o programa:

python main.py

📌 Exemplo de Uso

Usuário comum:

Cadastra conta

Faz login

Consulta cursos e emite certificado

Administrador:

Faz login como admin

Cria cursos e módulos

Gera relatórios e acessa logs

🔮 Possíveis Melhorias

Migração do JSON para banco de dados relacional (SQLite/MySQL)

Implementação de interface Web (Flask/Django)

Envio automático de certificados por e-mail

Testes unitários automatizados

👨‍💻 Equipe

Projeto desenvolvido como trabalho acadêmico na disciplina de Projeto Integrador Multidisciplinar (PIM).

Davi C. Cerqueira
 – Desenvolvedor
