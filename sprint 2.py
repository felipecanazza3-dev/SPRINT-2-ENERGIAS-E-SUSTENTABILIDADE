import time
import random


class PostoAbastecimentoSustentavel:
    def __init__(self, capacidade_maxima_grid=150.0):
        # Capacidade maxima de energia que o estabelecimento aguenta do grid (em kW)
        self.capacidade_maxima_grid = capacidade_maxima_grid
        self.vagas_carregadores = {"Vaga 1": 0.0, "Vaga 2": 0.0, "Vaga 3": 0.0}

    def simular_ambiente(self):
        """Simula as variacoes em tempo real do shopping e dos paineis solares."""
        # Consumo do shopping varia de acordo com o movimento
        consumo_shopping = round(random.uniform(60.0, 110.0), 2)
        # Geracao solar fotovoltaica ligada ao posto
        geracao_solar = round(random.uniform(15.0, 40.0), 2)
        return consumo_shopping, geracao_solar

    def algoritmo_balanceamento_dinamico(self, consumo_shopping, geracao_solar):
        """Calcula o excedente seguro e distribui dinamicamente para os VEs."""
        # A energia total disponivel e a capacidade do grid + o que o sol esta gerando
        energia_total_disponivel = self.capacidade_maxima_grid + geracao_solar

        # Margem de seguranca para evitar curtos/apagoes (excedente real disponivel)
        excedente_energia = energia_total_disponivel - consumo_shopping

        # Quantos carros estao carregando no momento (simulacao de ocupacao aleatoria)
        carros_conectados = [vaga for vaga in self.vagas_carregadores.keys() if random.choice([True, False])]

        # Limpa cargas anteriores
        for vaga in self.vagas_carregadores:
            self.vagas_carregadores[vaga] = 0.0

        if not carros_conectados:
            return excedente_energia, 0.0

        # Distribuicao igualitaria do excedente entre os carros conectados
        potencia_por_carro = round(excedente_energia / len(carros_conectados), 2)

        if potencia_por_carro > 50.0:
            potencia_por_carro = 50.0

        for vaga in carros_conectados:
            self.vagas_carregadores[vaga] = potencia_por_carro

        total_distribuido_ve = potencia_por_carro * len(carros_conectados)
        return excedente_energia, total_distribuido_ve

    def exibir_dashboard(self, ciclo, consumo_shopping, geracao_solar, excedente, total_ve):
        """Exibe os dados no terminal simulando um monitoramento tecnico."""
        consumo_total_grid = (consumo_shopping + total_ve) - geracao_solar
        carga_uso_percentual = (consumo_total_grid / self.capacidade_maxima_grid) * 100

        print("-" * 60)
        print(f"| MONITORAMENTO EM TEMPO REAL - CICLO {ciclo} |")
        print("-" * 60)
        print(f"Geracao Solar Atual      : {geracao_solar} kW (Energia Limpa)")
        print(f"Consumo Atual do Shopping: {consumo_shopping} kW")
        print(f"Excedente Seguro p/ VEs  : {round(excedente, 2)} kW")
        print("-" * 60)
        print("STATUS DOS CARREGADORES:")
        for vaga, carga in self.vagas_carregadores.items():
            status = f"Carregando a {carga} kW" if carga > 0 else "Livre / Sem demanda"
            print(f"  * {vaga}: {status}")
        print("-" * 60)
        print(f"Carga Total Utilizada do Grid: {round(consumo_total_grid, 2)} / {self.capacidade_maxima_grid} kW")
        print(f"Uso da Infraestrutura Local  : {round(carga_uso_percentual, 2)}%")

        if carga_uso_percentual > 95.0:
            print("ALERTA: Sistema operando proximo ao limite do Grid!")
        else:
            print("SISTEMA ESTAVEL: Balanceamento dinamico aplicando eficiencia energetica.")
        print("-" * 60 + "\n")


# Execucao do Prototipo
if __name__ == "__main__":
    posto = PostoAbastecimentoSustentavel(capacidade_maxima_grid=150.0)

    print("Iniciando Prova de Conceito - Sprint 2")
    print("Pressione CTRL+C para encerrar a simulacao.\n")
    time.sleep(2)

    ciclo = 1
    try:
        while True:
            # 1. Coleta dados simulados do ambiente
            consumo_shop, energia_sol = posto.simular_ambiente()

            # 2. Executa o algoritmo de balanceamento inteligente
            excedente, total_ve = posto.algoritmo_balanceamento_dinamico(consumo_shop, energia_sol)

            # 3. Mostra os resultados na tela
            # CORRECAO BEM AQUI: de 'consumption_shop' para 'consumo_shopping'
            posto.exibir_dashboard(ciclo, consumo_shopping=consumo_shop, geracao_solar=energia_sol,
                                   excedente=excedente, total_ve=total_ve)

            ciclo += 1
            time.sleep(4)  # Atualiza a cada 4 segundos para fins de demonstracao
    except KeyboardInterrupt:
        print("\nSimulacao encerrada pelo usuario. Prototipo finalizado com sucesso!")