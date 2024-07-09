import flet as ft

def main(page: ft.Page):
    

    def submit_clicked(e):
        lbl_result.value = f'O valor do dropdown é: {cbx_color.value}'
        page.update()
    
    lbl_result = ft.Text()

    btn_submit = ft.ElevatedButton(
        text='Submit',
        on_click=submit_clicked
    )

    cbx_color = ft.Dropdown(
        width=100,
        options=[
            ft.dropdown.Option('RED'),
            ft.dropdown.Option('GREEN'),
            ft.dropdown.Option('BLUE'),
        ]
    )

    page.add(
        cbx_color,
        btn_submit,
        lbl_result
    )

if __name__ == '__main__':
    ft.app(target=main)