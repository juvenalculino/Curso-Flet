import os
import flet as ft


os.environ['FLET_WS_MAX_MESSAGES_SIZE'] = '80000000'
def main(page: ft.Page):
    gv_dados = ft.GridView(expand=True, max_extent=150, child_aspect_ratio=1)
    page.add(gv_dados)


    for i in range(5000):
        gv_dados.controls.append(
            ft.Container(
                ft.Text(
                    f'Item: {i}'
                ),
                alignment=ft.alignment.center,
                bgcolor=ft.colors.AMBER_200,
                border=ft.border.all(1, ft.colors.AMBER_400),
                border_radius=ft.border_radius.all(5)
            )
        )
    page.update()


if __name__ == '__main__':
    ft.app(target=main)