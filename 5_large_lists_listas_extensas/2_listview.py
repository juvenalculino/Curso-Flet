import flet as ft

'''
Recomenda-se utilizar ListView e GridView

'''
def main(page: ft.Page):
    list_v = ft.ListView(
        expand=True,
        spacing=10
    )
    for i in range(5000):
        list_v.controls.append(
            ft.Text(
                f'Linha : {i}'
            )
        )
    page.add(list_v)

if __name__ == '__main__':
    ft.app(target=main)