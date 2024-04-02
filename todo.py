import flet
from flet import *
from datetime import datetime
import sqlite3


class FormContainer(UserControl):
    def __init__(self, func):
        self.func=func
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
                        on_click=self.func, 
                        style=ButtonStyle(
                            bgcolor={'': 'black'}, 
                            shape={'': RoundedRectangleBorder(radius=8),
                            },
                        ),
                    ),
                ],
            ),
        )

class CreateTask(UserControl):
    def __init__(self, task:str, date:str, func1, func2):
        self.task=task
        self.date=date
        self.func1 = func1
        self.func2 = func2
        super().__init__()

    def TaskDeleteEdit(self, nane, color, func):
        return IconButton(
            icon=nane,
            width=30,
            icon_size=18,
            icon_color=color,
            opacity=0,
            animate_opacity=200,
            on_click=lambda e: func(self.GetContinerInstance()),
        )
    
    def GetContinerInstance(self):
        return self

    def ShowIcons(self, e):
        if e.data == 'true':
            (
                e.control.content.controls[1].controls[0].opacity,
                e.control.content.controls[1].controls[1].opacity,
            ) = (1, 1)
            e.control.content.update()
        else:
            (
                e.control.content.controls[1].controls[0].opacity,
                e.control.content.controls[1].controls[1].opacity,
            ) = (0, 0)
            e.control.content.update()

    def build(self):
        return Container(
            width=280,
            height=60,
            border=border.all(0.85, 'white54'),
            border_radius=8,
            on_hover=lambda e: self.ShowIcons(e),
            clip_behavior=ClipBehavior.HARD_EDGE,
            padding=10,
            content=Row(
                alignment=MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    Column(
                        spacing=1,
                        alignment=MainAxisAlignment.CENTER,
                        controls=[
                            Text(value=self.task, size=10, weight='bold'),
                            Text(value=self.date, size=9, color='white54'),
                        ],
                    ),
                    Row(
                        spacing=0,
                        alignment=MainAxisAlignment.CENTER,
                        controls=[
                            self.TaskDeleteEdit(icons.DELETE_ROUNDED, 'red500', self.func1),
                            self.TaskDeleteEdit(icons.EDIT_ROUNDED, 'white70', self.func2),
                        ],                        
                    ),
                ],
            ),
        )

def main (page: Page):
    Page.horizontal_alignment='center'
    Page.vertical_alignment='center'

    def AddTaskToScreen(e):
        dateTime=datetime.now().strftime('%b - %d, %Y  %H:%M')
        if form.content.controls[0].value:
            _main_column_.controls.append(
                CreateTask(
                    form.content.controls[0].value,
                    dateTime,
                    DeleteFuntion,
                    UpdateFuntion,
                ),
            )
            _main_column_.update(),
 
            CreateToDoTask(e)
    
    def DeleteFuntion(e):
        _main_column_.controls.remove(e)
        _main_column_.update()

    def UpdateFuntion(e):
        form.height, form.opacity=200, 1
        (
            form.content.controls[0].value,
            form.content.controls[1].content.value,
            form.content.controls[1].on_click
        )=(
            e.controls[0].content.controls[0].controls[0].value,
            'Update',
            lambda _: FinalizeUpdate(e),
        )
        form.update()

    def FinalizeUpdate(e):
       e.controls[0].content.controls[0].controls[0].value = form.content.controls[0].value,
       e.controls[0].content.update(),
       CreateToDoTask(e),

    def CreateToDoTask(e):
        if form.height != 200:
            form.height, form.opacity=200, 1
            form.update()
        else:
            form.height, form.opacity=80, 0
            form.content.controls[0].value = None
            form.content.controls[1].content.value = 'Adicionar Texto'
            form.content.controls[1].on_click = lambda e: AddTaskToScreen(e)
            form.update()

    _main_column_=Column(
        scroll='hidden',
        expand=True,
        alignment=MainAxisAlignment.START,
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
                                FormContainer(lambda e: AddTaskToScreen(e)),
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