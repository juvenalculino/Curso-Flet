import flet as ft



def main(page: ft.Page):
    btn_action = ft.ElevatedButton('Click')
    page.add(btn_action)


if __name__ == '__main__':
    ft.app(target=main)