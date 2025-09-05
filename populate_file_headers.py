import os
from datetime import datetime

# Define a pasta raiz do projeto (deve ser a mesma do script bash)
PROJECT_ROOT = "MEx_NVIDIA_Inception_Project"

# Define o cabeçalho padrão para arquivos .md
HEADER_TEMPLATE = """---
Responsabilidade: {responsibility}
Autores (Time MEx): {authors}
Data da Última Atualização: {date}
Versão: {version}
Pasta de Localização: {location}
---

# {title}

"""

# Mapeamento de responsabilidades e autores por arquivo/pasta (adapte conforme necessário)
# Isso é um exemplo, você precisará preencher com as responsabilidades e autores reais
FILE_METADATA = {
    # Raiz
    "README.md": {
        "title": "Visão Geral do Projeto MEx-NVIDIA Inception",
        "responsibility": "Zeh Sobrinho (CEO), Maria Oliveira (Gerência de Projetos)",
        "authors": "Zeh Sobrinho, Maria Oliveira",
        "version": "1.0.0"
    },
    "tasks/ROADMAP.md": {
        "title": "Roadmap do Projeto MEx-NVIDIA Inception",
        "responsibility": "Maria Oliveira (Gerência de Projetos), Zeh Sobrinho (CEO)",
        "authors": "Maria Oliveira",
        "version": "1.0.0"
    },
    # docs/01_NVIDIA_Program_Info
    # Estes são arquivos externos, não precisam de cabeçalho interno
    # docs/02_MEx_Pitch_Deck
    "docs/02_MEx_Pitch_Deck/MEx_Edge_Swarm_DLT_White_Paper.pdf": {
        "title": "White Paper: MEx Edge Swarm DLT para NVIDIA Inception",
        "responsibility": "Zeh Sobrinho (CEO), Bruno Souza (CTO), Maria Oliveira (Gerência de Projetos)",
        "authors": "Zeh Sobrinho, Bruno Souza, Maria Oliveira",
        "version": "1.0.0"
    },
    # docs/03_Edge_Swarm_DLT_Tech_Docs
    "docs/03_Edge_Swarm_DLT_Tech_Docs/Edge_Swarm_DLT_Overview.md": {
        "title": "Visão Geral Técnica: Edge Swarm DLT",
        "responsibility": "Bruno Souza (CTO), João Almeida (Engenharia de Dados)",
        "authors": "Bruno Souza, João Almeida",
        "version": "1.0.0"
    },
    "docs/03_Edge_Swarm_DLT_Tech_Docs/Requirements.md": {
        "title": "Requisitos Técnicos do Edge Swarm DLT",
        "responsibility": "Bruno Souza (CTO), João Almeida (Engenharia de Dados)",
        "authors": "Bruno Souza, João Almeida",
        "version": "1.0.0"
    },
    "docs/03_Edge_Swarm_DLT_Tech_Docs/Outras_Docs_Tecnicas_do_Drex_Swarm.md": {
        "title": "Outras Documentações Técnicas do Drex Swarm",
        "responsibility": "Equipe de Engenharia",
        "authors": "Bruno Souza, João Almeida, Felipe Alves",
        "version": "1.0.0"
    },
    # docs/04_NVIDIA_Integration_Plan
    "docs/04_NVIDIA_Integration_Plan/Integration_Strategy.md": {
        "title": "Estratégia de Integração com NVIDIA",
        "responsibility": "Bruno Souza (CTO), Felipe Alves (Automação)",
        "authors": "Bruno Souza, Felipe Alves",
        "version": "1.0.0"
    },
    "docs/04_NVIDIA_Integration_Plan/GPU_Resource_Allocation_Plan.md": {
        "title": "Plano de Alocação de Recursos GPU",
        "responsibility": "Bruno Souza (CTO), João Almeida (Engenharia de Dados)",
        "authors": "Bruno Souza, João Almeida",
        "version": "1.0.0"
    },
    "docs/04_NVIDIA_Integration_Plan/Software_Stack_Compatibility.md": {
        "title": "Compatibilidade do Software Stack com NVIDIA",
        "responsibility": "Bruno Souza (CTO), Felipe Alves (Automação)",
        "authors": "Bruno Souza, Felipe Alves",
        "version": "1.0.0"
    },
    "docs/04_NVIDIA_Integration_Plan/Security_Considerations_NVIDIA.md": {
        "title": "Considerações de Segurança para Integração NVIDIA",
        "responsibility": "Júlio César (Segurança da Informação)",
        "authors": "Júlio César",
        "version": "1.0.0"
    },
    # docs/05_Meeting_Notes
    "docs/05_Meeting_Notes/2025-08-22_NVIDIA_Intro_Call.md": {
        "title": "Ata da Reunião Inicial NVIDIA (22/08/2025)",
        "responsibility": "Maria Oliveira (Gerência de Projetos), Zeh Sobrinho (CEO)",
        "authors": "Maria Oliveira",
        "version": "1.0.0"
    },
    "docs/05_Meeting_Notes/2025-09-XX_Inception_Kickoff.md": {
        "title": "Ata da Reunião de Kick-off NVIDIA Inception",
        "responsibility": "Maria Oliveira (Gerência de Projetos)",
        "authors": "Maria Oliveira",
        "version": "1.0.0"
    },
    # docs/06_Progress_Reports
    "docs/06_Progress_Reports/Q1_2026_Progress_Report.md": {
        "title": "Relatório de Progresso - Q1 2026",
        "responsibility": "Maria Oliveira (Gerência de Projetos)",
        "authors": "Maria Oliveira",
        "version": "1.0.0"
    },
    # docs/templates
    "docs/templates/Meeting_Minutes_Template.md": {
        "title": "Modelo de Ata de Reunião",
        "responsibility": "Maria Oliveira (Gerência de Projetos)",
        "authors": "Maria Oliveira",
        "version": "1.0.0"
    },
    "docs/templates/Progress_Report_Template.md": {
        "title": "Modelo de Relatório de Progresso",
        "responsibility": "Maria Oliveira (Gerência de Projetos)",
        "authors": "Maria Oliveira",
        "version": "1.0.0"
    },
}

