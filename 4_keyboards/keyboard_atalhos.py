import flet as ft

def main(page: ft.Page):
    

    def on_keyboard(e: ft.KeyboardEvent):
        page.add(
            ft.Text(
                f'Tecla: {e.key}, Shift: {e.shift}, CTRL: {e.ctrl}'
            )
        )

    page.on_keyboard_event = on_keyboard

    page.add(
        ft.Text('Combinação: (Tecla, Shift, Control)')
    )

if __name__ == '__main__':
    ft.app(target=main)