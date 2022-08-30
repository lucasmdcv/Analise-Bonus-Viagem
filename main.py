import pandas as pd
from twilio.rest import Client
import virtualenv


# Your account Sid from twilio.com/console
#https://console.twilio.com/?frameUrl=%2Fconsole%3Fx-target-region%3Dus1
account_sid = "AC0520e1a8eb2ae3c88e6edbf53627d042"
#Yout Auth Token from twilio.com/console
auth_token = "b5d0d2a647cab0d88b89bf57bcbb4735"
client = Client(account_sid, auth_token)

# Abrir os 6 arquivos em Excel
lista_meses = ['janeiro','fevereiro','março','abril','maio','junho']

for mes in lista_meses:
    print(mes)
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    print(tabela_vendas)
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000 , 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000 , 'Vendas'].values[0]
        print(f'No mês {mes} alguém bateu a meta. Vendedor: {vendedor},Vendas:{vendas}') 
    message = client.message.create(
           to ='+55 800 591 2482',
        from_='+55 61 99217 6239',
    body = f'No mês {mes} alguém bateu a meta. Vendedor: {vendedor},Vendas:{vendas}')
    print( message.sid) 




#Para cada arquivo:
#verificar se algum valor na coluna Vendas daquele arquivo é maior que 55.000

#Se for maior do que 55.000 --> um SMS com o nome, o mês e as vendas do vendedor

#caso não seja maior do que 55.000 não quero fazer nada