import flet as ft


def main(page: ft.Page):
    # Criar um botão
    txt_first_name = ft.Ref[ft.TextField]()
    txt_last_name = ft.Ref[ft.TextField]()
    col_controles = ft.Ref[ft.Column]()


    def saudar_click(e):
        col_controles.current.controls.append(
            ft.Text(f'Olá, {txt_first_name.current.value} {txt_last_name.current.value}!'
                )
            )
        txt_first_name.current.value = ''
        txt_last_name.current.value = ''

        page.update()
        txt_first_name.current.focus()


    btn_saudar = ft.ElevatedButton('Saudar', on_click=saudar_click)


    
    page.add(
        ft.TextField(ref=txt_first_name, label='Nome', autofocus=True),
        ft.TextField(ref=txt_last_name, label='Apelido', autofocus=True),
        btn_saudar,
        ft.Column(ref=col_controles)
    )


if __name__ == '__main__':
    ft.app(target=main)