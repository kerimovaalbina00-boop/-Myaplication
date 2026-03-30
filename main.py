import flet as ft

def main_page(page: ft.Page):
    page.title = "Мое первое приложение"
    page.theme_mode = ft.ThemeMode.LIGHT
    count = 0
    text_counter = ft.Text(f"Нажато: {count} раз")
    text_hello = ft.Text ('Hello World')
    name_input = ft.TextField()


    def on_button_click(e):
        nonlocal count 
        count += 1
        text_counter.value = f"Нажато: {count} раз"
        page.update()



    elevated_button = ft.ElevatedButton('Send', icon=ft.Icons.SEND, color=ft.Colors.RED, icon_color=ft.Colors.GREEN, on_click=on_button_click)
    # text_button = ft.TextButton('send')
    # icon_button = ft.IconButton(icon=ft.Icons.SEND)

    page.add(text_hello, name_input, elevated_button, text_counter)
    

ft.app(main_page)
