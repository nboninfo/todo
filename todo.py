import flet
from flet import *
from datetime import datetime
import sqlite3


class FormContainer(UserControl):
    def __init__(self):
        super().__init__()

    def build(self):
        return Container(
            width=280,
            height=80,
            bgcolor='bluegrey500',
            opacity=0,
            border_radius=40,
            margin=margin.only(left=-20, right=-20),
            animate=animation.Animation(400, 'decelerate'),
            animate_offset=200,
            padding=padding.only(top=45, bottom=45),
            content=Column(
                horizontal_alignment=CrossAxisAlignment.CENTER,
                controls=[
                    TextField(
                        height=48,
                        width=255,
                        filled=True,
                        text_size=12,
                        border_color='transparent',
                        hint_text='Descrição...',
                        hint_style=TextStyle(size=11),
                    ),
                    IconButton(
                        content=Text('Adicionar Tarefa'), 
                        width=180, 
                        height=44, 
                        style=ButtonStyle(
                            bgcolor={'': 'black'}, 
                            shape={'': RoundedRectangleBorder(radius=8),
                            },
                        ),
                    ),
                ],
            ),
        )


def main (page: Page):
    Page.horizontal_alignment='center'
    Page.vertical_alignment='center'

    def CreateToDoTask(e):
        if form.height != 200:
            form.height, form.opacity=200, 1
            form.update()
        else:
            form.height, form.opacity=80, 0
            form.update()

    _main_column_=Column(
        scroll='hidden',
        expand=True,
        alignment=MainAxisAlignment.CENTER,
        controls=[
            Row(
                alignment=MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    Text('Lista TODO', size=18, weight='bold'),
                    IconButton(
                        icons.ADD_CIRCLE_ROUNDED, icon_size=18, on_click=lambda e: CreateToDoTask(e)
                    ),
                ],
            ),
            Divider(height=8, color='white24'),          
        ],
    )

    page.add(
        Container(
            width=1500,
            height=800,
            margin=-10,
            bgcolor='bluegrey900',
            alignment=alignment.center,
            content=Row(
                alignment=MainAxisAlignment.CENTER,
                vertical_alignment=CrossAxisAlignment.CENTER,
                controls=[
                    Container(
                        width=280,
                        height=600,
                        bgcolor='#0f0f0f',
                        border_radius=40,
                        border=border.all(0.5, 'white'),
                        padding=padding.only(top=35, left=20, right=20),
                        clip_behavior=ClipBehavior.HARD_EDGE,
                        content=Column(
                            alignment=MainAxisAlignment.CENTER,
                            expand=True,
                            controls=[
                                _main_column_,
                                FormContainer(),
                            ],
                        ),
                    )
                ],
            ),
        )
    )
    page.update()

    form=page.controls[0].content.controls[0].content.controls[1].controls[0]



if  __name__=='__main__':
    flet.app(target=main)