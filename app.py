import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import dash
from dash import html, dcc, Input, Output, State

# Função para carregar e pré-processar o conjunto de dados.
def load_dataset(file_path):
    real_estate_data = pd.read_csv(file_path)
    features = ['Distance to the nearest MRT station', 'Number of convenience stores', 'Latitude', 'Longitude']
    target = 'House price of unit area'
    X = real_estate_data[features]
    y = real_estate_data[target]
    return X, y

# Função para treinar o modelo.
def train_model(X_train, y_train):
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model

# Função para definir o layout do aplicativo.
def define_layout():
    return html.Div([
        # Header com gradiente
        html.Div([
            html.H1("🏠 Previsão de Preços Imobiliários em São Paulo",
                   style={
                       'text-align': 'center',
                       'color': 'white',
                       'margin': '0',
                       'padding': '30px 0',
                       'font-family': 'Arial, sans-serif',
                       'font-weight': 'bold',
                       'font-size': '2.5rem',
                       'text-shadow': '2px 2px 4px rgba(0,0,0,0.3)'
                   }),
            html.P("Estimar o valor de imóveis com base em dados reais (2023).",
                  style={
                      'text-align': 'center',
                      'color': 'rgba(255,255,255,0.9)',
                      'margin': '0',
                      'padding-bottom': '20px',
                      'font-family': 'Arial, sans-serif',
                      'font-size': '1.1rem'
                  })
        ], style={
            'background': 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
            'margin': '-8px -8px 40px -8px',
            'box-shadow': '0 4px 15px rgba(0,0,0,0.2)'
        }),

        # Container principal
        html.Div([
            # Card de entrada de dados
            html.Div([
                html.H3("📊 Dados do Imóvel",
                       style={
                           'color': '#2c3e50',
                           'margin-bottom': '25px',
                           'font-family': 'Arial, sans-serif',
                           'text-align': 'center'
                       }),

                # Grid de inputs
                html.Div([
                    html.Div([
                        html.Label("🚇 Distância até MRT (metros)",
                                 style={'font-weight': 'bold', 'color': '#34495e', 'margin-bottom': '8px', 'display': 'block'}),
                        dcc.Input(id='distance_to_mrt', type='number', placeholder='Ex: 500',
                                  style={
                                      'width': '100%',
                                      'padding': '12px 15px',
                                      'border': '2px solid #e0e6ed',
                                      'border-radius': '8px',
                                      'font-size': '16px',
                                      'transition': 'all 0.3s ease',
                                      'box-sizing': 'border-box'
                                  })
                    ], style={'margin-bottom': '20px'}),

                    html.Div([
                        html.Label("🏪 Número de Lojas de Conveniência",
                                 style={'font-weight': 'bold', 'color': '#34495e', 'margin-bottom': '8px', 'display': 'block'}),
                        dcc.Input(id='num_convenience_stores', type='number', placeholder='Ex: 5',
                                  style={
                                      'width': '100%',
                                      'padding': '12px 15px',
                                      'border': '2px solid #e0e6ed',
                                      'border-radius': '8px',
                                      'font-size': '16px',
                                      'transition': 'all 0.3s ease',
                                      'box-sizing': 'border-box'
                                  })
                    ], style={'margin-bottom': '20px'}),

                    html.Div([
                        html.Div([
                            html.Label("📍 Latitude",
                                     style={'font-weight': 'bold', 'color': '#34495e', 'margin-bottom': '8px', 'display': 'block'}),
                            dcc.Input(id='latitude', type='number', placeholder='Ex: 25.0123',
                                      style={
                                          'width': '100%',
                                          'padding': '12px 15px',
                                          'border': '2px solid #e0e6ed',
                                          'border-radius': '8px',
                                          'font-size': '16px',
                                          'transition': 'all 0.3s ease',
                                          'box-sizing': 'border-box'
                                      })
                        ], style={'width': '48%', 'display': 'inline-block'}),

                        html.Div([
                            html.Label("📍 Longitude",
                                     style={'font-weight': 'bold', 'color': '#34495e', 'margin-bottom': '8px', 'display': 'block'}),
                            dcc.Input(id='longitude', type='number', placeholder='Ex: 121.5678',
                                      style={
                                          'width': '100%',
                                          'padding': '12px 15px',
                                          'border': '2px solid #e0e6ed',
                                          'border-radius': '8px',
                                          'font-size': '16px',
                                          'transition': 'all 0.3s ease',
                                          'box-sizing': 'border-box'
                                      })
                        ], style={'width': '48%', 'display': 'inline-block', 'margin-left': '4%'})
                    ], style={'margin-bottom': '30px'}),

                    # Botão de previsão
                    html.Div([
                        html.Button('🔮 Estimar Preço do Imóvel', id='predict_button', n_clicks=0,
                                    style={
                                        'background': 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
                                        'border': 'none',
                                        'color': 'white',
                                        'padding': '15px 40px',
                                        'font-size': '18px',
                                        'font-weight': 'bold',
                                        'border-radius': '25px',
                                        'cursor': 'pointer',
                                        'transition': 'all 0.3s ease',
                                        'box-shadow': '0 4px 15px rgba(102, 126, 234, 0.4)',
                                        'font-family': 'Arial, sans-serif'
                                    })
                    ], style={'text-align': 'center'})
                ])
            ], style={
                'background': 'white',
                'padding': '40px',
                'border-radius': '15px',
                'box-shadow': '0 10px 30px rgba(0,0,0,0.1)',
                'margin-bottom': '30px'
            }, className='card-animation'),

            # Card de resultado
            html.Div(id='prediction_output',
                     style={
                         'text-align': 'center',
                         'font-size': '24px',
                         'font-weight': 'bold',
                         'color': '#2c3e50',
                         'background': 'white',
                         'padding': '30px',
                         'border-radius': '15px',
                         'box-shadow': '0 10px 30px rgba(0,0,0,0.1)',
                         'font-family': 'Arial, sans-serif',
                         'min-height': '60px',
                         'display': 'flex',
                         'align-items': 'center',
                         'justify-content': 'center'
                     }, className='card-animation')
        ], style={
            'max-width': '800px',
            'margin': '0 auto',
            'padding': '0 20px'
        })
    ], style={
        'background': 'linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%)',
        'min-height': '100vh',
        'font-family': 'Arial, sans-serif',
        'padding': '0'
    })

