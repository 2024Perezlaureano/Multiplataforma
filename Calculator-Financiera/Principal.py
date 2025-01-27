import flet as ft

def calculadora_energetica(page):
    page.title = "Calculadora Energética"

    potencia = ft.TextField(label="Potencia (W)", value="0", keyboard_type=ft.KeyboardType.NUMBER)
    tiempo = ft.TextField(label="Tiempo (h)", value="0", keyboard_type=ft.KeyboardType.NUMBER)
    resultado = ft.Text("Consumo: 0 kWh", size=16)

    def calcular(e):
        try:
            p = float(potencia.value)
            t = float(tiempo.value)
            consumo = (p * t) / 1000
            resultado.value = f"Consumo: {consumo:.2f} kWh"
            page.update()
        except ValueError:
            resultado.value = "Entrada inválida. Ingrese números."
            page.update()

    calcular_btn = ft.ElevatedButton("Calcular", on_click=calcular, bgcolor=ft.colors.BLACK, color=ft.colors.WHITE)

    page.add(
        ft.Container(
            padding=20,
            content=ft.Column(
                [
                    ft.Text("Calculadora Energética", size=24, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                    potencia,
                    tiempo,
                    calcular_btn,
                    resultado,
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=15
            )
        )
    )


def calculadora_financiera(page):
    page.title = "Calculadora Financiera"
    page.theme_mode = ft.ThemeMode.LIGHT
    historial = []

    def calcular_interes_compuesto(e):
        try:
            principal = float(principal_input.value)
            tasa_interes = float(tasa_input.value) / 100
            tiempo = float(tiempo_input.value)
            monto_total = principal * (1 + tasa_interes) ** tiempo
            interes_generado = monto_total - principal
            resultado_text.value = f"Monto total: ${monto_total:.2f}\nInterés generado: ${interes_generado:.2f}"
            historial.append(resultado_text.value)
            page.update()
        except ValueError:
            resultado_text.value = "Entrada inválida. Ingrese números."
            page.update()

    def calcular_emi(e):
        try:
            principal = float(principal_input.value)
            tasa_interes = float(tasa_input.value) / 1200
            tiempo = float(tiempo_input.value) * 12
            emi = (principal * tasa_interes * (1 + tasa_interes) ** tiempo) / ((1 + tasa_interes) ** tiempo - 1)
            resultado_text.value = f"Cuota mensual (EMI): ${emi:.2f}"
            historial.append(resultado_text.value)
            page.update()
        except ValueError:
            resultado_text.value = "Entrada inválida. Ingrese números."
            page.update()

    def cambiar_tema(e):
        page.theme_mode = ft.ThemeMode.DARK if page.theme_mode == ft.ThemeMode.LIGHT else ft.ThemeMode.LIGHT
        page.update()

    def mostrar_historial(e):
        historial_text.value = "\n".join(historial)
        page.update()

    principal_input = ft.TextField(label="Monto Principal", width=300, border_radius=5, keyboard_type=ft.KeyboardType.NUMBER)
    tasa_input = ft.TextField(label="Tasa de Interés (%)", width=300, border_radius=5, keyboard_type=ft.KeyboardType.NUMBER)
    tiempo_input = ft.TextField(label="Tiempo (años)", width=300, border_radius=5, keyboard_type=ft.KeyboardType.NUMBER)

    calcular_interes_button = ft.ElevatedButton(text="Calcular Interés Compuesto", on_click=calcular_interes_compuesto, bgcolor=ft.colors.BLUE_ACCENT_700, color=ft.colors.WHITE)
    calcular_emi_button = ft.ElevatedButton(text="Calcular EMI", on_click=calcular_emi, bgcolor=ft.colors.BLUE_ACCENT_700, color=ft.colors.WHITE)
    cambiar_tema_button = ft.ElevatedButton(text="Cambiar Tema", on_click=cambiar_tema, bgcolor=ft.colors.BLUE_GREY_100, color=ft.colors.BLACK)
    mostrar_historial_button = ft.ElevatedButton(text="Mostrar Historial", on_click=mostrar_historial, bgcolor=ft.colors.BLUE_GREY_100, color=ft.colors.BLACK)

    resultado_text = ft.Text(value="", size=16)
    historial_text = ft.Text(value="", size=14)
    separador = ft.Divider(height=5, color=ft.colors.GREY_400)

    page.add(
        ft.Container(
            padding=20,
            content=ft.Column(
                [
                    ft.Text("Calculadora Financiera", size=24, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                    ft.Container(content=ft.Column([principal_input, tasa_input, tiempo_input], spacing=10), margin=ft.margin.only(bottom=20)),
                    ft.Row([calcular_interes_button, calcular_emi_button], alignment=ft.MainAxisAlignment.SPACE_AROUND),
                    cambiar_tema_button,
                    mostrar_historial_button,
                    separador,
                    resultado_text,
                    historial_text,
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=15
            )
        )
    )

def main(page: ft.Page):
    page.title = "Calculadoras"
    page.window_width = 450
    page.window_height = 700
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def tab_changed(e):
        page.update()

    tabs = ft.Tabs(
        expand=True,
        tabs=[
            ft.Tab(text="Energética", content=ft.Container(calculadora_energetica(page), padding=20)),
            ft.Tab(text="Financiera", content=ft.Container(calculadora_financiera(page), padding=20)),
        ],
        on_change=tab_changed,
    )
    page.add(tabs)

ft.app(target=main)