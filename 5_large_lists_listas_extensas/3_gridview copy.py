import flet as ft
import os

'''
Recomenda-se utilizar ListView e GridView

'''
os.environ['FLET_WS_MAX_MESSAGE_SIZE'] = '8000000'

def main(page: ft.Page):
    row = ft.Row(
        wrap=True, scroll='always', expand=True
    )
    page.add(row)

    for i in range(5000):
        row.controls.append(
            ft.Container(
                ft.Text(
                    f'Item: {i}'
                ),
                width=100,
                height=100,
                alignment=ft.alignment.center,
                bgcolor=ft.colors.AMBER_100,
                border=ft.border.all(1, ft.colors.AMBER_400),
                border_radius=ft.border_radius.all(5),
            )
        )
    page.update()

if __name__ == '__main__':
    ft.app(target=main)