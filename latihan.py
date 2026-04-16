notes = []

def add_note():
    note = input("Masukkan catatan: ")
    notes.append(note)

def show_notes():
    for index, note in enumerate(notes):
        print(f"{index}. {note}")

def delete_note():
    try:
        index = int(input("Index: "))
        notes.pop(index)
    except:
        print("Input tidak valid")