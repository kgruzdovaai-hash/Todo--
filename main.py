import os
os.system('chcp 65001 >nul')  # Set console to UTF-8 for Russian support

from user import User
from project import Project
from task import Task
from tags import Tag
from comment import Comment

# Global data
users = []
projects = []
tags = []

class CLI:
    def __init__(self):
        pass

    def print_menu(self):
        print("\n" + "="*50)
        print("          СИСТЕМА УПРАВЛЕНИЯ ЗАДАЧАМИ")
        print("="*50)
        print("Доступные команды:")
        print("  1. Добавить пользователя")
        print("  2. Создать проект")
        print("  3. Добавить задачу")
        print("  4. Добавить тег")
        print("  5. Добавить комментарий")
        print("  6. Назначить задачу")
        print("  7. Добавить тег к задаче")
        print("  8. Отметить задачу как выполненную")
        print("  9. Показать пользователей")
        print(" 10. Показать проекты")
        print(" 11. Показать задачи проекта")
        print(" 12. Показать теги")
        print(" 13. Помощь")
        print(" 14. Выход")
        print("="*50)

    def get_input(self, prompt, validator=None):
        while True:
            try:
                value = input(prompt).strip()
                if validator:
                    value = validator(value)
                return value
            except EOFError:
                print("Ввод завершен. Выход из программы.")
                return None
            except KeyboardInterrupt:
                print("\nПрервано пользователем. Выход.")
                return None
            except Exception as e:
                print(f"Ошибка ввода: {e}. Попробуйте снова.")

    def validate_int(self, value):
        try:
            return int(value)
        except ValueError:
            raise ValueError("Введите число.")

    def validate_non_empty(self, value):
        if not value:
            raise ValueError("Поле не может быть пустым.")
        return value

    def add_user(self):
        name = self.get_input("Введите имя: ", self.validate_non_empty)
        if name is None: return
        email = self.get_input("Введите email: ", self.validate_non_empty)
        if email is None: return
        user_id = len(users) + 1
        user = User(user_id, name, email)
        users.append(user)
        print(f"Пользователь {user.name} добавлен с ID {user_id}.")

    def create_project(self):
        user_id = self.get_input("Введите ID пользователя: ", self.validate_int)
        if user_id is None: return
        user = find_user(user_id)
        if not user:
            print(f"Пользователь с ID {user_id} не найден.")
            return
        name = self.get_input("Введите название проекта: ", self.validate_non_empty)
        if name is None: return
        project_id = len(projects) + 1
        project = user.create_project(project_id, name)
        projects.append(project)
        print(f"Проект '{project.name}' создан с ID {project_id}.")

    def add_task(self):
        project_id = self.get_input("Введите ID проекта: ", self.validate_int)
        if project_id is None: return
        project = find_project(project_id)
        if not project:
            print(f"Проект с ID {project_id} не найден.")
            return
        name = self.get_input("Введите название задачи: ", self.validate_non_empty)
        if name is None: return
        description = self.get_input("Введите описание задачи: ", self.validate_non_empty)
        if description is None: return
        task_id = len([t for p in projects for t in p.tasks]) + 1
        task = project.add_task(task_id, name, description)
        print(f"Задача '{task.name}' добавлена в проект '{project.name}' с ID {task_id}.")

    def add_tag(self):
        name = self.get_input("Введите название тега: ", self.validate_non_empty)
        if name is None: return
        tag_id = len(tags) + 1
        tag = Tag(tag_id, name)
        tags.append(tag)
        print(f"Тег '{tag.name}' добавлен с ID {tag_id}.")

    def add_comment(self):
        task_id = self.get_input("Введите ID задачи: ", self.validate_int)
        if task_id is None: return
        user_id = self.get_input("Введите ID пользователя: ", self.validate_int)
        if user_id is None: return
        task = find_task(task_id)
        user = find_user(user_id)
        if not task:
            print(f"Задача с ID {task_id} не найдена.")
            return
        if not user:
            print(f"Пользователь с ID {user_id} не найден.")
            return
        text = self.get_input("Введите текст комментария: ", self.validate_non_empty)
        if text is None: return
        comment = task.add_comment(user, text)
        print(f"Комментарий добавлен к задаче '{task.name}'.")

    def assign_task(self):
        task_id = self.get_input("Введите ID задачи: ", self.validate_int)
        if task_id is None: return
        user_id = self.get_input("Введите ID пользователя: ", self.validate_int)
        if user_id is None: return
        task = find_task(task_id)
        user = find_user(user_id)
        if not task:
            print(f"Задача с ID {task_id} не найдена.")
            return
        if not user:
            print(f"Пользователь с ID {user_id} не найден.")
            return
        task.add_assignee(user)
        print(f"Пользователь {user.name} назначен на задачу '{task.name}'.")

    def tag_task(self):
        task_id = self.get_input("Введите ID задачи: ", self.validate_int)
        if task_id is None: return
        tag_id = self.get_input("Введите ID тега: ", self.validate_int)
        if tag_id is None: return
        task = find_task(task_id)
        tag = find_tag(tag_id)
        if not task:
            print(f"Задача с ID {task_id} не найдена.")
            return
        if not tag:
            print(f"Тег с ID {tag_id} не найден.")
            return
        task.add_tag(tag)
        print(f"Тег '{tag.name}' добавлен к задаче '{task.name}'.")

    def mark_done(self):
        task_id = self.get_input("Введите ID задачи: ", self.validate_int)
        if task_id is None: return
        task = find_task(task_id)
        if not task:
            print(f"Задача с ID {task_id} не найдена.")
            return
        task.mark_as_done()
        print(f"Задача '{task.name}' отмечена как выполненная.")

    def show_users(self):
        if not users:
            print("Нет пользователей.")
        else:
            for u in users:
                print(f"ID: {u.user_id}, Имя: {u.name}, Email: {u.email}")

    def show_projects(self):
        if not projects:
            print("Нет проектов.")
        else:
            for p in projects:
                print(f"ID: {p.project_id}, Название: {p.name}, Владелец: {p.owner.name}, Участники: {len(p.members)}, Задачи: {len(p.tasks)}")

    def show_tasks(self):
        project_id = self.get_input("Введите ID проекта: ", self.validate_int)
        if project_id is None: return
        project = find_project(project_id)
        if not project:
            print(f"Проект с ID {project_id} не найден.")
            return
        if not project.tasks:
            print("Нет задач в этом проекте.")
        else:
            for t in project.tasks:
                status = 'Выполнена' if t.is_done else 'В ожидании'
                assignees = [a.name for a in t.assignees]
                tags_list = [tg.name for tg in t.tags]
                print(f"ID: {t.task_id}, Название: {t.name}, Статус: {status}")
                print(f"  Описание: {t.description}")
                print(f"  Исполнители: {assignees}")
                print(f"  Теги: {tags_list}")
                print(f"  Комментарии: {len(t.comments)}")
                for c in t.comments:
                    print(f"    - {c.author.name}: {c.text}")

    def show_tags(self):
        if not tags:
            print("Нет тегов.")
        else:
            for t in tags:
                print(f"ID: {t.tag_id}, Название: {t.name}")

    def run(self):
        print("Добро пожаловать в систему управления задачами CLI")
        while True:
            self.print_menu()
            choice = self.get_input("Выберите номер команды: ", self.validate_int)
            if choice is None:
                break
            if choice == 1:
                self.add_user()
            elif choice == 2:
                self.create_project()
            elif choice == 3:
                self.add_task()
            elif choice == 4:
                self.add_tag()
            elif choice == 5:
                self.add_comment()
            elif choice == 6:
                self.assign_task()
            elif choice == 7:
                self.tag_task()
            elif choice == 8:
                self.mark_done()
            elif choice == 9:
                self.show_users()
            elif choice == 10:
                self.show_projects()
            elif choice == 11:
                self.show_tasks()
            elif choice == 12:
                self.show_tags()
            elif choice == 13:
                self.print_menu()
            elif choice == 14:
                print("До свидания!")
                break
            else:
                print("Неверный номер команды.")

