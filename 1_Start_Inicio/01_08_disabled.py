import flet as ft


def main(page: ft.Page):
    txt_first_name = ft.TextField()
    txt_last_name = ft.TextField()

    # Propriedade disabled  atribuído de forma individual:
    txt_first_name.disabled = True
    txt_last_name.disabled = True

    # Propriedade disabled atribuída em uma lista de controles:
    col_controles = ft.Column(
        controls=[
            txt_first_name,
            txt_last_name
        ]
    )

    page.add(
        col_controles
    )

if __name__ == '__main__':
    ft.app(target=main)