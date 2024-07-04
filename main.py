
import flet as ft
import google.generativeai as genai


class PageContent(ft.Container):
    def __init__(self, page:ft.Page):
        super().__init__()
        self.page = page
        
        self.chat_log = ft.Container(content=ft.Column(controls=[],scroll=ft.ScrollMode.HIDDEN),expand=True)

        self.chat_content = ft.Container(
            content=ft.Column(
                controls=[
                    self.chat_log,
                    ft.Container(content=ft.TextField(hint_text="chat",on_submit=self.on_submit_chat),height=50)
                ],
            ),
            expand=True
        )



        self.expand =True
        self.content = ft.Row(
            controls=[
                self.chat_content,
                ft.VerticalDivider(),
                ft.Container(bgcolor=ft.colors.RED,width=400)
            ]
        )

    def on_submit_chat(self,e):
        rect = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text(value="Test User",size=15),
                    ft.Text(value=e.control.value, size=20)
                ]
            ),
            border=ft.border.all(width=1),
            border_radius=10,
            padding=ft.padding.all(value=5)
        )
        self.chat_log.content.controls.append(rect)
        e.control.value = ""
        e.control.update()
        self.chat_log.update()

def main(page:ft.Page):
    
    page.title = "test"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.theme_mode = "light"
    
    # page.go("/Page_content")
    page.add(PageContent(page=page))

ft.app(target=main)



