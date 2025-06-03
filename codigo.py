# Passo 1: Entrar no sistemas da empresa - Ex.: https://dlp.hashtagtreinamentos.com/python/intensivao/login
# Passo 2: Fazer login
# Passo 3: Importar a base de dados - Ex.: produtos.csv 
# Passo 4: Cadastrar 1 produto
# Passo 5: Repetir para todos produtos

# pg.click -> clica em algum lugar
# pg.press -> aperta 1 tecla 
# pg.write -> escreve um texto
# pg.hotkey -> apertar uma combinação de teclas pg.hotkey('ctrl', 'c')

import pyautogui as pg
import time
import pandas as pd

pg.PAUSE = 0.5

pg.press('win')
pg.write('chrome')
pg.press('enter')
pg.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pg.press('enter')
time.sleep(2)
pg.click(x = 811, y = 403) 
pg.write('teste@gmail.com')
pg.press('tab')
pg.write('minhasenhasecreta')
pg.press('tab')
pg.press('enter')
time.sleep(2)
tabela = pd.read_csv('produtos.csv')
print(tabela)

for linha in tabela.index:
    pg.click(x=763, y=288)
    codigo = tabela.loc[linha, 'codigo']
    pg.write(codigo)
    pg.press('tab')
    marca = tabela.loc[linha, 'marca']
    pg.write(marca)
    pg.press('tab')
    tipo = tabela.loc[linha, 'tipo']
    pg.write(tipo)
    pg.press('tab')
    categoria = tabela.loc[linha, 'categoria']
    pg.write(str(categoria))
    pg.press('tab')
    preco_unitario = tabela.loc[linha, 'preco_unitario']
    pg.write(str(preco_unitario))
    pg.press('tab') 
    custo = tabela.loc[linha, 'custo']
    pg.write(str(custo))
    pg.press('tab')
    obs = str(tabela.loc[linha, 'obs'])
    if obs != 'nan':
        pg.write(obs)
        pg.press('tab')
    pg.press('enter')
    pg.scroll(10000)