def print_help():
    cli = CLI()
    cli.print_menu()

def find_user(user_id):
    return next((u for u in users if u.user_id == user_id), None)

def find_project(project_id):
    return next((p for p in projects if p.project_id == project_id), None)

def find_task(task_id):
    for p in projects:
        for t in p.tasks:
            if t.task_id == task_id:
                return t
    return None

def find_tag(tag_id):
    return next((t for t in tags if t.tag_id == tag_id), None)

def main():
    print("Добро пожаловать в систему управления задачами CLI")
    print_help()

    while True:
        try:
            cmd = input("\nВведите команду: ").strip().split()
            if not cmd:
                continue
            command = cmd[0].lower()

            if command == 'add_user':
                if len(cmd) < 3:
                    print("Добавить пользователя: add_user <имя> <email>")
                else:
                    user_id = len(users) + 1
                    user = User(user_id, cmd[1], ' '.join(cmd[2:]))
                    users.append(user)
                    print(f"User {user.name} added with ID {user_id}.")

            elif command == 'create_project':
                if len(cmd) < 3:
                    print("Usage: create_project <user_id> <name>")
                else:
                    user_id = int(cmd[1])
                    user = find_user(user_id)
                    if not user:
                        print(f"User with ID {user_id} not found.")
                    else:
                        project_id = len(projects) + 1
                        project = user.create_project(project_id, ' '.join(cmd[2:]))
                        projects.append(project)
                        print(f"Project '{project.name}' created with ID {project_id}.")

            elif command == 'add_task':
                if len(cmd) < 4:
                    print("Usage: add_task <project_id> <name> <description>")
                else:
                    project_id = int(cmd[1])
                    project = find_project(project_id)
                    if not project:
                        print(f"Project with ID {project_id} not found.")
                    else:
                        task_id = len([t for p in projects for t in p.tasks]) + 1
                        task = project.add_task(task_id, cmd[2], ' '.join(cmd[3:]))
                        print(f"Task '{task.name}' added to project '{project.name}' with ID {task_id}.")

            elif command == 'add_tag':
                if len(cmd) < 2:
                    print("Usage: add_tag <name>")
                else:
                    tag_id = len(tags) + 1
                    tag = Tag(tag_id, ' '.join(cmd[1:]))
                    tags.append(tag)
                    print(f"Tag '{tag.name}' added with ID {tag_id}.")

            elif command == 'add_comment':
                if len(cmd) < 4:
                    print("Usage: add_comment <task_id> <user_id> <text>")
                else:
                    task_id = int(cmd[1])
                    user_id = int(cmd[2])
                    task = find_task(task_id)
                    user = find_user(user_id)
                    if not task:
                        print(f"Task with ID {task_id} not found.")
                    elif not user:
                        print(f"User with ID {user_id} not found.")
                    else:
                        comment = task.add_comment(user, ' '.join(cmd[3:]))
                        print(f"Comment added to task '{task.name}'.")

            elif command == 'assign_task':
                if len(cmd) < 3:
                    print("Usage: assign_task <task_id> <user_id>")
                else:
                    task_id = int(cmd[1])
                    user_id = int(cmd[2])
                    task = find_task(task_id)
                    user = find_user(user_id)
                    if not task:
                        print(f"Task with ID {task_id} not found.")
                    elif not user:
                        print(f"User with ID {user_id} not found.")
                    else:
                        task.add_assignee(user)
                        print(f"User {user.name} assigned to task '{task.name}'.")

            elif command == 'tag_task':
                if len(cmd) < 3:
                    print("Usage: tag_task <task_id> <tag_id>")
                else:
                    task_id = int(cmd[1])
                    tag_id = int(cmd[2])
                    task = find_task(task_id)
                    tag = find_tag(tag_id)
                    if not task:
                        print(f"Task with ID {task_id} not found.")
                    elif not tag:
                        print(f"Tag with ID {tag_id} not found.")
                    else:
                        task.add_tag(tag)
                        print(f"Tag '{tag.name}' added to task '{task.name}'.")

            elif command == 'mark_done':
                if len(cmd) < 2:
                    print("Usage: mark_done <task_id>")
                else:
                    task_id = int(cmd[1])
                    task = find_task(task_id)
                    if not task:
                        print(f"Task with ID {task_id} not found.")
                    else:
                        task.mark_as_done()
                        print(f"Task '{task.name}' marked as done.")

            elif command == 'show_users':
                if not users:
                    print("No users.")
                else:
                    for u in users:
                        print(f"ID: {u.user_id}, Name: {u.name}, Email: {u.email}")

            elif command == 'show_projects':
                if not projects:
                    print("No projects.")
                else:
                    for p in projects:
                        print(f"ID: {p.project_id}, Name: {p.name}, Owner: {p.owner.name}, Members: {len(p.members)}, Tasks: {len(p.tasks)}")

            elif command == 'show_tasks':
                if len(cmd) < 2:
                    print("Usage: show_tasks <project_id>")
                else:
                    project_id = int(cmd[1])
                    project = find_project(project_id)
                    if not project:
                        print(f"Project with ID {project_id} not found.")
                    else:
                        if not project.tasks:
                            print("No tasks in this project.")
                        else:
                            for t in project.tasks:
                                status = 'Done' if t.is_done else 'Pending'
                                assignees = [a.name for a in t.assignees]
                                tags_list = [tg.name for tg in t.tags]
                                print(f"ID: {t.task_id}, Name: {t.name}, Status: {status}")
                                print(f"  Description: {t.description}")
                                print(f"  Assignees: {assignees}")
                                print(f"  Tags: {tags_list}")
                                print(f"  Comments: {len(t.comments)}")
                                for c in t.comments:
                                    print(f"    - {c.author.name}: {c.text}")

            elif command == 'show_tags':
                if not tags:
                    print("No tags.")
                else:
                    for t in tags:
                        print(f"ID: {t.tag_id}, Name: {t.name}")

            elif command == 'help':
                print_help()

            elif command == 'quit':
                print("Goodbye!")
                break

            else:
                print("Unknown command. Type 'help' for available commands.")

        except ValueError as e:
            print(f"Invalid input: {e}")
        except Exception as e:
            print(f"Ошибка: {e}")

if __name__ == "__main__":
    cli = CLI()
    cli.run()