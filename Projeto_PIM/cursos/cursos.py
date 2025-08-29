import json
import os
from datetime import datetime
from usuarios.usuarios import usuario_logado, eh_admin, registrar_log, usuarios_cadastrados, salvar_usuarios

# ========== CONFIGURAÇÕES ==========
ARQUIVO_CURSOS = "cursos.json"
COR_SUCESSO = "\033[1;32m"
COR_ERRO = "\033[1;31m"
COR_TITULO = "\033[1;36m"
RESET_COR = "\033[0m"
COR_ALERTA = "\033[1;33m"  # Amarelo

# ========== BANCO DE DADOS ==========
def carregar_cursos() -> dict:
    """Carrega cursos do JSON ou cria estrutura inicial"""
    if os.path.exists(ARQUIVO_CURSOS):
        with open(ARQUIVO_CURSOS, 'r') as f:
            return json.load(f)
    
    return {
        "1": {
            "nome": "Introdução à Programação",
            "carga_horaria": "40h",
            "modulos": [],
            "criado_por": "Sistema",
            "data_criacao": datetime.now().isoformat()
        }
    }

def salvar_cursos():
    """Salva os cursos no arquivo JSON"""
    with open(ARQUIVO_CURSOS, 'w') as f:
        json.dump(cursos_disponiveis, f, indent=4, ensure_ascii=False)

# Dados globais
cursos_disponiveis = carregar_cursos()

# ========== OPERAÇÕES PRINCIPAIS ==========
def tela_cursos():
    """Menu principal de cursos"""
    while True:
        print(f"\n{COR_TITULO}=== GERENCIAMENTO DE CURSOS ===")
        print("1. 📋 Listar cursos")
        print("2. ➕ Criar novo curso (ADM)")
        print("3. ✏️ Editar curso (ADM)")
        print("4. 🗑️ Deletar curso (ADM)")  # Nova opção
        print("0. ↩ Voltar")
        print("="*40 + RESET_COR)
        
        escolha = input("Escolha: ")

        if escolha == '1':
            listar_cursos(completo=True)
        elif escolha == '2':
            if eh_admin():
                criar_curso()
            else:
                print(f"{COR_ERRO}⚠️ Apenas ADMs podem criar cursos!{RESET_COR}")
        elif escolha == '3':
            if eh_admin():
                editar_curso()
            else:
                print(f"{COR_ERRO}⚠️ Acesso restrito!{RESET_COR}")
        elif escolha == '4':  # Nova opção
            if eh_admin():
                deletar_curso()
            else:
                print(f"{COR_ERRO}⚠️ Acesso restrito!{RESET_COR}")
        elif escolha == '0':
            break
        else:
            print(f"{COR_ERRO}❌ Opção inválida!{RESET_COR}")


def matricular_aluno():
    """Permite ao usuário se matricular em cursos disponíveis"""
    if not usuario_logado:
        print(f"{COR_ERRO}⚠️ Faça login primeiro!{RESET_COR}")
        return

    print(f"\n{COR_TITULO}=== MATRÍCULA EM CURSOS ===")
    listar_cursos(completo=True)
    
    id_curso = input("\nID do curso para matrícula: ").strip()
    if id_curso not in cursos_disponiveis:
        print(f"{COR_ERRO}❌ Curso não encontrado!{RESET_COR}")
        return

    # Adiciona aos cursos do usuário
    usuario = usuario_logado['nome']
    if id_curso not in usuarios_cadastrados[usuario]['cursos']:
        usuarios_cadastrados[usuario]['cursos'].append(id_curso)
        salvar_usuarios()
        registrar_log("Matrícula realizada", f"Usuário: {usuario} | Curso: {id_curso}")
        print(f"\n{COR_SUCESSO}✅ Matrícula realizada com sucesso!{RESET_COR}")
    else:
        print(f"{COR_ALERTA}⚠️ Você já está matriculado neste curso!{RESET_COR}")
    
    input("Pressione Enter para voltar...")            

