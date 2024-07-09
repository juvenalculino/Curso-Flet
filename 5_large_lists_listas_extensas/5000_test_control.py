import flet as ft

'''
Para mostrar listas com muitos dados recomenda-se utilizar ListView w GridView

'''
def main(page: ft.Page):
    for i in range(5000):
        page.controls.append(
            ft.Text(
                f'Linha: {i}'
            )
        )
    page.scroll = 'always'
    page.update()
    

if __name__ == '__main__':
    ft.app(target=main)