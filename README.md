# 🏠 Aplicativo de Previsão de Preços Imobiliários

<div align="center">

![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
![Dash](https://img.shields.io/badge/dash-2.0+-green.svg)
![Scikit-learn](https://img.shields.io/badge/scikit--learn-1.0+-orange.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

**Uma aplicação web moderna e intuitiva para previsão de preços imobiliários usando Machine Learning**

[🚀 Demo](#-como-usar) • [📋 Funcionalidades](#-funcionalidades) • [⚙️ Instalação](#️-instalação) • [📊 Dados](#-sobre-os-dados)

</div>

---

## 📖 Sobre o Projeto

Este projeto oferece uma **interface web elegante e responsiva** construída com Dash que utiliza **Machine Learning** para prever preços imobiliários. O sistema emprega um modelo de **Regressão Linear** treinado com dados reais do mercado imobiliário, considerando fatores como localização, proximidade de transporte público e infraestrutura local.

### 🎯 Objetivo
Fornecer estimativas precisas e rápidas de preços imobiliários para auxiliar compradores, vendedores e investidores em suas decisões.

## ✨ Funcionalidades

- 🎨 **Interface Moderna**: Design responsivo com gradientes e animações
- 🤖 **Machine Learning**: Modelo de regressão linear para previsões precisas
- 📱 **Responsivo**: Funciona perfeitamente em desktop e mobile
- ⚡ **Tempo Real**: Previsões instantâneas ao inserir os dados
- 🛡️ **Validação**: Verificação automática dos dados de entrada
- 📊 **Feedback Visual**: Mensagens claras e informativas para o usuário

## 🚀 Como Usar

### Pré-requisitos

Certifique-se de ter o Python 3.8+ instalado em seu sistema.

### ⚙️ Instalação

1. **Clone o repositório:**
```bash
git clone https://github.com/seu-usuario/previsao-precos-imobiliarios.git
cd previsao-precos-imobiliarios
```

2. **Instale as dependências:**
```bash
pip install pandas scikit-learn dash
```

### 🎯 Executando o Aplicativo

```bash
python app.py
```

Acesse **`http://127.0.0.1:8050/`** em seu navegador para usar a aplicação.

## 📊 Como Funciona

1. **📍 Insira os Dados**: Preencha as informações do imóvel:
   - Distância até a estação MRT mais próxima (metros)
   - Número de lojas de conveniência na área
   - Coordenadas geográficas (latitude e longitude)

2. **🔮 Obtenha a Previsão**: Clique no botão e receba instantaneamente o preço estimado por metro quadrado

3. **📈 Análise**: O modelo considera todos os fatores para fornecer uma estimativa baseada em dados históricos

## 🏗️ Estrutura do Projeto

```
📦 previsao-precos-imobiliarios/
├── 📄 app.py                                    # Aplicação principal
├── 📊 real_estate.csv                          # Dataset de imóveis
├── 📓 previsao_de_precos_de_imoveis_com_python.ipynb  # Notebook de análise
└── 📖 README.md                                # Este arquivo
```

## 📊 Sobre os Dados

O dataset utilizado contém **414 registros** de transações imobiliárias reais com as seguintes características:

| Campo | Descrição |
|-------|-----------|
| 🚇 **Distance to MRT** | Distância até a estação de metrô mais próxima |
| 🏪 **Convenience Stores** | Número de lojas de conveniência na área |
| 📍 **Latitude/Longitude** | Coordenadas geográficas precisas |
| 💰 **Price per Unit Area** | Preço por metro quadrado (variável alvo) |

## 🔧 Tecnologias Utilizadas

- **Python 3.8+**: Linguagem principal
- **Dash**: Framework para aplicações web interativas
- **Pandas**: Manipulação e análise de dados
- **Scikit-learn**: Machine Learning e modelagem
- **HTML/CSS**: Interface e estilização

## 🎨 Interface

A aplicação possui um design moderno com:
- **Gradientes suaves** e cores harmoniosas
- **Cards elegantes** para organização do conteúdo
- **Ícones intuitivos** para melhor usabilidade
- **Feedback visual** em tempo real
- **Validação de dados** com mensagens claras

## 🤝 Contribuindo

Contribuições são sempre bem-vindas! Para contribuir:

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 🙏 Agradecimentos

- **Dash Community**: Pelo excelente framework web
- **Scikit-learn**: Pelas ferramentas de Machine Learning
- **statso.io**: Pelo dataset utilizado no projeto

---

<div align="center">

**Desenvolvido com ❤️ para facilitar decisões imobiliárias inteligentes**

⭐ Se este projeto foi útil para você, considere dar uma estrela!

</div>