# Ponto de entrada principal.
if __name__ == '__main__':
    # Carrega e pré-processa o conjunto de dados.
    file_path = "./real_estate.csv"
    X, y = load_dataset(file_path)

    # Divide o conjunto de dados.
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Treina o modelo.
    model = train_model(X_train, y_train)

    # Inicializa o aplicativo Dash.
    app = dash.Dash(__name__)

    # Adiciona CSS customizado para efeitos hover e animações
    app.index_string = '''
    <!DOCTYPE html>
    <html>
        <head>
            {%metas%}
            <title>{%title%}</title>
            {%favicon%}
            {%css%}
            <style>
                /* Efeitos hover para inputs */
                input[type="number"]:hover {
                    border-color: #667eea !important;
                    box-shadow: 0 0 10px rgba(102, 126, 234, 0.3) !important;
                }

                input[type="number"]:focus {
                    border-color: #667eea !important;
                    box-shadow: 0 0 15px rgba(102, 126, 234, 0.5) !important;
                    outline: none !important;
                }

                /* Efeito hover para o botão */
                button:hover {
                    transform: translateY(-2px) !important;
                    box-shadow: 0 6px 20px rgba(102, 126, 234, 0.6) !important;
                }

                /* Animação suave para todos os elementos */
                * {
                    transition: all 0.3s ease !important;
                }

                /* Animação de entrada para os cards */
                @keyframes fadeInUp {
                    from {
                        opacity: 0;
                        transform: translateY(30px);
                    }
                    to {
                        opacity: 1;
                        transform: translateY(0);
                    }
                }

                .card-animation {
                    animation: fadeInUp 0.6s ease-out;
                }
            </style>
        </head>
        <body>
            {%app_entry%}
            <footer>
                {%config%}
                {%scripts%}
                {%renderer%}
            </footer>
        </body>
    </html>
    '''

    # Define o layout do aplicativo.
    app.layout = define_layout()

    # Callback para atualizar a saída.
    @app.callback(
        Output('prediction_output', 'children'),
        [Input('predict_button', 'n_clicks')],
        [State('distance_to_mrt', 'value'), 
         State('num_convenience_stores', 'value'),
         State('latitude', 'value'),
         State('longitude', 'value')]
    )
    
    # Função para atualizar a saída.
    def update_output(n_clicks, distance_to_mrt, num_convenience_stores, latitude, longitude):
        if n_clicks == 0:
            return html.Div([
                html.P("👆 Preencha os campos acima e clique no botão para obter sua previsão!",
                       style={'color': '#7f8c8d', 'font-size': '18px', 'margin': '0'})
            ])

        if not all(v is not None for v in [distance_to_mrt, num_convenience_stores, latitude, longitude]):
            return html.Div([
                html.P("⚠️ Por favor, preencha todos os campos para obter uma previsão!",
                       style={'color': '#e74c3c', 'font-size': '18px', 'margin': '0'})
            ])

        # Validações básicas
        if distance_to_mrt < 0:
            return html.Div([
                html.P("❌ A distância até a estação MRT deve ser um valor positivo!",
                       style={'color': '#e74c3c', 'font-size': '18px', 'margin': '0'})
            ])

        if num_convenience_stores < 0:
            return html.Div([
                html.P("❌ O número de lojas de conveniência deve ser um valor positivo!",
                       style={'color': '#e74c3c', 'font-size': '18px', 'margin': '0'})
            ])

        try:
            # Prepara o vetor de recursos.
            features = pd.DataFrame([[distance_to_mrt, num_convenience_stores, latitude, longitude]],
                                    columns=['Distance to the nearest MRT station',
                                             'Number of convenience stores', 'Latitude', 'Longitude'])
            # Previsão.
            prediction = model.predict(features)[0]

            # Formatação do resultado com estilo
            return html.Div([
                html.Div([
                    html.H3("✅ Previsão Concluída!",
                           style={'color': '#27ae60', 'margin-bottom': '15px'}),
                    html.Div([
                        html.Span("💰 Preço Estimado: ",
                                 style={'font-size': '20px', 'color': '#2c3e50'}),
                        html.Span(f"R$ {prediction:.2f}",
                                 style={'font-size': '28px', 'font-weight': 'bold', 'color': '#27ae60'}),
                        html.Span(" por m²",
                                 style={'font-size': '18px', 'color': '#7f8c8d'})
                    ], style={'margin-bottom': '10px'}),
                    html.P("📊 Esta previsão foi gerada usando machine learning com base nos dados fornecidos.",
                           style={'color': '#7f8c8d', 'font-size': '14px', 'margin': '0', 'font-style': 'italic'})
                ])
            ])

        except Exception as e:
            return html.Div([
                html.P("❌ Erro ao processar a previsão. Verifique os dados inseridos.",
                       style={'color': '#e74c3c', 'font-size': '18px', 'margin': '0'})
            ])

    # Executa o app.
    app.run(debug=True)