# ========== FUNÇÕES DE GERENCIAMENTO ==========
def criar_curso():
    """Cadastro de novos cursos (apenas ADM)"""
    print(f"\n{COR_TITULO}=== NOVO CURSO ===")
    
    # Gera ID automático
    novo_id = str(max(int(k) for k in cursos_disponiveis.keys()) + 1)
    
    nome = input("Nome do curso: ").strip()
    carga_horaria = input("Carga horária (ex: 40h): ").strip()
    
    if not nome or not carga_horaria:
        print(f"{COR_ERRO}❌ Preencha todos os campos!{RESET_COR}")
        return
    
    cursos_disponiveis[novo_id] = {
        "nome": nome,
        "carga_horaria": carga_horaria,
        "modulos": [],
        "criado_por": usuario_logado["nome"],  # Corrigido
        "data_criacao": datetime.now().isoformat()
    }
    
    salvar_cursos()
    registrar_log("Curso criado", f"ID: {novo_id} | Nome: {nome}")
    print(f"\n{COR_SUCESSO}✅ Curso criado com sucesso!{RESET_COR}")

def editar_curso():
    """Edição de cursos existentes (apenas ADM)"""
    print(f"\n{COR_TITULO}=== EDITAR CURSO ===")
    listar_cursos()
    
    id_curso = input("\nID do curso a editar: ").strip()
    
    if id_curso not in cursos_disponiveis:
        print(f"{COR_ERRO}❌ Curso não encontrado!{RESET_COR}")
        return
    
    print(f"\nEditando: {cursos_disponiveis[id_curso]['nome']}")
    print("Deixe em branco para manter o valor atual\n")
    
    novo_nome = input(f"Novo nome [{cursos_disponiveis[id_curso]['nome']}]: ").strip()
    nova_carga = input(f"Nova carga horária [{cursos_disponiveis[id_curso]['carga_horaria']}]: ").strip()
    
    if novo_nome:
        cursos_disponiveis[id_curso]["nome"] = novo_nome
    if nova_carga:
        cursos_disponiveis[id_curso]["carga_horaria"] = nova_carga
    
    cursos_disponiveis[id_curso]["ultima_edicao"] = {
        "por": usuario_logado["nome"],  # Corrigido
        "em": datetime.now().isoformat()
    }
    
    salvar_cursos()
    registrar_log("Curso editado", f"ID: {id_curso}")
    print(f"\n{COR_SUCESSO}✅ Curso atualizado!{RESET_COR}")

def deletar_curso():
    """Remove um curso existente (apenas ADM)"""
    print(f"\n{COR_TITULO}=== DELETAR CURSO ===")
    listar_cursos()
    
    id_curso = input("\nID do curso a deletar: ").strip()
    
    if id_curso not in cursos_disponiveis:
        print(f"{COR_ERRO}❌ Curso não encontrado!{RESET_COR}")
        return
    
    curso = cursos_disponiveis[id_curso]
    confirmacao = input(f"\nTem certeza que deseja deletar o curso '{curso['nome']}'? (S/N): ").upper()
    
    if confirmacao == 'S':
        del cursos_disponiveis[id_curso]
        salvar_cursos()
        registrar_log("Curso deletado", f"ID: {id_curso} | Nome: {curso['nome']}")
        print(f"\n{COR_SUCESSO}✅ Curso deletado com sucesso!{RESET_COR}")
    else:
        print(f"{COR_ALERTA}❌ Operação cancelada.{RESET_COR}")

# ========== FUNÇÕES AUXILIARES ==========
def listar_cursos(completo: bool = False):
    """Lista todos os cursos com detalhes"""
    print(f"\n{COR_TITULO}=== CURSOS DISPONÍVEIS ===")
    for id_curso, curso in cursos_disponiveis.items():
        print(f"\n{id_curso}. {curso['nome']} ({curso['carga_horaria']})")
        print(f"   Criado por: {curso['criado_por']}")
        print(f"   Data: {curso['data_criacao'][:10]}")
        
        if completo:
            if curso["modulos"]:
                print("   Módulos:")
                for mod in curso["modulos"]:
                    print(f"     - {mod['nome']} (por {mod['criado_por']})")
            else:
                print("   Nenhum módulo cadastrado")
    
    print("="*40 + RESET_COR)
    if completo:
        input("\nPressione Enter para continuar...")

def get_curso(id_curso: str) -> dict:
    """Retorna os dados de um curso específico"""
    return cursos_disponiveis.get(id_curso, {})