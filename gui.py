import rekins
from rekins import Rekins
import PySimpleGUI as gui

gui.LOOK_AND_FEEL_TABLE['CyberpunkTheme'] = {'BACKGROUND': '#FFFC2E',
                                        'TEXT': '#19F1FF',
                                        'INPUT': '#FF2525',
                                        'TEXT_INPUT': '#000000',
                                        'SCROLL': '#19F1FF',
                                        'BUTTON': ('#FFFC2E', '#19F1FF'),
                                        'PROGRESS': ('#FF2525', '#FFFC2E'),
                                        'BORDER': 1, 'SLIDER_DEPTH': 0, 
'PROGRESS_DEPTH': 0, }
gui.theme('CyberpunkTheme')



laditeLayout = [[gui.Text('Ievadi Vardu')],[gui.InputText('',key='Vards'),gui.Text('')],[gui.Text('Ievadi Veltijumu')],[gui.InputText('',key='Veltijums')],[gui.Text('Ievadi Izmeru (platums/garums/augstums)')],[gui.InputText('',key='Izmers')],[gui.Text('Ievadi Materiala Cenu')],[gui.InputText('',key='Materials'),gui.Button('Aprekinat',key='Aprekins')]]

layout = [[gui.Text('H e l l o ')],[gui.Button("Do NOT Press Here!",size=(5,5)),gui.Button('Exit')],[gui.Text('',key='-Choice-')]]

window = gui.Window('Rekins',laditeLayout, size=(500,250),finalize=True)

while True:
    event, values = window.read()
    if event == 'Aprekins':
        print('Poga Nospiesta')
        dati = Rekins(values['Vards'],values['Veltijums'],values['Izmers'],values['Materials'])
        print(dati.aprekins()[1])
    if event == gui.WIN_CLOSED:
        break
    if event == 'Exit':
        break
    if event == 'Do NOT Press Here!':
        window['-Choice-'].update('YOU PRESSED IT!?')
        window['Do NOT Press Here!'].update(button_color = ('black','red'),disabled=True)

window.close()