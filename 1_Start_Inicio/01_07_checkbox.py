import flet as ft


def main(page: ft.Page):
    # Criando uma aplicação to do com checkbox
    def adicionar_tarefa_clicada(e):
        txt_nova_tarefa = campo_texto_limpo.value
        campo_texto_limpo.value = ''
        page.add(
            ft.Checkbox(
                label=txt_nova_tarefa
            )
        )
    campo_texto_limpo = ft.TextField(
        hint_text="Qual tarefa deseja adicionar?", width=300
    )
    btn_adicionar_tarefa = ft.ElevatedButton('Adicionar', on_click=adicionar_tarefa_clicada)
    print(btn_adicionar_tarefa)

    page.add(
        ft.Row(
            [campo_texto_limpo, btn_adicionar_tarefa]
        )
    )


if __name__ == '__main__':
    ft.app(target=main)