import flet as ft

def main(page: ft.Page):
    page.title = "Calculadora TAP"
    page.window_width = 250
    page.window_height = 500 
    page.padding = 20

    # 1. El display de texto
    texto_display = ft.Text(value="0", size=30)
    display = ft.Container(
        content=texto_display,
        bgcolor=ft.Colors.BLACK12,
        border_radius=8,
        alignment=ft.Alignment(1, 0), 
        padding=10,
        width=210,
        height=70,
    )

    # 2. Función para escribir números (1 al 5)
    def escribir_numero(e):
        if texto_display.value == "0":
            texto_display.value = str(e.control.data)
        else:
            texto_display.value += str(e.control.data)
        page.update()

    # 3. Función para limpiar pantalla
    def borrar_pantalla(e):
        texto_display.value = "0"
        page.update()

    grid = ft.GridView(
        runs_count=2,
        spacing=10,
        width=210,
        height=320, 
    )

    # 4. Lista de botones numéricos (Incluyendo el 5)
    config = [
        ("1", ft.Colors.BLUE),
        ("2", ft.Colors.GREEN),
        ("3", ft.Colors.ORANGE),
        ("4", ft.Colors.RED),
        ("5", ft.Colors.PURPLE), # Nuevo botón para llenar el hueco
    ]

    for num, col in config:
        grid.controls.append(
            ft.FilledButton(
                content=ft.Text(num),
                data=num,
                on_click=escribir_numero,
                style=ft.ButtonStyle(
                    bgcolor=col,
                    shape=ft.RoundedRectangleBorder(radius=8),
                ),
            )
        )

    # 5. Botón de Borrar (C) al final
    grid.controls.append(
        ft.FilledButton(
            content=ft.Text("C", color=ft.Colors.WHITE),
            on_click=borrar_pantalla,
            style=ft.ButtonStyle(
                bgcolor=ft.Colors.BLACK,
                shape=ft.RoundedRectangleBorder(radius=8),
            ),
        )
    )

    page.add(
        ft.Column(
            controls=[display, grid],
            tight=True
        )
    )

if __name__ == "__main__":
    ft.app(target=main)