def populate_header(filepath, metadata):
    """Insere o cabeçalho no início de um arquivo .md."""
    if not filepath.endswith(".md"):
        print(f"Ignorando arquivo não Markdown: {filepath}")
        return

    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    relative_path = os.path.relpath(filepath, PROJECT_ROOT)
    
    header_content = HEADER_TEMPLATE.format(
        responsibility=metadata.get("responsibility", "Não definida"),
        authors=metadata.get("authors", "Não definidos"),
        date=current_date,
        version=metadata.get("version", "0.0.1"),
        location=os.path.dirname(relative_path),
        title=metadata.get("title", os.path.basename(filepath).replace(".md", ""))
    )

    try:
        with open(filepath, 'r+') as f:
            content = f.read()
            # Verifica se o cabeçalho já existe para evitar duplicação
            if not content.strip().startswith("---"):
                f.seek(0, 0) # Volta ao início do arquivo
                f.write(header_content + content)
                print(f"Cabeçalho adicionado a: {filepath}")
            else:
                print(f"Cabeçalho já existe em: {filepath}. Ignorando.")
    except Exception as e:
        print(f"Erro ao processar {filepath}: {e}")

def main():
    if not os.path.exists(PROJECT_ROOT):
        print(f"Pasta raiz do projeto '{PROJECT_ROOT}' não encontrada. Execute o script Bash primeiro.")
        return

    print(f"Populando cabeçalhos nos arquivos .md dentro de '{PROJECT_ROOT}'...")

    for root, _, files in os.walk(PROJECT_ROOT):
        for file in files:
            relative_filepath = os.path.relpath(os.path.join(root, file), PROJECT_ROOT)
            if relative_filepath in FILE_METADATA:
                full_filepath = os.path.join(root, file)
                populate_header(full_filepath, FILE_METADATA[relative_filepath])
            elif file.endswith(".md"): # Para outros arquivos .md não especificados no metadata
                 full_filepath = os.path.join(root, file)
                 # Cria metadata genérico para arquivos não listados especificamente
                 generic_metadata = {
                    "title": os.path.basename(file).replace(".md", ""),
                    "responsibility": "A definir",
                    "authors": "Time MEx",
                    "version": "0.0.1"
                 }
                 populate_header(full_filepath, generic_metadata)

    print("Processo de população de cabeçalhos concluído.")

if __name__ == "__main__":
    main()