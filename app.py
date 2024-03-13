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
        html.Div([
            html.H1("Previsão de Preços Imobiliários", style={'text-align': 'center'}),
            html.Div([
                dcc.Input(id='distance_to_mrt', type='number', placeholder='Distância até a Estação MRT (metros)',
                          style={'margin': '10px', 'padding': '10px'}),
                dcc.Input(id='num_convenience_stores', type='number', placeholder='Número de Lojas de Conveniência',
                          style={'margin': '10px', 'padding': '10px'}),
                dcc.Input(id='latitude', type='number', placeholder='Latitude',
                          style={'margin': '10px', 'padding': '10px'}),
                dcc.Input(id='longitude', type='number', placeholder='Longitude',
                          style={'margin': '10px', 'padding': '10px'}),
                html.Button('Estimar Preço', id='predict_button', n_clicks=0,
                            style={'margin': '10px', 'padding': '13px', 'background-color': 'rgb(0, 0, 238)', 'border': 'none', 'color': 'white'}),
            ], style={'text-align': 'center'}),
            html.Div(id='prediction_output', style={'text-align': 'center', 'font-size': '20px', 'margin-top': '20px'})
        ], style={'width': '50%', 'margin': '0 auto', 'border': 'none', 'padding': '20px', 'border-radius': '10px'})
    ])

# Ponto de entrada principal.
if __name__ == '__main__':
    # Carrega e pré-processa o conjunto de dados.
    file_path = "./data/real_estate.csv"
    X, y = load_dataset(file_path)

    # Divide o conjunto de dados.
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Treina o modelo.
    model = train_model(X_train, y_train)

    # Inicializa o aplicativo Dash.
    app = dash.Dash(__name__)

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
        if n_clicks > 0 and all(v is not None for v in [distance_to_mrt, num_convenience_stores, latitude, longitude]):
            # Prepara o vetor de recursos.
            features = pd.DataFrame([[distance_to_mrt, num_convenience_stores, latitude, longitude]], 
                                    columns=['Distance to the nearest MRT station', 
                                             'Number of convenience stores', 'Latitude', 'Longitude'])
            # Previsão.
            prediction = model.predict(features)[0]
            return f'Preço Previsto do Imóvel: R${prediction:.2f} por metro quadrado.'
        elif n_clicks > 0:
            return 'Por favor, insira todos os valores para obter uma previsão!'
        return ''

    # Executa o app.
    app.run_server(debug=True)

