import flet as ft

def main(page: ft.Page):
    page.title = 'Contador'
    page.vertical_alignment = 'center'
    
    txt_numero = ft.TextField(
        value='0',
        text_align='right',
        width=150
    )

    def reduzir_click(e):
        txt_numero.value = int(txt_numero.value) - 1
        page.update()
    
    def aumentar_click(e):
        txt_numero.value = int(txt_numero.value) + 1
        page.update()

    page.add(
        ft.Row(
            [
            ft.IconButton(ft.icons.REMOVE, on_click=reduzir_click),
            txt_numero,
            ft.IconButton(ft.icons.ADD, on_click=aumentar_click),
            ],
            alignment='center'
        )
    )


if __name__ == '__main__':
    ft.app(target=main)