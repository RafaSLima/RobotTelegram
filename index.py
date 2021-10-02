# Importar bibliotecas necessarias
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import pyodbc
import pyautogui


# Conexão com o Banco de Dados

server = 'SILVER\SQLEXPRESS'
database = 'ITEMS_SHIP'
username = 'sa'
password = '12345678'
connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + 
';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)

cursor =  connection.cursor()

# Setando configurações do browser

options = webdriver.ChromeOptions()
options.add_argument('lang=pt-br')
options.add_argument('--start-maximized')
options.add_argument('--user-data-dir=C:\\Users\\w10\\AppData\\Local\\Google\\Chrome\\User Data\\Default')
options.add_argument('--profile-directory=Profile 1')

# Navegando até o telegram

driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options = options)
driver.get('https://web.telegram.org/z/')
time.sleep(5)

# Buscando ids no Banco de dados
cursor.execute("SELECT ID FROM SEND_TELEGRAM WHERE VALIDATION = 0 ORDER BY ID")
ids = cursor.fetchall()

def buscando(contact):

    search = driver.find_element_by_id('telegram-search-input')
    search.send_keys(contact)
    time.sleep(5)

    group = driver.find_element_by_xpath('//*[@id="LeftColumn-main"]/div[2]/div[2]/div/div[2]/div/div/div[2]/div/div/div/div[2]')
    group.click()
    time.sleep(5)

def send_message(msg):
    
    messagem = driver.find_element_by_id('editable-message-text')
    messagem.clear()
    time.sleep(2)
    messagem.send_keys(msg)
    time.sleep(5)

    send_messagem = driver.find_element_by_xpath('//*[@id="MiddleColumn"]/div[3]/div[2]/div/div[2]/div[1]/button')
    send_messagem.click()
    time.sleep(5)

def send_file(file):

    clip = driver.find_element_by_xpath('//*[@id="message-compose"]/div[2]/button[2]')
    clip.click()
    time.sleep(2)

    anexo = driver.find_element_by_xpath('//*[@id="message-compose"]/div[2]/div[4]/div/div[2]')
    anexo.click()
    time.sleep(5)

    pyautogui.write(file)
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(5)

    send_anexo = driver.find_element_by_xpath('//*[@id="portals"]/div/div/div/div[2]/div[1]/button[2]')
    send_anexo.click()
    time.sleep(2)

def send_img(img):

    clip = driver.find_element_by_xpath('//*[@id="message-compose"]/div[2]/button[2]')
    clip.click()
    time.sleep(2)

    imagem = driver.find_element_by_xpath('//*[@id="message-compose"]/div[2]/div[4]/div/div[1]')
    imagem.click()
    time.sleep(2)

    pyautogui.write(img)
    pyautogui.press('enter')
    time.sleep(2)

    send_img = driver.find_element_by_xpath('//*[@id="portals"]/div/div/div/div[2]/div[1]/button[2]')
    send_img.click()
    time.sleep(5)

for id in ids:
    cursor.execute("SELECT CONTACT FROM SEND_TELEGRAM WHERE ID =?", id)
    contact = cursor.fetchall()
    cursor.execute("SELECT MESSAGE FROM SEND_TELEGRAM WHERE ID =?", id)
    msg = cursor.fetchall()
    cursor.execute("SELECT SRC_FILE FROM SEND_TELEGRAM WHERE ID =?", id)
    file = cursor.fetchall()
    cursor.execute("SELECT SRC_IMG FROM SEND_TELEGRAM WHERE ID =?", id)
    img = cursor.fetchall()
    buscando(contact[0][0])
    if msg[0][0] != None:
        send_message(msg[0][0])
    if img[0][0] != None:
        send_img(img[0][0])
    if file[0][0] != None:
        send_file(file[0][0])
    cursor.execute("UPDATE SEND_TELEGRAM SET VALIDATION = 1, DATE_SEND = CONVERT(DATE,GETDATE()) WHERE ID =?", id)
    cursor.commit()



driver.quit()
