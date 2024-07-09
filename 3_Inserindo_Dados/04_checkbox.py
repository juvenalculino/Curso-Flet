import flet as ft

def main(page: ft.Page):
    page.title = 'Contador'
    page.vertical_alignment = 'center'
    
    
    

    def checkbox_changed(e):
        lbl_result.value = f'Estou aprendendo a programar! {chk_area.value}'
        page.update()

    lbl_result = ft.Text()

    chk_area = ft.Checkbox(
        label='Aprender a programar em Python',
        value=False,
        on_change=checkbox_changed
    )

    page.add(chk_area, lbl_result)

if __name__ == '__main__':
    ft.app(target=main)