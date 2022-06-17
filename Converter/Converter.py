import PySimpleGUI as sg

layout = [
    #[sg.Text('Convert:'), sg.Spin(['item 1', 'item 2']) , sg.Text('To:'), sg.Spin(['item 1', 'item 2'])],
    [sg.Text('Convert:'), sg.Spin(['km to mile','kg to pound','sec to min'], key = '-UNITS-')],
    [sg.Text('Valor a ser convertido')],
    [sg.Input(key = '-INPUT-'), sg.Button('Converter', key = '-CONVERTBUTTON-')],
    [sg.Text('Valor convertido:'), sg.Text('output test', enable_events = True, key = '-OUTPUT-')]
]

window = sg.Window('Converter', layout)

while True:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED:
        break
    
    #Update text(-OUTPUT-) to the converted value
    if event == '-CONVERTBUTTON-':
        input_value = values['-INPUT-']
        #print('INPUT VALUE:', input_value)

        if input_value.isnumeric():
            conversion = values['-UNITS-']
            #print('CONVERSION UNIT VALUE: ', conversion)
            
            if conversion == 'km to mile':
                output = 
            elif conversion == 'kg to pound':
                output = 
            elif conversion == 'sec to min':
                output = 
        else:
            print('Error')
            
        print(output)
            
window.close()