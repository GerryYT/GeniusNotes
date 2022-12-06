from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QInputDialog

import json

Form, Window = uic.loadUiType("untitled.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)

'''notes = {
    "Добро пожаловать!" : {
        "текст" : "Это самое лучшее приложение для заметок в мире!",
        "теги" : ["добро", "инструкция"]
    }
}
with open("notes_data.json", "w") as file:
    json.dump(notes, file)'''

def add_note():
    note_name, ok = QInputDialog.getText(window, "Добавить заметку", "Название заметки: ")
    if ok and note_name != "":
        notes[note_name] = {"текст" : "", "теги" : []}
        form.SpisokZametok.addItem(note_name)
        form.SpisokZametok_2.addItems(notes[note_name]["теги"])
        print(notes)

def show_note():
    key = form.SpisokZametok.selectedItems()[0].text()
    print(key)
    form.textEdit.setText(notes[key]["текст"])
    form.SpisokZametok_2.clear()
    form.SpisokZametok_2.addItems(notes[key]["теги"])

def save_note():
    if form.SpisokZametok.selectedItems():
        key = form.SpisokZametok.selectedItems()[0].text()
        notes[key]["текст"] = form.textEdit.toPlainText()
        with open('notes_data.json', 'w') as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False)
        print(notes)
    else:
        print('Заметка для сохранения не выбрана!')

def del_note():
    if form.SpisokZametok.selectedItems():
        key = form.SpisokZametok.selectedItems()[0].text()
        del notes[key]
        form.SpisokZametok.clear()
        form.SpisokZametok_2.clear()
        form.textEdit.clear()
        form.SpisokZametok.addItems(notes)
        with open('notes_data.json', 'w') as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False)
        print(notes)
    else:
        print('Заметка для удаления не выбрана!')

def add_tag():
    if form.SpisokZametok.selectedItems():
        key = form.SpisokZametok.selectedItems()[0].text()
        tag = form.lineEdit.text()
        if not tag in notes[key]["теги"]:
            notes[key]["теги"].append(tag)
            form.SpisokZametok_2.addItem(tag)
            form.lineEdit.clear()
        with open("notes_data.json", "w") as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False)
        print(notes)
    else:
        print("Заметка для добавления тега не выбрана!")

def del_tag():
    if form.SpisokZametok_2.selectedItems():
        key = form.SpisokZametok.selectedItems()[0].text()
        tag = form.SpisokZametok_2.selectedItems()[0].text()
        notes[key]["теги"].remove(tag)
        form.SpisokZametok_2.clear()
        form.SpisokZametok_2.addItems(notes[key]["теги"])
        with open("notes_data.json", "w") as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False)
        print(notes)
    else:
        print("Тег для удаления не выбран!")

def search_tag():
    print(form.SearchZametka.text())
    tag = form.lineEdit.text()
    if form.SearchZametka.text() == "Искать заметки по тегу" and tag:
        print(tag)
        notes_filtered = {}
        for note in notes:
            if tag in notes [note]["теги"]:
                notes_filtered[note]=notes[note]
        form.SearchZametka.setText("Сбросить поиск")
        form.SpisokZametok.clear()
        form.SpisokZametok_2.clear()
        form.SpisokZametok.addItems(notes_filtered)
        print(form.SearchZametka.text())
    elif form.SearchZametka.text() == "Сбросить поиск":
        form.lineEdit.clear()
        form.SpisokZametok.clear()
        form.SpisokZametok_2.clear()
        form.SpisokZametok.addItems(notes)
        form.SearchZametka.setText("🔎Искать заметки по тегу🔎")
        print(form.SearchZametka.text())
    else:
        pass

form.SpisokZametok.itemClicked.connect(show_note)
form.SaveZametka.clicked.connect(save_note)
form.DelZametka.clicked.connect(del_note)
form.AddZametka.clicked.connect(add_note)
form.AddZametka_2.clicked.connect(add_tag)
form.DelZametka_2.clicked.connect(del_tag)
form.SearchZametka.clicked.connect(search_tag)
with open("notes_data.json", "r") as file:
    notes = json.load(file)
form.SpisokZametok.addItems(notes)
window.show()
app.exec()
