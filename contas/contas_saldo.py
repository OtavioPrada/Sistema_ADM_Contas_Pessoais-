import PySimpleGUI as sg
import mysql.connector
import persistencia.persistencia_contas as thisPersistencia
thisPersistencia = thisPersistencia.PersistenciaContas


# Função para exibir a tabela de contas
def criaTela():

    sg.ChangeLookAndFeel('Dark')
    # Layout da interface
    layout = [
        [sg.Text('Inclusão de Saldo', justification='center')],
        [sg.Text('Codigo', size=(5, 1)), sg.Text(text='', key='labCodigo')],
        [sg.Button('Fechar')]
    ]

    window = sg.Window('Inclusão Saldo', layout, finalize=True)
    while True:
        iCodigo = thisPersistencia.getLastCodigo()
        codigo = (iCodigo)
        window['labCodigo'].update(codigo)
        event, _ = window.read()
        if event == sg.WINDOW_CLOSED or event == 'Fechar':
            break


    window.close()