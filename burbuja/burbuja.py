import flet as ft
import random
import time


def main(page: ft.Page):

    def create_containers(number: int):
        contianer_list = []
        for _ in range(number):
            contianer_list.append(
                ft.Container(
                    content=ft.Text(value=random.randint(1, 100)),
                    alignment=ft.alignment.center,
                    width=50,
                    height=50,
                    bgcolor=ft.colors.BLUE,
                    border_radius=25,
                )
            )
        return contianer_list

    row = ft.Row(controls=create_containers(10))
    page.add(row)

    time.sleep(1)

    arr = row.controls

    n: int = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            arr[j].bgcolor = ft.colors.GREEN
            arr[j + 1].bgcolor = ft.colors.GREEN
            time.sleep(0.5)
            page.update()
            if (int)(arr[j].content.value) > (int)(arr[j + 1].content.value):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            arr[j].bgcolor = ft.colors.BLUE
            arr[j + 1].bgcolor = ft.colors.BLUE
        arr[n - i - 1].bgcolor = ft.colors.AMBER

    page.update()


ft.app(target=main)
