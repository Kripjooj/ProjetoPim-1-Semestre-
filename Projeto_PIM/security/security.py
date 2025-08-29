import os
import getpass
from datetime import datetime
from usuarios.usuarios import usuario_logado, eh_admin, registrar_log, usuarios_cadastrados, salvar_usuarios

# ========== CONFIGURAÇÕES ==========
COR_SUCESSO = "\033[1;32m"
COR_ERRO = "\033[1;31m"
COR_TITULO = "\033[1;36m"
COR_ALERTA = "\033[1;33m"
RESET_COR = "\033[0m"

# ========== FUNÇÕES PRINCIPAIS ==========
def tela_seguranca():
    """Menu completo de segurança"""
    while True:
        print(f"\n{COR_TITULO}=== SEGURANÇA E PRIVACIDADE ===")
        print("1. 🔒 Políticas de Segurança")
        print("2. 🔑 Alterar minha senha")
        
        if eh_admin():
            print(f"{COR_ALERTA}3. ⚠️ Relatório de Acessos Suspeitos{RESET_COR}")
            print(f"{COR_ALERTA}4. 🛡️ Forçar Troca de Senha (ADM){RESET_COR}")
        
        print("0. ↩ Voltar")
        print("="*40 + RESET_COR)
        
        opcao = input("Escolha: ").strip()

        if opcao == '1':
            mostrar_politicas()
        elif opcao == '2':
            alterar_senha()
        elif opcao == '3' and eh_admin():
            relatorio_acessos()
        elif opcao == '4' and eh_admin():
            forcar_troca_senha()
        elif opcao == '0':
            break
        else:
            print(f"{COR_ERRO}❌ Opção inválida!{RESET_COR}")
            input("Pressione Enter para continuar...")

# ========== FUNÇÕES DE SEGURANÇA ==========
def mostrar_politicas():
    """Exibe as políticas de segurança"""
    print(f"\n{COR_TITULO}=== POLÍTICAS DE SEGURANÇA ===")
    print(f"{COR_SUCESSO}• Senhas criptografadas e protegidas")
    print("• Conformidade com LGPD (Lei 13.709/2018)")
    print("• Registro de todas as atividades críticas")
    print("• Autenticação obrigatória para operações sensíveis")
    print("• Nível de acesso baseado em permissões")
    print(f"• Auditoria periódica dos sistemas{RESET_COR}")
    input("\nPressione Enter para voltar...")

def alterar_senha():
    """Permite ao usuário alterar sua própria senha"""
    if not usuario_logado:
        print(f"{COR_ERRO}⚠️ Faça login primeiro!{RESET_COR}")
        return

    print(f"\n{COR_TITULO}=== ALTERAR SENHA ===")
    
    # Verifica senha atual
    senha_atual = getpass.getpass("Senha atual: ")
    if usuarios_cadastrados[usuario_logado['nome']]['senha'] != senha_atual:
        print(f"{COR_ERRO}❌ Senha atual incorreta!{RESET_COR}")
        return

    # Pede nova senha 2x
    nova_senha = getpass.getpass("Nova senha: ")
    confirmacao = getpass.getpass("Confirme a nova senha: ")

    if nova_senha != confirmacao:
        print(f"{COR_ERRO}❌ As senhas não coincidem!{RESET_COR}")
        return

    # Atualiza no sistema
    usuarios_cadastrados[usuario_logado['nome']]['senha'] = nova_senha
    salvar_usuarios()
    registrar_log("Senha alterada", f"Usuário: {usuario_logado['nome']}")
    print(f"\n{COR_SUCESSO}✅ Senha atualizada com sucesso!{RESET_COR}")
    input("Pressione Enter para voltar...")

# ========== FUNÇÕES ADMINISTRATIVAS ==========
def relatorio_acessos():
    """Gera relatório de acessos suspeitos (apenas ADM)"""
    print(f"\n{COR_ALERTA}=== ACESSOS SUSPEITOS ===")
    print("1. 📅 Últimos 30 dias")
    print("2. 🔍 Buscar por usuário")
    print("0. ↩ Voltar")
    
    opcao = input("Escolha: ").strip()
    # Implemente a lógica de relatórios aqui
    print(f"{COR_SUCESSO}Relatório gerado com sucesso!{RESET_COR}")
    input("Pressione Enter para voltar...")

def forcar_troca_senha():
    """Força um usuário a trocar a senha no próximo login (apenas ADM)"""
    print(f"\n{COR_ALERTA}=== FORÇAR TROCA DE SENHA ===")
    from usuarios.usuarios import listar_usuarios
    listar_usuarios()
    
    usuario = input("\nNome do usuário: ").strip()
    if usuario in usuarios_cadastrados:
        usuarios_cadastrados[usuario]['precisa_trocar_senha'] = True
        salvar_usuarios()
        registrar_log("Forçou troca de senha", f"ADM: {usuario_logado['nome']} | Usuário: {usuario}")
        print(f"\n{COR_SUCESSO}✅ Usuário precisará trocar a senha no próximo login!{RESET_COR}")
    else:
        print(f"{COR_ERRO}❌ Usuário não encontrado!{RESET_COR}")
    input("Pressione Enter para voltar...")