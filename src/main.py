from src.TaskSources.file_task import FileTaskSource
from src.TaskSources.task_generator import TaskGenerator
from src.TaskSources.api_task import ApiTaskSource
from src.recieve_tasks import receive
from src.exceptions.file_task_source_exceptions import TaskSourceError

def main() -> None:
    tasks = []
    while True:
        print("\n1 - Прочитать задачу из файла\n"
              "2 - Сгенерировать задачи\n"
              "3 - API заглушка\n"
              "4 - Увидеть задачи\n"
              "5 - Выход\n")
        try:
            variant = int(input("Выберите пункт: "))
        except ValueError:
            print("Ошибка: введите число.")
            continue

        try:
            if variant == 1:
                filename = input("Укажите файл: ")
                src = FileTaskSource(filename)
                tasks.extend(receive(src))

            elif variant == 2:
                num = int(input("Укажите количество задач: "))
                src = TaskGenerator(num)
                tasks.extend(receive(src))

            elif variant == 3:
                num = int(input("Укажите количество задач для API: "))
                src = ApiTaskSource(tasks_count=num, simulate_delay=True)
                tasks.extend(receive(src))

            elif variant == 4:
                for t in tasks:
                    print(f"{t.id}: {t.payload}")

            elif variant == 5:
                break

            else:
                print(f"Неверный пункт меню: {variant}")

        except TaskSourceError as e:
            print(f"Ошибка источника: {e}")
        except Exception as e:
            print(f"Неожиданная ошибка: {e}")

if __name__ == "__main__":
    main()