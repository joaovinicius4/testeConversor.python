import requests

def converter(valor, moeda_origem, moeda_destino):
    
    url = f"https://api.frankfurter.app/latest?amount={valor}&from={moeda_origem}&to={moeda_destino}"
    resposta = requests.get(url)

    if resposta.status_code != 200:
        raise Exception("Erro ao acessar a API de câmbio")

    dados = resposta.json()
    return dados['rates'][moeda_destino]
