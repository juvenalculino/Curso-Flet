import flet as ft
import time


def main(page: ft.Page):
    # Controles que servem como contêineres para outros controles – classe de linha
    
    """row_dados = ft.Row(
        controls=[
            ft.Text('Python'),
            ft.Text('Flet'),
            ft.Text('Flutter'),
        ]
    )
    page.add(row_dados)"""

    ## Podemos utilizar uma lista
    linguagens = ['Python', 'Flet', 'Flutter']
    etiquetas = []
    for e in linguagens:
        etiquetas.append(ft.Text(e))
    
    row_dados = ft.Row(controls=etiquetas)
    page.add(row_dados)


ft.app(target=main)
