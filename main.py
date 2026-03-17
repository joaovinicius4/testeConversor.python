from converter import converter
from historico import salvar_historico

# Lista de moedas suportadas (pode aumentar conforme necessidade)
MOEDAS = {
    "USD": "Dólar Americano",
    "BRL": "Real Brasileiro",
    "EUR": "Euro",
    "GBP": "Libra Esterlina",
    "JPY": "Iene Japonês",
    "CAD": "Dólar Canadense",
    "AUD": "Dólar Australiano",
    "CHF": "Franco Suíço"
}

def mostrar_opcoes():
    print("\n=== Moedas disponíveis ===")
    for codigo, nome in MOEDAS.items():
        print(f"{codigo} - {nome}")
    print("==========================\n")

def menu():
    print("\n=== Conversor de Moedas ===")
    mostrar_opcoes()

    try:
        valor = float(input("Digite o valor: "))
        origem = input("Moeda de origem (ex: USD): ").upper()
        destino = input("Moeda de destino (ex: BRL): ").upper()

        resultado = converter(valor, origem, destino)
        print(f"\n{valor} {origem} = {resultado:.2f} {destino}")
        salvar_historico(valor, origem, destino, resultado)

    except Exception as e:
        print("Erro:", e)

if __name__ == "__main__":
    menu()
    input("\nPressione ENTER para sair...")
