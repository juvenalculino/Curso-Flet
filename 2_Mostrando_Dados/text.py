import flet as ft


def main(page: ft.Page):
    lbt_text = ft.Text(
        value='Flat e Python!',
        size=30,
        color='Green',
        bgcolor=ft.colors.AMBER_200,
        weight='bold',
        italic=True
    )

    page.add(lbt_text)


if __name__ == '__main__':
    ft.app(target=main)
    