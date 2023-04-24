from data_base import load_notes, save_notes
from functions import add_note, edit_note, delete_note, filter_notes, get_index, get_datatime
from view import list_notes, show_note, menu_printing


def notes():
    file = 'notes.json'
    notes_param = load_notes(file)
    while True:
        menu_printing()
        cmd = input('\nВыберите команду: ')
        if cmd == '1':
            list_notes(notes_param)
        elif cmd == '2':
            notes_param.append(add_note())
            save_notes(file, notes_param)
            print('Заметка добавлена')
        elif cmd == '3':
            index = get_index(notes_param, 'редактирования')
            edit_note(notes_param, index)
            save_notes(file, notes_param)
        elif cmd == '4':
            index = get_index(notes_param, 'удаления')
            delete_note(notes_param, index)
            save_notes(file, notes_param)
        elif cmd == '5':
            index = get_index(notes_param, 'просмотра')
            show_note(notes_param, index)
        elif cmd == '6':
            if notes_param:
                start_date = get_datatime('Начальная дата для поиска:')
                end_date = get_datatime('Конечная дата для поиска:')
                filtered_notes = filter_notes(notes_param, start_date, end_date)
                list_notes(filtered_notes)
            else:
                print('Список заметок пуст')
        elif cmd == '7':
            break
