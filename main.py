import PySimpleGUI as sg
import random

header = [[sg.Text('Wisielec')]]
buttons_bottom = [[sg.Button('Nowa gra', key='-NEW_GAME-', size=(20, 15)), sg.Button('Wyjdz', key='-EXIT-', size=(20, 15))]]

layout = [
    [sg.Frame('', header, size=(400, 30), vertical_alignment='center', element_justification='center')],
    [sg.Text('Kategoria: ', key='-CATEGORY-')],
    [sg.Text('Uzyte litery: ', size=(50, 2), key='-USED_LETTERS-')],
    [sg.Text('Zycia: ', key='-LIFES-')],
    [sg.Text('Odgadywane slowo: ', key='-WORD-')],
    [sg.Input(size=(25, 1), key='-INPUT-', disabled=True), sg.Button('Sprawdz', key='-SEND-', size=(25, 1), disabled=True)],
    [sg.Text('', key='-INFO-')],
    [sg.Frame('Dominik Szymański, 26071', buttons_bottom, size=(400, 60), vertical_alignment='center', element_justification='center')]
]

window = sg.Window('Window Title', layout)


words = [
    {'word': 'truskawka', 'category': 'owoc'},
    {'word': 'samochod', 'category': 'pojazd'},
    {'word': 'komputer', 'category': 'sprzet elektroniczny'},
    {'word': 'biurko', 'category': 'mebel'},
    {'word': 'kangur', 'category': 'zwierze'},
    {'word': 'zlodziej', 'category': 'zawod'},
    {'word': 'zeszyt', 'category': 'przedmiot szkolny'},
    {'word': 'motocykl', 'category': 'pojazd'},
    {'word': 'goryl', 'category': 'zwierze'},
    {'word': 'laptop', 'category': 'sprzet elektroniczny'},
    {'word': 'butelka', 'category': 'przedmiot codziennego uzytku'},
    {'word': 'zolw', 'category': 'zwierze'},
    {'word': 'skrzypce', 'category': 'instrument muzyczny'},
    {'word': 'lampka', 'category': 'przedmiot codziennego uzytku'},
    {'word': 'wino', 'category': 'napoj alkoholowy'},
    {'word': 'pralka', 'category': 'sprzet AGD'},
    {'word': 'pajak', 'category': 'owad'},
    {'word': 'ksiazka', 'category': 'przedmiot szkolny'},
    {'word': 'cukier', 'category': 'produkt spozywczy'},
    {'word': 'rower', 'category': 'pojazd'},
    {'word': 'delfin', 'category': 'zwierze'},
    {'word': 'telewizor', 'category': 'sprzet RTV'},
    {'word': 'drzewo', 'category': 'roslina'},
    {'word': 'rak', 'category': 'zwierze'},
    {'word': 'skarbonka', 'category': 'przedmiot codziennego uzytku'},
    {'word': 'guma do zucia', 'category': 'slodycz'},
    {'word': 'kawa', 'category': 'napoj'},
    {'word': 'zarowka', 'category': 'przedmiot domowy'},
    {'word': 'pianino', 'category': 'instrument muzyczny'},
    {'word': 'motyl', 'category': 'owad'},
    {'word': 'kotlet', 'category': 'danie miesne'},
    {'word': 'kon', 'category': 'zwierze'},
    {'word': 'lampa', 'category': 'przedmiot domowy'},
    {'word': 'kanapka', 'category': 'jedzenie'},
    {'word': 'swinka morska', 'category': 'zwierze'},
    {'word': 'kurtka', 'category': 'ubranie'},
    {'word': 'ryba', 'category': 'zwierze wodne'},
    {'word': 'olowek', 'category': 'przedmiot szkolny'},
    {'word': 'lody', 'category': 'slodycz'},
    {'word': 'zaba', 'category': 'zwierze'},
    {'word': 'mikrofalowka', 'category': 'sprzet AGD'},
    {'word': 'konik polny', 'category': 'zwierze'},
    {'word': 'dzwonek', 'category': 'przedmiot domowy'},
    {'word': 'piec', 'category': 'przedmiot domowy'},
    {'word': 'pociag', 'category': 'pojazd'},
    {'word': 'zaglowka', 'category': 'pojazd wodny'},
    {'word': 'kawalek sera', 'category': 'jedzenie'},
    {'word': 'mucha', 'category': 'owad'},
    {'word': 'przycisk', 'category': 'przedmiot elektroniczny'},
    {'word': 'telefon', 'category': 'sprzet elektroniczny'},
    {'word': 'waz', 'category': 'zwierze'},
    {'word': 'glowa', 'category': 'czesc ciala'},
    {'word': 'gruszka', 'category': 'owoc'},
    {'word': 'roleta', 'category': 'przedmiot domowy'},
    {'word': 'kaczka', 'category': 'zwierze'},
    {'word': 'fartuch', 'category': 'ubranie'},
    {'word': 'lodz podwodna', 'category': 'pojazd wodny'},
    {'word': 'kot', 'category': 'zwierze'},
    {'word': 'kwiat', 'category': 'roslina'},
    {'word': 'slon', 'category': 'zwierze'},
    {'word': 'mysz', 'category': 'zwierze'},
    {'word': 'zagiel', 'category': 'przedmiot wodny'}
]

