# @Autor Otavio Vinicius Prada
# Tela Inicial

import PySimpleGUI as sg
import mysql.connector
import pandas as pd
import Consulta_Contas as ConsultaContas
import contas_saldo as TelaAddSaldo
import persistencia.persistencia_contas as thisPersistencia
thisPersistencia = thisPersistencia.PersistenciaContas

#Seta o estilo ja janela
sg.ChangeLookAndFeel('Dark')


# Layout da interface
layout = [
    [sg.Text('Bem Vindo a Consolta de Contas', justification='center')],
    [sg.Text('Saldo Bruto do mês:', size=(15, 1)), sg.InputText(key='saldo')],
    [sg.Text('Contas do mês:',      size=(15, 1)), sg.InputText(key='contas')],
    # [sg.Checkbox('Parcelado:', key='parcelado')],
    [sg.Button('Adicionar Saldo'), sg.Button('Adicionar Divida')],
    [sg.Button('Consultar saldo'), sg.Button('Consultar Dividas')],
    # [sg.HorizontalSeparator()],
    # [sg.Text('Contas cadastradas')],
    [sg.Listbox(values=[], size=(40, 5), key='contas')],
    [sg.Button('Sair')]
]

# Cria a janela com o layout
window = sg.Window("Sistema de Contas", icon=r'icon.ico', element_justification='center').Layout(layout)
# Lista para armazenar as contas
# contas = thisPersistencia.buscar_contas()

# Loop para capturar os eventos da interface
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Sair':
        break

    elif event == 'Adicionar Saldo':
        TelaAddSaldo.criaTela()

    # elif event == 'Adicionar':
    #     nome  = values['nome']
    #     valor = values['valor']    
    #     thisPersistencia.inserir_conta(nome, valor)
    #     contas.append(f'{nome} - R${valor}')
    #     window['contas'].update(contas)
    #     sg.Popup('Conta adicionada com sucesso!')

    # elif event == 'Consultar':
    #     thisPersistencia.buscar_contas()
    #     window['contas'].update(contas)       

    # elif event == 'Remover':
    #     selecao = values['contas']
    #     if selecao:
    #         conta = selecao[0]
    #         nome, valor = conta.split(' - ')
    #         valor = float(valor[2:])
    #         cnx = thisPersistencia.conectar_bd()
    #         cursor = cnx.cursor()
    #         query = "DELETE FROM contas WHERE nome=%s AND valor=%s"
    #         values = (nome, valor)
    #         cursor.execute(query, values)
    #         cnx.commit()
    #         cursor.close()
    #         cnx.close()
    #         contas.remove(conta)
    #         window['contas'].update(contas)
    #         sg.Popup('Conta removida com sucesso!')

    elif event == 'Consultar Dividas':
        ConsultaContas.exibir_tabela_contas()        
# Fecha a janela
window.close()

