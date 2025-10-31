from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
from datetime import datetime
import os

dados = []

num = 0

pesquisa = "Power BI"
pesquisa = pesquisa.replace(" ", "%20")

driver = webdriver.Firefox()
espera = WebDriverWait(driver, 5)
driver.maximize_window()
driver.get(f"https://www.linkedin.com/jobs/search/?currentJobId=4332782262&f_TPR=r604800&geoId=106057199&keywords={pesquisa}&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true")
time.sleep(3)

botao_fechar = driver.find_element(By.XPATH, "//button[@aria-label='Fechar']")
driver.execute_script("arguments[0].click();", botao_fechar)

def vagas():
        return driver.find_elements(By.XPATH, "//div[@class='base-search-card__info']")

def esperar(num):
    try:
        espera.until(lambda driver: len(vagas()) > num)
    except:
        print("As vagas pararam de carregar")
        return False

for job in range(70):
    if esperar(job) == False:
        break
    scrolling = vagas()
    driver.execute_script('arguments[0].scrollIntoView();', scrolling[job])
    vaga = vagas()
    nome_vaga = vaga[job].find_element(By.XPATH, ".//h3[@class='base-search-card__title']").text
    nome_empresa = vaga[job].find_element(By.XPATH, ".//h4[@class='base-search-card__subtitle']").text
    local_vaga = vaga[job].find_element(By.XPATH, ".//span[@class='job-search-card__location']").text
    try:
        link = vaga[job].find_element(By.XPATH, "./preceding-sibling::a\
        [contains(@class, 'base-card__full-link')]").get_attribute("href")
    except:
        link = "Sem Link"

    try:
        tempo_vaga = vaga[job].find_element(By.XPATH, ".//time[@class='job-search-card__listdate']").text
    except:
        tempo_vaga = vaga[job].find_element(By.XPATH, ".//time[@class='job-search-card__listdate--new']").text

    finally:
        dados.append({"Nome da Vaga": nome_vaga,
                      "Nome da Empresa": nome_empresa,
                      "Local da Vaga": local_vaga,
                     "Foi postada a:": tempo_vaga,
                      "Link da vaga:": link
                     })

df = pd.DataFrame(dados)

data_hoje = datetime.now().strftime("%d-%m-%Y")

pesq = pesquisa.replace("%20", " ")

nome_arquivo = f"Vagas em {pesq} {data_hoje}"

df.to_csv(f'{nome_arquivo}.csv', index=False, encoding='utf-8-sig')

print(f"Arquivo {nome_arquivo} criado com sucesso!")

try:
    pasta_origem = "D:/Programação/Python/Automacao/"
    pasta_destino = "D:/Dados para Analise/Vagas LinkedIN/"
    os.rename(f'{pasta_origem}' + f'{nome_arquivo}.csv', f'{pasta_destino}' + f'{nome_arquivo}.csv')
    print(f"\nArquivo {nome_arquivo} movido com sucesso!")
except:
    print("\nOcorreu um erro ao realocar o arquivo!")
finally:
    driver.quit()