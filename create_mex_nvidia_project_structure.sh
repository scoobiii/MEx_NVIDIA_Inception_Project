#!/bin/bash

# Define a pasta raiz do projeto
PROJECT_ROOT="MEx_NVIDIA_Inception_Project"

echo "Criando a estrutura de pastas e arquivos para o projeto MEx-NVIDIA Inception..."

# Cria a pasta raiz
mkdir -p "$PROJECT_ROOT"
cd "$PROJECT_ROOT"

# Cria as pastas principais
mkdir -p docs
mkdir -p src
mkdir -p diagrams
mkdir -p tasks

# Cria as subpastas dentro de 'docs'
mkdir -p docs/01_NVIDIA_Program_Info
mkdir -p docs/02_MEx_Pitch_Deck
mkdir -p docs/03_Edge_Swarm_DLT_Tech_Docs
mkdir -p docs/04_NVIDIA_Integration_Plan
mkdir -p docs/05_Meeting_Notes
mkdir -p docs/06_Progress_Reports
mkdir -p docs/templates

# Cria arquivos na raiz
touch README.md
touch LICENSE
touch .gitignore

# Cria arquivos dentro de 'docs'
touch docs/01_NVIDIA_Program_Info/NVIDIA_Inception_Startup_Program_ES-LA_2025.pdf # Arquivo existente, apenas placeholder
touch docs/01_NVIDIA_Program_Info/Outros_Materiais_da_NVIDIA.pdf # Placeholder para outros materiais

touch docs/02_MEx_Pitch_Deck/MEx_Edge_Swarm_DLT_Pitch_NVIDIA.pptx # Placeholder
touch docs/02_MEx_Pitch_Deck/MEx_Edge_Swarm_DLT_White_Paper.pdf

touch docs/03_Edge_Swarm_DLT_Tech_Docs/Edge_Swarm_DLT_Overview.md
touch docs/03_Edge_Swarm_DLT_Tech_Docs/Architecture_Diagrams.drawio # Placeholder para Draw.io
touch docs/03_Edge_Swarm_DLT_Tech_Docs/Requirements.md
touch docs/03_Edge_Swarm_DLT_Tech_Docs/Outras_Docs_Tecnicas_do_Drex_Swarm.md

touch docs/04_NVIDIA_Integration_Plan/Integration_Strategy.md
touch docs/04_NVIDIA_Integration_Plan/GPU_Resource_Allocation_Plan.md
touch docs/04_NVIDIA_Integration_Plan/Software_Stack_Compatibility.md
touch docs/04_NVIDIA_Integration_Plan/Security_Considerations_NVIDIA.md

touch docs/05_Meeting_Notes/2025-08-22_NVIDIA_Intro_Call.md
touch docs/05_Meeting_Notes/2025-09-XX_Inception_Kickoff.md

touch docs/06_Progress_Reports/Q1_2026_Progress_Report.md

touch docs/templates/Meeting_Minutes_Template.md
touch docs/templates/Progress_Report_Template.md

# Cria placeholders para 'src' (apenas pastas por enquanto)
mkdir -p src/nvidia_integrations/cuda_kernels
mkdir -p src/nvidia_integrations/api_wrappers
mkdir -p src/dlt_core

# Cria placeholders para 'diagrams'
touch diagrams/DLT_NVIDIA_Architecture.png # Placeholder para imagem

# Cria arquivos em 'tasks'
touch tasks/ROADMAP.md

echo "Estrutura criada com sucesso em '$PROJECT_ROOT'!"