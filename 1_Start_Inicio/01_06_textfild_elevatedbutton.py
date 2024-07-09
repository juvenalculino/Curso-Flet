import flet as ft
import time


def main(page: ft.Page):
    # Para mostrar o nome na tela precisamos Indicar o objeto textfield dentro de uma variavel
    txt_nome = ft.TextField(label='Digite seu nome: ')

    lbl_saudar = ft.Text()
    

    def saudar(e):
        # Podemos passar o value diretamente e utilizar o page.update para mostrar na tela
        lbl_saudar.value = f'Olá - {txt_nome.value}'
        page.update()

    row = ft.Row(
        controls=[
            # Passando o objeto
            txt_nome,
            ft.ElevatedButton(text='Saudação', on_click=saudar),
            lbl_saudar,
        ]
    )

    page.add(row)
    


ft.app(target=main)
