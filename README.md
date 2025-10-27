Projeto Prático 1 — Física Computacional

Este projeto foi desenvolvido como parte da disciplina de Física Computacional, com o objetivo de aplicar conceitos de programação científica em Python.  
O programa realiza conversão de unidades físicas e operações com vetores 2D, além de plotar vetores no plano cartesiano utilizando a biblioteca Matplotlib.

------------------------------------------------------------
FUNCIONALIDADES
------------------------------------------------------------

1. CONVERSOR DE UNIDADES
O programa permite converter entre diferentes unidades de:
- Velocidade: km/h ↔ m/s
- Massa: kg ↔ g
- Comprimento: m ↔ cm, cm ↔ m, m ↔ km, km ↔ m

2. OPERAÇÕES COM VETORES 2D
O usuário pode inserir as componentes de dois vetores (A e B) e o programa realiza:
- Soma (A + B)
- Subtração (A - B)
- Cálculo do módulo de cada vetor (‖A‖ e ‖B‖)

3. PLOTAGEM GRÁFICA
Os vetores e os resultados das operações são plotados no plano cartesiano, com:
- Eixos X e Y centralizados
- Escala proporcional
- Legenda identificando cada vetor
- Cores distintas para melhor visualização

------------------------------------------------------------
Programas utilizados:
------------------------------------------------------------
- Python 3
- NumPy
- Matplotlib

------------------------------------------------------------
COMO EXECUTAR O PROJETO
------------------------------------------------------------

1° Clonar o repositório:
    git clone https://github.com/seu-usuario/nome-do-repositorio.git

2° Instalar as dependências:
    pip install numpy matplotlib

3° Rodar o programa:
      python projeto.py

------------------------------------------------------------
ESTRUTURA DO MENU
------------------------------------------------------------
1. Conversor de Unidades
    1. Velocidade
    2. Massa
    3. Comprimento
2. Operações com Vetores 2D
3. Sair

------------------------------------------------------------
EXEMPLO
------------------------------------------------------------
Escolha uma das opções abaixo:
1. Conversor de Unidades
2. Operações com Vetores 2D
3. Sair

Se o usuário escolher 2, o programa solicitará as componentes dos vetores:

Insira as coordenadas para o Vetor A:
Componente Ax: 3
Componente Ay: 2

Insira as coordenadas para o Vetor B:
Componente Bx: 1
Componente By: 4

O programa exibirá:
Soma A + B = (4, 6)
Subtração A - B = (2, -2)
|A| = 3.61
|B| = 4.12

E abrirá uma janela gráfica com a representação dos vetores.

------------------------------------------------------------
AUTORES:
------------------------------------------------------------
- Giselly Jahel
- Thaíssa Sampaio
- Thalisson Souza

------------------------------------------------------------
LICENÇA
------------------------------------------------------------
Este projeto é de uso educacional e foi desenvolvido para fins de aprendizado na disciplina de Física Computacional.

------------------------------------------------------------
UNIVERSIDADE / CURSO / SEMESTRE / DISCIPLINA
------------------------------------------------------------
Universidade Estadual de Santa Cruz

Ciência da Computação

Semestre: 2025.2

Disciplina: Física Computacional
