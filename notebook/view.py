# from textwrap import wrap


# def list_notes(notes):
#     # вывод списка заметок на экран
#     if len(notes) == 0:
#         print('Список заметок пуст')
#     else:
#         for i, note in enumerate(notes):
#             print(f"| {i } | {note} | {note} | {note}")


# def show_note(notes, index):
#     # вывод одной заметки
#     try:
#         note = notes[index]
#         txt = note['body']
#         print(f"\n{'Заголовок':<13s}: {note['title']}")
#         print(f"{'Дата записи':<13s}: {note['date']}")
#         print(f"{'Текст заметки':<13s}: ")
#         line_break(txt)
#     except TypeError:
#         print('\nЗапись отсутствует')


# def line_break(text):
#     # печать текста заметки по строкам
#     lines = wrap(text, width=120)
#     x = 0
#     while len(lines) > x:
#         print(lines[x])
#         x += 1


# def menu_printing():
#     # вывод меню команд
#     print('\n1 - Посмотреть все заметки')
#     print('2 - Добавить заметку')
#     print('3 - Редактировать заметку')
#     print('4 - Удалить заметку')
#     print('5 - Посмотреть одну заметку')
#     print('6 - Поиск заметок по дате')
#     print('7 - Выход')
