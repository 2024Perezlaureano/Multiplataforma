import flet as ft

def main(page: ft.Page):
    page.title = "Calculadora Energética"

    potencia = ft.TextField(label="Potencia (W)", value="0")
    tiempo = ft.TextField(label="Tiempo (h)", value="0")
    resultado = ft.Text("Consumo: 0 kWh")

    def calcular(e):
        try:
            p = float(potencia.value)
            t = float(tiempo.value)
            consumo = (p * t) / 1000
            resultado.value = f"Consumo: {consumo:.2f} kWh"
            page.update()
        except ValueError:
            resultado.value = "Entrada inválida"
            page.update()

    calcular_btn = ft.ElevatedButton("Calcular", on_click=calcular)

    page.add(
        potencia,
        tiempo,
        calcular_btn,
        resultado
    )

ft.app(target=main)