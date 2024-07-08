import flet as ft



def main(page: ft.Page):
    # Vamos criar um controle para representar um texto
    texto = ft.Text(value='Olá mundo, meu nome é Juvenal!', color=ft.colors.BLACK, bgcolor=ft.colors.RED)  
    page.controls.append(texto) 
    page.update()


ft.app(target=main)
