import os

# Caminho base (pasta onde será criado o repositório)
#base_path = os.getcwd()  # Ou defina manualmente: r'C:\\Users\\SeuUsuario\\PastaDoProjeto'
base_path = r'D:\GoogleDrive\01 DOUTORADO\03 Meus Artigos\MXRio\Repositorio'
print('Criando pastas em:', base_path)

# Estrutura de diretórios
dirs = [
    'stl',
    os.path.join('testes'),
    os.path.join('docs')
]

# Conteúdos dos arquivos principais (README, protocolos, etc.)
arquivos_md = {
    'README.md': """# Manufatura Aditiva para Resiliência em Saúde  
# Additive Manufacturing for Healthcare Resilience

**Autores / Authors:**  
Raphael Vinagre, Marcelo Viana Marques Ferreira, João Victor Correia de Melo, Jorge Roberto Lopes

**Descrição / Description**  
Desenvolvimento, validação e documentação de dispositivos médicos impressos em 3D para ventilação não-invasiva em cenários de crise.  
Development, validation, and documentation of 3D-printed medical devices for non-invasive ventilation in crisis scenarios.

O projeto adota uma abordagem de design centrada no usuário e produção distribuída, promovendo resiliência hospitalar e manufatura aberta.  
The project adopts a human-centered design and distributed manufacturing, fostering hospital resilience and open manufacturing.

**Estrutura / Structure**
- `/stl/`: Arquivos STL das peças / STL 3D model files
- `/testes/`: Relatórios e dados experimentais / Test reports and raw data
- `/docs/`: Metodologia e fichas técnicas / Methodology and technical datasheets

**Licenciamento / Licensing**  
CC BY-SA 4.0. Consulte LICENSE / See LICENSE

---

Repositório bilíngue. Para informações detalhadas, consultar cada subdiretório.  
Bilingual repository. For detailed information, check each subdirectory.
""",

    os.path.join('testes', 'setup_testes.md'): """# Setup Experimental dos Testes  
# Test Experimental Setup

**Autores / Authors:**  
Raphael Vinagre, Marcelo Viana Marques Ferreira, João Victor Correia de Melo, Jorge Roberto Lopes

## Objetivo / Objective  
Descrever o ambiente, instrumentos e procedimentos empregados na validação funcional dos conectores impressos em 3D.  
Describe the environment, instruments, and procedures used in the functional validation of the 3D-printed connectors.

## Equipamentos / Equipment
- Analisador de fluxo: VT PLUS HF (Fluke)
- Sistema de aquisição: LabView 2021 + DAQ NI-9215
- Pulmão artificial: Test Lung 6810 (Dräger)
- Câmara climática: Binder BD56

## Protocolo / Protocol
1. Montar o conector impresso à máscara VNI e circuito do ventilador.  
   Attach the printed connector to the NIV mask and ventilator circuit.
2. Realizar 5 medições por unidade, monitorando pressão, vazão e vedação.  
   Perform 5 measurements per unit; monitor pressure, flow, and sealing.
3. Registrar dados em planilha CSV.  
   Record data in CSV spreadsheet.

*Para resultados quantitativos, consulte `tabela_resultados.csv`.*  
*For quantitative results, see `tabela_resultados.csv`.*
""",

    os.path.join('testes', 'relatorio_validacao_funcional.md'): """# Relatório de Validação Funcional  
# Functional Validation Report

**Autores / Authors:**  
Raphael Vinagre, Marcelo Viana Marques Ferreira, João Victor Correia de Melo, Jorge Roberto Lopes

## Amostragem / Sampling
- 30 unidades impressas (ABS) / 30 printed units (ABS)
- 10 unidades originais (controle, Philips) / 10 original units (control, Philips)

## Variáveis Testadas / Variables Tested
- Vedação / Seal integrity
- Resistência mecânica / Mechanical resistance
- Estabilidade dimensional pós-esterilização / Dimensional stability after sterilization

## Resultados / Results
- Diferença de pressão máxima: 2,1% (dentro da margem ISO 80601-2-12:2020)  
  Max pressure difference: 2.1% (within ISO 80601-2-12:2020 margin)
- Vedação equivalente em 98% dos testes  
  Equivalent sealing in 98% of tests
- Aceitação clínica: 100% na simulação  
  Clinical acceptance: 100% in simulation

*Detalhes quantitativos estão em `tabela_resultados.csv`.*  
*See `tabela_resultados.csv` for quantitative details.*
""",

    os.path.join('testes', 'protocolo_esterilizacao.md'): """# Protocolo de Esterilização  
# Sterilization Protocol

**Autores / Authors:**  
Raphael Vinagre, Marcelo Viana Marques Ferreira, João Victor Correia de Melo, Jorge Roberto Lopes

## Materiais Testados / Materials Tested
- ABS virgem e reciclado, PLA, PETG, Nylon, Resina SLA  
  Virgin and recycled ABS, PLA, PETG, Nylon, SLA resin

## Métodos / Methods
1. Autoclave (calor úmido, 121ºC, 20min)  
   Autoclave (moist heat, 121ºC, 20min)
2. Sterrad (peróxido de hidrogênio)  
   Sterrad (hydrogen peroxide vapor)

## Observações / Notes
- ABS: estável após 10 ciclos Sterrad.  
  ABS: stable after 10 Sterrad cycles.
- PLA/PETG: falha após 2 ciclos.  
  PLA/PETG: failed after 2 cycles.
""",

    os.path.join('docs', 'metodologia_RTD.md'): """# Metodologia Research Through Design (RTD)  
# Research Through Design (RTD) Methodology

**Autores / Authors:**  
Raphael Vinagre, Marcelo Viana Marques Ferreira, João Victor Correia de Melo, Jorge Roberto Lopes

## O que é RTD?  
A Research Through Design integra pesquisa e prática de projeto em ciclos iterativos, gerando soluções técnica e socialmente viáveis.  
Research Through Design (RTD) integrates research and design practice in iterative cycles, generating technically and socially viable solutions.

## Aplicação no projeto / Application in the project
- Imersão clínica / Clinical immersion
- Co-design interdisciplinar / Interdisciplinary co-design
- Prototipagem e testes iterativos / Iterative prototyping and testing
- Avaliação empírica e otimização final / Empirical evaluation and final optimization

*Veja documento principal para fluxograma detalhado.*  
*See main report for detailed flowchart.*
""",

    os.path.join('docs', 'ficha_tecnica_materiais.md'): """# Ficha Técnica – Polímero ABS para Impressão 3D  
# ABS Polymer Technical Datasheet for 3D Printing

**Autores / Authors:**  
Raphael Vinagre, Marcelo Viana Marques Ferreira, João Victor Correia de Melo, Jorge Roberto Lopes

| Parâmetro           | Valor (PT)      | Value (EN)         |
|---------------------|-----------------|--------------------|
| Temp. bico          | 220°C ± 5°C     | Nozzle temp        |
| Temp. mesa          | 110°C ± 2°C     | Bed temp           |
| Velocidade impressão| 60 mm/s         | Print speed        |
| Esp. parede         | 1,6 mm          | Wall thickness     |
| Altura de camada    | 0,2 mm          | Layer height       |
| Preenchimento       | 100%            | Infill             |
| Resfriamento        | Desligado       | Cooling off        |

**Observação / Note:**  
ABS recomendado pela estabilidade após esterilização em vapor e peróxido.  
ABS is recommended due to its stability after vapor and hydrogen peroxide sterilization.
"""
}

# Criar diretórios
for d in dirs:
    os.makedirs(os.path.join(base_path, d), exist_ok=True)

# Criar arquivos de texto (.md)
for filepath, content in arquivos_md.items():
    full_path = os.path.join(base_path, filepath)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(content)


print("Estrutura e arquivos criados com sucesso.")
