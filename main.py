import flet  as ft 

def main(page: ft.Page):
    page.title = "Meu Primeiro app Flet" 
    page.bgcolor = "#9dcdfa"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.add(
        ft.Text(value="Ana Júlia"),
        ft.ElevatedButton("Clique Aqui"),
    )

ft.run(main)
