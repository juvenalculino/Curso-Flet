import flet as ft


def main(page: ft.Page):
    # Criar um botão
    txt_first_name = ft.TextField(label='Nome', autofocus=True)
    txt_last_name = ft.TextField(label='Apelido', autofocus=True)
    col_controles = ft.Column()


    def saudar_click(e):
        col_controles.controls.append(ft.Text(
                f'Olá {txt_first_name.value} {txt_last_name.value}!'
                )
            )
        txt_first_name.value = ''
        txt_last_name.value = ''

        page.update()
        #txt_first_name.focus()


    btn_saudar = ft.ElevatedButton('Saudar', on_click=saudar_click)


    
    page.add(
        txt_first_name,
        txt_last_name,
        btn_saudar,
        col_controles
    )


if __name__ == '__main__':
    ft.app(target=main)