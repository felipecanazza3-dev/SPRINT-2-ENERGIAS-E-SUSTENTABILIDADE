# Solucao em Energias Renovaveis e Sustentaveis - Postos Comerciais de Abastecimento

## Descricao do Projeto
Este projeto tem como objetivo principal transformar o cenario atual de abastecimento de veiculos eletricos (VEs), migrando de uma infraestrutura residencial para uma solucao comercial viavel e eficiente atraves da criacao de postos de abastecimento inteligentes. 

Com base em pesquisas detalhadas, a solucao ataca tres dores criticas do mercado:
1. Sobrecarga da rede eletrica local em horarios de pico.
2. Complexidade e ineficiencia na monetizacao e cobranca do servico.
3. Falta de previsibilidade financeira e controle de danos para o comerciante.

## Sprint 2 - Prova de Conceito Funcional (PoC)
A Prova de Conceito desenvolvida em Python foca na demonstracao operacional do Algoritmo de Balanceamento de Carga Dinamico, integrado a um sistema de captacao de energia solar fotovoltaica.

### Funcionalidades do Codigo
* **Simulacao de Ambiente:** Varia dinamicamente em tempo real o consumo de energia de um estabelecimento comercial (ex: Shopping) e a taxa de geracao de energia limpa (paineis solares).
* **Algoritmo de Balanceamento Inteligente:** Monitora a carga total, calcula o excedente de energia seguro de forma dinamica e distribui essa potencia de maneira igualitaria entre os carregadores ativos.
* **Protecao contra Apagoes:** O algoritmo impede que a demanda dos VEs ultrapasse o limite maximo do grid contratado, garantindo a integridade fisica da rede eletrica e evitando curtos-circuitos.

### Justificativa Tecnica e Sustentabilidade
* **Eficiencia Energetica:** Garante o aproveitamento maximo da infraestrutura local sem a necessidade de investimentos massivos em novos transformadores ou aumento fixo de contratos de demanda com a concessionaria.
* **Principios de Sustentabilidade:** A prioridade de carregamento utiliza a energia excedente vinda da matriz solar limpa e barata instalada junto ao posto, reduzindo a pegada de carbono da operacao e o custo financeiro total por recarga.

## Instrucoes de Uso e Como Executar
1. Certifique-se de possuir o ambiente Python 3 instalado no computador.
2. Baixe ou clone os arquivos deste repositorio.
3. Abra o terminal na pasta do projeto e execute o comando:
   ```bash
   python "sprint 2.py"
