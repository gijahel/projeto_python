import matplotlib.pyplot as plt  # type: ignore
import numpy as np  # type: ignore

""" Se o usuário selecionar conversão de velocidade, poderá escolher:
1: converter quilômetros por hora (km/h) para metros por segundo (m/s) ou
2: converter metros por segundo (m/s) para quilômetros por hora (km/h). 
Qualquer opção diferente dessas será inválida. """

def converter_velocidade():
    print("\nConversão de Velocidade:")
    print("1. Quilômetros por hora (km/h) para metros por segundo (m/s).")
    print("2. Metros por segundo (m/s) para quilômetros por hora (km/h).")
    escolha = int(input("Escolha a opção: "))

    if escolha == 1:
        valor = float(input("Digite o valor: "))
        resultado = valor / 3.6
        print(f"{valor} km/h = {resultado:.2f} m/s")
    elif escolha == 2:
        valor = float(input("Digite o valor: "))
        resultado = valor * 3.6
        print(f"{valor} m/s = {resultado:.2f} km/h")
    else:
        print("Opção inválida.")
        
""" Se o usuário selecionar conversão de massa, poderá escolher:
1: Converter quilograma (kg) para grama (g) ou
2: Converter grama (g) para quilograma (kg).
Qualquer opção diferente dessas será inválida. """

def converter_massa():
    print("\nConversão de Massa:")
    print("1. Quilograma (kg) para grama (g).")
    print("2. Grama (g) para quilograma (kg).")
    escolha = int(input("Escolha a opção: "))

    if escolha == 1:
        valor = float(input("Digite o valor: "))
        resultado = valor * 1000
        print(f"{valor} kg = {resultado:.2f} g")
    elif escolha == 2:
        valor = float(input("Digite o valor: "))
        resultado = valor / 1000
        print(f"{valor} g = {resultado:.2f} kg")
    else:
        print("Opção inválida.")

""" Se o usuário selecionar conversão de comprimente, poderá escolher:
1: Converter quilograma (kg) para grama (g);
2: Converter grama (g) para quilograma (kg);
3: Converter metros (m) para quilômetros (km) ou
4: Converter quilômetros (km) para metros (m).
Qualquer opção diferente dessas será inválida. """

def converter_comprimento():
    print("\nConversão de Comprimento:")
    print("1. Metros (m) para centímetros (cm).")
    print("2. Centímetros (cm) para metros (m).")
    print("3. Metros (m) para quilômetros (km).")
    print("4. Quilômetros (km) para metros (m).")
    escolha = int(input("Escolha a opção: "))

    if escolha == 1:
        valor = float(input("Digite o valor: "))
        resultado = valor * 100
        print(f"{valor} m = {resultado:.2f} cm")
    elif escolha == 2:
        valor = float(input("Digite o valor: "))
        resultado = valor / 100
        print(f"{valor} cm = {resultado:.2f} m")
    elif escolha == 3:
        valor = float(input("Digite o valor: "))
        resultado = valor / 1000
        print(f"{valor} m = {resultado:.2f} km")
    elif escolha == 4:
        valor = float(input("Digite o valor: "))
        resultado = valor * 1000
        print(f"{valor} km = {resultado:.2f} m")
    else:
        print("Opção inválida.")


""" Menu de opções, o usuário escolhe:
1: Para realizar conversão de unidades;
2: Para ealizar operações com vetores 2D ou
3: Para sair. 
Qualquer opção diferente dessas será inválida. """

