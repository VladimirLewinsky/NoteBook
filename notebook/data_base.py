import json


def load_notes(file):
    # загрузка заметок из файла в список
    try:
        with open(file) as f:
            notes = json.load(f)
    except FileNotFoundError:
        notes = []
    return notes


def save_notes(file, notes):
    # сохранение списка заметок в файл
    with open(file, 'w') as f:
        json.dump(notes, f)
