import flet as ft 


def main(page: ft.Page):
    page.title = 'Contador com FLET'.upper()
    page.vertical_alignment='center'

    txt_number = ft.TextField(
        value='0',
        text_align='right',
        width=100,
        bgcolor=ft.colors.RED_300,
    )

    def click_menos(e):
        print(e.control)
        txt_number.value = int(txt_number.value) - 1
        page.update()
    

    def click_mais(e):
        txt_number.value = int(txt_number.value) + 1
        page.update()
        

    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.REMOVE, on_click=click_menos),
                txt_number,  # Contador na tela
                ft.IconButton(ft.icons.ADD, on_click=click_mais),
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

ft.app(target=main)