def menu():
    while True:
        print("Escolha uma das opções abaixo:")
        print("1. Conversor de Unidades")
        print("2. Operações com Vetores 2D")
        print("3. Sair")
        opcao = int(input("Escolha a categoria: "))
        if opcao == 1:
            print("\nConverter:")
            print("1. Velocidade")
            print("2. Massa")
            print("3. Comprimento")
            print("4. Voltar\n")
            opcao = int(input("Escolha a categoria: "))

            if opcao == 1:
                converter_velocidade()
            elif opcao == 2:
                converter_massa()
            elif opcao == 3:
                converter_comprimento()
            elif opcao == 4:
                continue
            else:
                print("Opção inválida. Tente novamente.")
        elif opcao == 2:
            print("=== Operações com Vetores 2D ===\n")

            print("Insira as coordenadas para o Vetor A:")
            try:
                Ax = float(input("Componente Ax: "))
                Ay = float(input("Componente Ay: "))
            except ValueError:
                print("Entrada inválida. Por favor, insira números.")
                exit()

            print("\nInsira as coordenadas para o Vetor B:")
            try:
                Bx = float(input("Componente Bx: "))
                By = float(input("Componente By: "))
            except ValueError:
                print("Entrada inválida. Por favor, insira números.")
                exit()

            # --- Criação dos vetores NumPy ---
            A = np.array([Ax, Ay])
            B = np.array([Bx, By])

            Soma = A + B
            Subtracao = A - B
            modulo_A = np.linalg.norm(A)
            modulo_B = np.linalg.norm(B)

            print("\n--- Resultados das Operações ---")
            print(f"Vetor A: ({A[0]}, {A[1]})")
            print(f"Vetor B: ({B[0]}, {B[1]})")
            print(f"Soma A + B: ({Soma[0]}, {Soma[1]})")
            print(f"Subtração A - B: ({Subtracao[0]}, {Subtracao[1]})")
            print(f"Módulo |A|: {modulo_A:.2f}")
            print(f"Módulo |B|: {modulo_B:.2f}")

            # --- Plotar os Vetores (Matplotlib) ---

            # Ponto de origem para todos os vetores (0, 0)
            origin_x, origin_y = 0, 0

            #Determinar o limite máximo do gráfico para melhor visualização
            #Consideramos o maior valor absoluto entre todas as coordenadas x e y
            all_coords = np.concatenate([A, B, Soma, Subtracao])
            max_abs_coord = np.max(np.abs(all_coords))
            limit = max_abs_coord + 1.5  # Adiciona uma margem para visualização

            fig, ax = plt.subplots(figsize=(8, 8))

            # Função para plotar um vetor específico
            def plot_vetor(vetor, color, label):
                ax.quiver(origin_x, origin_y, vetor[0], vetor[1],
                          angles='xy', scale_units='xy', scale=1,
                          color=color, width=0.008, label=label)

                # Adicionar o rótulo do ponto final do vetor
                ax.text(vetor[0] * 1.05, vetor[1] * 1.05,
                        f'({vetor[0]:.1f}, {vetor[1]:.1f})', fontsize=9, color=color)

            # Plotagem dos vetores
            plot_vetor(A, 'blue', f'Vetor A({A[0]}, {A[1]})')
            plot_vetor(B, 'red', f'Vetor B({B[0]}, {B[1]})')
            plot_vetor(Soma, 'green', f'Soma A+B({Soma[0]}, {Soma[1]})')
            plot_vetor(Subtracao, 'orange',
                        f'Subtração A-B({Subtracao[0]}, {Subtracao[1]})')

            # Configurações de Eixos
            ax.axhline(0, color='gray', linestyle='--', linewidth=0.5)
            ax.axvline(0, color='gray', linestyle='--', linewidth=0.5)
            ax.grid(True, linestyle=':', alpha=0.6)

            # Definir limites dos eixos
            ax.set_xlim([-limit, limit])
            ax.set_ylim([-limit, limit])
            ax.set_xlabel('Eixo X')
            ax.set_ylabel('Eixo Y')

            # Título e Legenda
            ax.set_title('Representação dos Vetores e Suas Operações')
            ax.legend(loc='upper left')

            # Garante que os eixos X e Y tenham a mesma escala
            plt.gca().set_aspect('equal', adjustable='box')
            plt.show()
            print("\n")
        elif opcao == 3:
            print("Programa finalizado.\n")
            break
        else:
            print("Opção inválida. Tente novamente.\n")

menu()



