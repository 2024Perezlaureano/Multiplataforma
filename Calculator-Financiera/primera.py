import flet as ft

def calculadora_energetica():
    potencia = ft.TextField(label="Potencia (W)", value="0", keyboard_type=ft.KeyboardType.NUMBER)
    tiempo = ft.TextField(label="Tiempo (h)", value="0", keyboard_type=ft.KeyboardType.NUMBER)
    resultado = ft.Text("Consumo: 0 kWh")
    error_text = ft.Text("", color=ft.colors.RED)

    def calcular(e):
        try:
            p = float(potencia.value)
            t = float(tiempo.value)
            if p < 0 or t < 0:
                raise ValueError("Los valores deben ser positivos")
            consumo = (p * t) / 1000
            resultado.value = f"Consumo: {consumo:.2f} kWh"
            error_text.value = ""
            page.update()
        except ValueError as ex:
            resultado.value = "Consumo: 0 kWh"
            error_text.value = str(ex) if "could not convert string to float" not in str(ex) else "Entrada inválida. Ingrese números."
            page.update()

    calcular_btn = ft.ElevatedButton("Calcular", on_click=calcular)

    return ft.Column([potencia, tiempo, calcular_btn, resultado, error_text], horizontal_alignment=ft.CrossAxisAlignment.CENTER, width=400)

def calculadora_financiera():
    principal_input = ft.TextField(label="Monto Principal", value="0", keyboard_type=ft.KeyboardType.NUMBER)
    tasa_input = ft.TextField(label="Tasa de Interés (%)", value="0", keyboard_type=ft.KeyboardType.NUMBER)
    tiempo_input = ft.TextField(label="Tiempo (años)", value="0", keyboard_type=ft.KeyboardType.NUMBER)
    resultado_text = ft.Text(value="", size=20)
    historial_text = ft.Text(value="", size=20)
    historial = []
    error_text = ft.Text("", color=ft.colors.RED)

    def calcular_interes_compuesto(e):
        try:
            principal = float(principal_input.value)
            tasa_interes = float(tasa_input.value) / 100
            tiempo = float(tiempo_input.value)
            if principal < 0 or tasa_interes < 0 or tiempo < 0:
                raise ValueError("Los valores deben ser positivos")
            monto_total = principal * (1 + tasa_interes) ** tiempo
            interes_generado = monto_total - principal
            resultado_text.value = f"Monto total: ${monto_total:.2f}\nInterés generado: ${interes_generado:.2f}"
            error_text.value = ""
            historial.append(resultado_text.value)
            page.update()
        except ValueError as ex:
            resultado_text.value = ""
            error_text.value = str(ex) if "could not convert string to float" not in str(ex) else "Entrada inválida. Ingrese números."
            page.update()

    def calcular_emi(e):
        try:
            principal = float(principal_input.value)
            tasa_interes = float(tasa_input.value) / 1200  # Tasa mensual
            tiempo = float(tiempo_input.value) * 12  # Meses
            if principal < 0 or tasa_interes < 0 or tiempo < 0:
                raise ValueError("Los valores deben ser positivos")
            emi = (principal * tasa_interes * (1 + tasa_interes) ** tiempo) / ((1 + tasa_interes) ** tiempo - 1)
            resultado_text.value = f"Cuota mensual (EMI): ${emi:.2f}"
            error_text.value = ""
            historial.append(resultado_text.value)
            page.update()
        except ValueError as ex:
            resultado_text.value = ""
            error_text.value = str(ex) if "could not convert string to float" not in str(ex) else "Entrada inválida. Ingrese números."
            page.update()

    def cambiar_tema(e):
        page.theme_mode = ft.ThemeMode.DARK if page.theme_mode == ft.ThemeMode.LIGHT else ft.ThemeMode.LIGHT
        page.update()

    def mostrar_historial(e):
        historial_text.value = "\n".join(historial)
        page.update()

    calcular_interes_button = ft.ElevatedButton(text="Calcular Interés Compuesto", on_click=calcular_interes_compuesto)
    calcular_emi_button = ft.ElevatedButton(text="Calcular EMI", on_click=calcular_emi)
    cambiar_tema_button = ft.ElevatedButton(text="Cambiar Tema", on_click=cambiar_tema)
    mostrar_historial_button = ft.ElevatedButton(text="Mostrar Historial", on_click=mostrar_historial)

    return ft.Column(
        [
            ft.Text("Calculadora Financiera", size=30, weight=ft.FontWeight.BOLD),
            principal_input,
            tasa_input,
            tiempo_input,
            calcular_interes_button,
            calcular_emi_button,
            cambiar_tema_button,
            mostrar_historial_button,
            resultado_text,
            historial_text,
            error_text
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        width=400
    )


def main(page: ft.Page):
    page.title = "Calculadoras"
    page.theme_mode = ft.ThemeMode.LIGHT #establece el tema claro por defecto

    def tab_changed(e):
        page.update()

    tabs = ft.Tabs(
        expand=True,
        tabs=[
            ft.Tab(text="Energética", content=calculadora_energetica()),
            ft.Tab(text="Financiera", content=calculadora_financiera()),
        ],
        on_change=tab_changed,
    )

    page.add(tabs)

ft.app(target=main)