import json

def salvar_historico(valor, origem, destino, resultado):
    historico = {
        "valor": valor,
        "moeda_origem": origem,
        "moeda_destino": destino,
        "resultado": resultado
    }
    with open("historico.json", "a") as arquivo:
        arquivo.write(json.dumps(historico) + "\n")
