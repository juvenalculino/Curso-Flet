import flet as ft
import time


def saudacao(e):
    print('Olá, mundo!')
    

def main(page: ft.Page):
    # Capturando nome de uma pessoa com TextFild e ElevatedButton. Os dados setrão mostrados no terminal.
    row = ft.Row(
        controls=[
            ft.TextField(label='Digite seu nome: '),
            ft.ElevatedButton(text='Saudação', on_click=saudacao),
        ]
    )

    page.add(row)
    


ft.app(target=main)
