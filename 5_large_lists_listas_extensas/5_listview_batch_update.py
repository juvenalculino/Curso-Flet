import flet as ft


def main(page: ft.Page):
    lv_texto = ft.ListView(
        expand=1,
        spacing=10,
        item_extent=50
    )
    page.add(lv_texto)

    for i in range(5000):
        lv_texto.controls.append(
            ft.Text(
                f'Item: {i}'
            )
        )
        # Vamos realizar uma atualização quando o valor de i com o resto = 0
        if i % 500 == 0:
            page.update()
    page.update()



if __name__ == '__main__':
    ft.app(target=main)