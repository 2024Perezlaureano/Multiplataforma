import flet as ft

def main(page: ft.Page):
    page.title = "Lista de Tareas"

    tasks = []  # Lista para almacenar las tareas
    new_task = ft.TextField(hint_text="Nueva tarea", expand=True)

    def add_task(e):
        if new_task.value:
            tasks.append(
                ft.Row(
                    [
                        ft.Checkbox(on_change=task_checked),
                        ft.Text(new_task.value, expand=True),
                        ft.IconButton(
                            ft.icons.DELETE,
                            on_click=delete_task,
                            data=new_task.value,  # Pasar el texto de la tarea como dato
                        ),
                    ],
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                )
            )
            new_task.value = ""
            update_tasks()

    def delete_task(e):
        for task in tasks[:]: # Iterar sobre una copia de la lista para evitar errores de modificación durante la iteración
            if isinstance(task,ft.Row) and task.controls[1].value == e.control.data: #verifica que sea una fila y compara el valor del texto
                tasks.remove(task)
        update_tasks()

    def task_checked(e):
        for task in tasks:
            if isinstance(task,ft.Row) and task.controls[0] == e.control:
                task.controls[1].strike = e.control.value
                break
        update_tasks()

    def update_tasks():
        page.controls.pop()
        page.add(
            ft.Column(
                [
                    ft.Row(
                        [
                            new_task,
                            ft.ElevatedButton("Agregar tarea", on_click=add_task),
                        ]
                    ),
                    ft.Column(tasks),
                ]
            )
        )
        page.update()

    update_tasks()

ft.app(target=main)