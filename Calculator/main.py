import flet as ft


@ft.control
class CalcButton(ft.Button):
    expand: int = 1


@ft.control
class DigiButton(CalcButton):
    bgcolor: ft.Colors = ft.Colors.WHITE_24
    color: ft.Colors = ft.Colors.WHITE


@ft.control
class ActionButton(CalcButton):
    bgcolor: ft.Colors = ft.Colors.ORANGE
    color: ft.Colors = ft.Colors.WHITE


@ft.control
class ExtraActionButton(CalcButton):
    bgcolor: ft.Colors = ft.Colors.BLUE_GREY_100
    color: ft.Colors = ft.Colors.BLACK


@ft.control
class CalculatorApp(ft.Container):
    def __init__(self):
        super().__init__()
        self.width = 350
        self.bgcolor = ft.Colors.BLACK
        self.border_radius = ft.BorderRadius.all(20)
        self.padding = 20
        self.result = ft.Text(value="0", color=ft.Colors.WHITE, size=40)
        self.content = ft.Column(
            controls=[
                ft.Row(
                    controls=[self.result],
                    alignment=ft.MainAxisAlignment.END,
                ),
                ft.Row(
                    controls=[
                        ExtraActionButton(content="AC", on_click=self.button_clicked),
                        ExtraActionButton(content="+/-", on_click=self.button_clicked),
                        ExtraActionButton(content="%", on_click=self.button_clicked),
                        ActionButton(content="/", on_click=self.button_clicked),
                    ]
                ),
                ft.Row(
                    controls=[
                        DigiButton(content="7", on_click=self.button_clicked),
                        DigiButton(content="8", on_click=self.button_clicked),
                        DigiButton(content="9", on_click=self.button_clicked),
                        ActionButton(content="*", on_click=self.button_clicked),
                    ]
                ),
                ft.Row(
                    controls=[
                        DigiButton(content="4", on_click=self.button_clicked),
                        DigiButton(content="5", on_click=self.button_clicked),
                        DigiButton(content="6", on_click=self.button_clicked),
                        ActionButton(content="-", on_click=self.button_clicked),
                    ]
                ),
                ft.Row(
                    controls=[
                        DigiButton(content="1", on_click=self.button_clicked),
                        DigiButton(content="2", on_click=self.button_clicked),
                        DigiButton(content="3", on_click=self.button_clicked),
                        ActionButton(content="+", on_click=self.button_clicked),
                    ]
                ),
                ft.Row(
                    controls=[
                        DigiButton(content="0", expand=2, on_click=self.button_clicked),
                        DigiButton(content=".", on_click=self.button_clicked),
                        ActionButton(content="=", on_click=self.button_clicked),
                    ]
                ),
            ]
        )
    def button_clicked(self, e):
        data = e.control.content
        print(f"Button clicked whit data = {data}")
        if self.result.value == "Error" or data == "AC":
            self.result.value = "0"
            self.reset()
        
        elif data in("1","2","3","4","5","6","7","8","9","0","."):
            if self.result.value == "0" or self.new_operand:
                self.result.value = data
                self.new_operand = False
            else:
                self.result.value = self.result.value + data
        








def main(page: ft.Page):
    page.title = "Calculator"
    calc = CalculatorApp()
    page.add(calc)


ft.run(main)
