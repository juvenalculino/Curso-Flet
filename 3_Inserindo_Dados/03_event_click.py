import flet as ft

def main(page: ft.Page):
    page.title = 'Contador'
    page.vertical_alignment = 'center'
    
    

    def btn_clicked(e):
        if not txt_name.value:
            txt_name.error_text = "Por favor, digite seu nome!"
            page.update()
        else:
            name = txt_name.value
            page.clean()
            page.add(ft.Text(f'Olá, {name}'))

    txt_name = ft.TextField(
        label='Seu nome'
    )
    page.add(txt_name, ft.ElevatedButton('Say hello!', on_click=btn_clicked))


if __name__ == '__main__':
    ft.app(target=main)