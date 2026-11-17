from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

BRAVE_PATH = r"Introduce la ruta de tu navegador aquí"
CHROMEDRIVER_PATH = r"C:\chromedriver\chromedriver.exe"
 
USER_DATA_DIR = r"Introduce aquí la ruta de los datos de usuario de tu navegador"
PROFILE_NAME = "Default"
URL_PRESENTE = "instrucción 1"
 
options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
options.add_argument(r"--user-data-dir=C:\temp_brave_test2")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
 
service = Service(CHROMEDRIVER_PATH, log_output="chromedriver.log")
driver = webdriver.Chrome(service=service, options=options)
 
try:
    driver.get(URL_PRESENTE)
 
    wait = WebDriverWait(driver, 30)
 
    print("Esperando a que la página cargue...")
    time.sleep(5) 

    try:
        wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, "[data-testid='page-loading-spinner']")))
        print("El spinner desapareció.")
    except Exception:
        print("Ningún spinner detectado, continuamos.")
 
    time.sleep(3)

    print("Buscando la tarjeta de regalo...")
    botao_presente = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "[capture-custom-sku-name='PRESENTE DIÁRIO']"))
    )
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", botao_presente)
    time.sleep(2)
 
    print("Al hacer clic en la tarjeta del regalo...")
    botao_presente.click()
 
    time.sleep(3)

    print("Buscando el botón CLAIM GIFT...")
    botao_confirmar = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='claim-button']"))
    )
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", botao_confirmar)
    time.sleep(2)
 
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='claim-button']")))
 
    print("Al hacer clic en CLAIM GIFT...")
    try:
        botao_confirmar.click()
    except Exception:
        print("El clic falló, JavaScript...")
        driver.execute_script("arguments[0].click();", botao_confirmar)
 
    print("Y")
    time.sleep(4)
 
except Exception as e:
    print(f"N: {type(e).__name__}: {e}")

finally:
    driver.quit()