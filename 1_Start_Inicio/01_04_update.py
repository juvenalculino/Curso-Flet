import flet as ft
import time


def main(page: ft.Page):
    # Alterar o estado de um controle de texto e refletir seu estado com o método update()
    lbl_texto = ft.Text()  
    page.add(lbl_texto) 
    for i in range(10):
        lbl_texto.value = f'Passo: {i}'
        page.update()
        time.sleep(1)  # Simulando um delay para demonstrar a atualização dinâmica
    print(page.controls[0].value) # Olá mundo, meu nome é Juvenal!
    page.update()


ft.app(target=main)
