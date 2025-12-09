 <!-- ## Спроектировать систему управления задачами (Todo-лист) с использованием ООП. -->
 <!-- ## Todo-лист — это список задач, которые нужно сделать. -->

Основные классы: User, Project, Task, Tags, Comment

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
- Класс Tags имеет метод rename
- Класс Comment имеет методы edit, delete.

 Взаимодействие объектов:
 - Объект User создает и владеет несколькими объектами Project 
 - Объект Project содержит в себе список объектов Task, members
 - Объект Task может иметь несколько исполнителей assignees, tags, comments
 - Comment принадлежит задаче и имеет автора.
 - Tag может быть общей сущностью или уникальной для пользователя/проекта (уточняется при реализации).

 
Система строится на пяти основных классах (User, Project, Task, Tag, Comment), каждый из которых имеет чётко определённые атрибуты и методы. Классы связаны отношениями: User — Project (многие ко многим), Project — Task (один ко многим), Task — Tag/Comment/User (многие ко многим). 
Система поддерживает совместную работу, метки, комментарии и расширяемость.
