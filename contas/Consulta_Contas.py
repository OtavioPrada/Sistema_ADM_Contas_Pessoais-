import PySimpleGUI as sg
import mysql.connector
import pandas as pd
import persistencia.persistencia_contas as thisPersistencia
thisPersistencia = thisPersistencia.PersistenciaContas

# Função para exibir a tabela de contas
def exibir_tabela_contas():
    contas = thisPersistencia.buscar_contas_Tabela()
    df = pd.DataFrame(contas, columns=['Nome', 'Valor'])

    layout = [
        [sg.Table(values=df.values.tolist(), headings=df.columns.tolist(), auto_size_columns=False,
                  display_row_numbers=True, justification='center', num_rows=min(25, len(df)), def_col_width=40, vertical_scroll_only=True)],
        [sg.Button('Fechar')]
    ]
    window = sg.Window('Tabela de Contas', layout, finalize=True)

    while True:
        event, _ = window.read()
        if event == sg.WINDOW_CLOSED or event == 'Fechar':
            break

    window.close()
