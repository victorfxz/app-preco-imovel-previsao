# Aplicativo de Previsão de Preços Imobiliários

Este repositório contém um notebook e aplicativo web simples construído com o Dash que prevê preços imobiliários com base em determinadas características. O aplicativo utiliza um modelo de regressão linear treinado em um conjunto de dados de imóveis.





![](D:\Git\estudos-e-projetos-de-ciencia-de-dados\aprendizado-de-maquina\app-preco-imovel-previsao\img\app.gif)

## Início

### Pré-requisitos

Certifique-se de ter as seguintes bibliotecas instaladas:

```bash
!pip install pandas scikit-learn dash
```

### Instalação

Clone o repositório:

```bash
git clone https://github.com/seunome/previsao-de-precos-imobiliarios.git
cd previsao-de-precos-imobiliarios
```

### Uso

1. Substitua o espaço reservado pelo caminho real para o seu conjunto de dados de imóveis no script.

```python
file_path = "./data/real_estate.csv"  # substitua pelo seu caminho.
```

2. Execute o aplicativo:

```bash
python app.py
```

Acesse `http://127.0.0.1:8050/` em seu navegador da web para acessar o aplicativo.

## Recursos

- Preveja preços imobiliários com base na distância até a estação MRT mais próxima, número de lojas de conveniência, latitude e longitude.
- Interface web interativa com campos de entrada para interação do usuário.

## Estrutura do Aplicativo

- `app.py`: O script principal contendo o código do aplicativo.
- `./data/real_estate.csv`: Conjunto de dados usados.
- `notebook/previsao_de_precos_de_imoveis_com_python.ipynb`: Contem uma abordagem sistemática para prever os preços de imóveis. Com: engenharia de recursos, análise exploratória de dados (EDA) e treinamento do modelo.
- `img/...`: Gráficos.

## Agradecimentos

- Este aplicativo utiliza o Dash, um framework web em Python para construir aplicações web analíticas.
- statso.io/community - dataset.