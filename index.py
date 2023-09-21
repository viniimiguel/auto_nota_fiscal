from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from time import sleep

class Nota_fiscal:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.set_window_size(462,976)
        self.sitelink='https://erp.tiny.com.br/login/'
        self.cnpj_empresa = ['42.247.586/0001-33', '34.028.316/0001-03', '20.121.850/0001-55', '34.268.705/0001-06']
        self.login={
            'credenciais':{
                'login':'/html/body/div/div/div/div/div[1]/div[1]/div[2]/div/input',
                'senha':'/html/body/div/div/div/div/div[1]/div[1]/div[3]/div/input',
                'button':'/html/body/div/div/div/div/div[1]/div[1]/div[5]/button',
                'hamburguer':'/html/body/div[3]/div[1]/div[1]',
                'vendas':'/html/body/div[3]/div[2]/div[1]/div[1]/nav/ul/li[4]',
                'ntf':'#main-menu > div.sidebar-menu-container > div.sidebar-menu > div.sidebar-menu-nav > nav > ul > li.menu-modulos--active.menu-modulos-mobile--active > nav > ul > li:nth-child(3) > a > span',
                'situacao':'/html/body/div[7]/div/div[4]/div[1]/div[4]/div[2]/ul/li/a/span[2]/span',
                'pendentes':'/html/body/div[7]/div/div[4]/div[1]/div[4]/div[2]/ul/li/ul/li[2]/a',

            }
        }
    def main(self): 
        self.abre()
        self.ntf()
        sleep(5)
        self.envia()
        sleep(2000)

    def abre(self):
        self.driver.get(self.sitelink)

    
        self.driver.find_element(By.XPATH,self.login['credenciais']['login']).click()
        sleep(2)
        self.driver.find_element(By.XPATH,self.login['credenciais']['senha']).click()
        sleep(2)
        self.driver.find_element(By.XPATH,self.login['credenciais']['button']).click()
        sleep(30)


    def ntf(self):
        try:
            self.driver.find_element(By.XPATH,self.login['credenciais']['hamburguer']).click()
            sleep(0.5)
            self.driver.find_element(By.XPATH,self.login['credenciais']['vendas']).click()
            sleep(1)
            self.driver.find_element(By.CSS_SELECTOR,self.login['credenciais']['ntf']).click()
            sleep(7)
            self.driver.find_element(By.XPATH,self.login['credenciais']['situacao']).click()
            sleep(5)
            self.driver.find_element(By.XPATH,self.login['credenciais']['pendentes']).click()
            sleep(0.5)

        except Exception as e:
            print(f'Erro {e}')
            
    def envia(self):
        self.contador=1

        while True:
                notas={
                    'ne_fiscais':{
                        'NT':f'/html/body/div[7]/div/div[4]/div[2]/div[2]/div/div[1]/form/table/tbody/tr[{self.contador}]/td[3]'
                    }
                }
                self.editar={
                    'valores':{
                        'edit':'/html/body/div[7]/div/div[5]/div[1]/div/button',
                        'cnpj':'/html/body/div[7]/div/div[5]/div[2]/div[2]/form/div[13]/div/div[5]/div[1]/div[2]/input',
                        'desconto':'/html/body/div[7]/div/div[5]/div[2]/div[2]/form/div[10]/div[1]/div[13]/input',
                        'salvar':'/html/body/div[7]/div/div[5]/div[2]/div[2]/form/div[17]/div/div/button[2]'
                    }
                }
                try:
                    self.driver.find_element(By.XPATH,notas ['ne_fiscais']['NT']).click()
                    sleep(5)
                    self.driver.find_element(By.XPATH,self.editar ['valores']['edit']).click()
                    sleep(5)
                    valida=self.driver.find_element(By.XPATH,self.editar['valores']['cnpj'])
                    validat=valida.text
                    print (validat)
                    print(valida)
                    if validat[0]== '42.247.586/0001-33':
                        ds=self.driver.find_element(By.XPATH,self.editar['valores']['desconto'])
                        
                        sleep(1)
                        desconto='80%'
                        ds.send_keys(desconto)
                    elif validat[1]== '34.028.316/0001-03':
                        ds=self.driver.find_element(By.XPATH,self.editar['valores']['desconto'])
                        
                        sleep(1)
                        desconto='80%'
                        ds.send_keys(desconto)
                    elif validat[2]== '20.121.850/0001-55':
                        ds=self.driver.find_element(By.XPATH,self.editar['valores']['desconto'])
                        
                        sleep(1)
                        desconto='50%'
                        ds.send_keys(desconto)
                    elif validat[3]== '34.268.705/0001-06':
                        ds=self.driver.find_element(By.XPATH,self.editar['valores']['desconto'])
                        
                        sleep(1)
                        desconto='90%'
                        ds.send_keys(desconto)
                    else:
                        ds=self.driver.find_element(By.XPATH,self.editar['valores']['desconto'])
                        
                        sleep(1)
                        desconto='80%'
                        ds.send_keys(desconto)
                    self.driver.find_element(By.XPATH,self.editar['valores']['salvar'])
                    self.contador += 1
                except NoSuchElementException:
                    break
                except Exception as e:
                    print(f'Erro {e}')
        
notafiscal= Nota_fiscal()
notafiscal.main()
