Что попросил:
                Ты — опытный backend‑разработчик на Python.
                Я проектирую систему управления задачами на Python с использованием ООП, с модульной архитектурой. Вот архитектура на русском языке:

                Основные классы: User, Project, Task, Tag, Comment

                Атрибуты классов:
                - У класса User есть user_id, name, email, projects.
                - У класса Project есть project_id, name, tasks, members, owner.
                - У класса Task есть task_id, name, discription, is_done, due_date, priority, project, assignees, tags, comments.
                - У класса Tags есть tag_id, name.
                - У класса Comment есть comment_id, author, task, text, created_ad

                Методы классов:
                - Класс User имеет методы create_project, delet_project, get_project, join_project, leave_project.
                - Класс Project имеет методы add_task, remove_task, get_tasks, rename, add_member, remove_member, get_members.
                - Класс Task имеет методы mark_as_done, mark_as_undone, change_description, change_due_date, change_priority, rename, add_assignee, remove_assignee, add_tag, remove_tag, add_comment,get_comments.
                - Класс Tag имеет метод rename
                - Класс Comment имеет методы edit, delete.

                Взаимодействие объектов:
                - Объект User создает и владеет несколькими объектами Project 
                - Объект Project содержит в себе список объектов Task, members
                - Объект Task может иметь несколько исполнителей assignees, tags, comments
                - Comment принадлежит задаче и имеет автора.
                - Tag может быть общей сущностью или уникальной для пользователя/проекта (уточняется при реализации).

                
                Система строится на пяти основных классах (User, Project, Task, Tag, Comment), каждый из которых имеет чётко определённые атрибуты и методы. Классы связаны отношениями: User — Project (многие ко многим), Project — Task (один ко многим), Task — Tag/Comment/User (многие ко многим). 
                Система поддерживает совместную работу, метки, комментарии и расширяемость.

                напиши полный код на Python, реализующий эту архитектуру. Создай классы в отдельных файлах, которые я описал, с атрибутами и методами. В конце файла добавь пример создания нескольких объектов и вызова их методов, чтобы продемонстрировать работу системы.

                Создай проект со структурой папок и файлов, похожей на пример ниже (названия можно адаптировать, но смысл должен сохраниться):
                ● main.py — точка входа.
                ● config.py — классы конфигурации.
                ● requirements.txt — список зависимостей проекта.
                ● README.md — краткое описание проекта и инструкции по запуску.

                Добавь инструкции для запуска виртуального окружения

                нужен CLI-меню для действий: добавление пользователя, задачи, проекта и т.д. с валидацией ввода и красивым текстовым меню.
                Раздели бизнес-логику и интерфейс:  Логика классов — отдельно, CLI — в main.py.

Что получил:
        В терминале вывелась такая инфа
                === Task Management System Demo ===
                Project: Task Management System
                Owner: Alice
                Members: ['Alice', 'Bob']
                Tasks: 2
                - Design architecture: Done
                Assignees: ['Alice', 'Bob']
                Tags: ['urgent']
                Comments: 2
                - Alice: This is a critical task
                - Bob: I agree, let's prioritize this
                - Implement classes: Pending
                Assignees: ['Alice']
                Tags: ['feature']
                Comments: 0

Что исправил: 
                1.  ИИ забыл добавить в инструкцию запуск виртуально окружения. Решение -Попросила чтобы ИИ  сам запустил виртуальное окружение
                2.  были ошибки такого плана 
                Traceback (most recent call last):
                File "E:\ИИ\!Учеба\Project\VPb04_Todo_list\main.py", line 58, in <module>
                main()
                File "E:\ИИ\!Учеба\Project\VPb04_Todo_list\main.py", line 20, in main
                task1 = project.add_task(1, "Design architecture", "Design the system architecture")
                File "E:\ИИ\!Учеба\Project\VPb04_Todo_list\project.py", line 10, in add_task
                task = Task(task_id, name, description, self, due_date, priority)
                NameError: name 'Task' is not defined. Did you mean: 'task'?

                Решение - Выбрала файл main.py и спросила у ИИ что нужно исправить в этом файле чтобы он запустился. 

                3. Добавила промпт Сделай так чтобы через терминал можно было добавлять записи

                4. Сделай CLI-меню для действий: добавление пользователя, задачи, проекта и т.д. с валидацией ввода и красивым текстовым меню.