lifes = 5
used_letters = []

current_word = ''
current_category = ''
user_word = ''


def new_game():
    global random_entry, current_category, current_word, lifes, used_letters, user_word
    random_entry = random.choice(words)
    current_word = random_entry['word']
    current_category = random_entry['category']
    lifes = 5
    used_letters = []
    user_word = ''
    for letter in current_word:
        user_word += '_'

    
def generate_used_letters_text(used_letters):
    used_letters_string = ''
    for element in used_letters:
        used_letters_string += element + ', '
    used_letters_string = used_letters_string[:len(used_letters_string) - 2]
    return used_letters_string
    
new_game()

while True:
    event, values = window.read()
    
    if event == '-NEW_GAME-':
        new_game()
        window['-INFO-'].update("Rozpoczeto nowa gre.")
        window['-SEND-'].update(disabled=False)
        window['-INPUT-'].update(disabled=False)
    
    if event == sg.WIN_CLOSED or event == '-EXIT-': # if user closes window or clicks cancel
        break
    
    if len(values['-INPUT-']) == 1:
        letter = values['-INPUT-'].lower()
        window['-INPUT-'].update("")
        
        if letter not in used_letters:
            used_letters.append(letter)
        
        if letter not in current_word or letter in user_word:
            window['-INFO-'].update("Pudlo!")
            lifes -= 1
        
        if letter in current_word and letter not in user_word:
            new_user_word = ''
            for id, word_letter in enumerate(current_word):
                if letter == current_word[id]:
                    new_user_word += letter
                else:
                    new_user_word += user_word[id]
            user_word = new_user_word
            window['-INFO-'].update("Trafiono!")
                
            
    elif (len(values['-INPUT-']) < 1):
        window['-INFO-'].update("Pole nie moze byc puste.")
        window['-INPUT-'].update("")
    else:
        window['-INFO-'].update("Mozesz podac tylko jenda litere na raz!")
        window['-INPUT-'].update("")
        
    
    window['-CATEGORY-'].update('Kategoria: ' + current_category)
    window['-USED_LETTERS-'].update('Użyte litery: ' + generate_used_letters_text(used_letters))
    window['-LIFES-'].update('Zycia: ' + str(lifes))
    window['-WORD-'].update('Slowo: ' + " ".join(user_word))
    
    if (user_word == current_word):
        window['-INFO-'].update("Wygrales!")
        window['-SEND-'].update(disabled=True)
        window['-INPUT-'].update(disabled=True)
    
    if (lifes == 0):
        window['-INFO-'].update("Przegrales!")
        window['-SEND-'].update(disabled=True)
        window['-INPUT-'].update(disabled=True)
    
window.close()
