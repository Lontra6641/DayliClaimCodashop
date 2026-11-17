from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

BRAVE_PATH = r"enter the path to your browser here"
CHROMEDRIVER_PATH = r"C:\chromedriver\chromedriver.exe"
 
USER_DATA_DIR = r"enter the path to your browser's user data here"
PROFILE_NAME = "Default"
URL_PRESENTE = "instruction 1"
 
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
 
    print("Waiting for page to load...")
    time.sleep(5) 

    try:
        wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, "[data-testid='page-loading-spinner']")))
        print("The spinner has disappeared.")
    except Exception:
        print("No spinner detected; proceeding.")
 
    time.sleep(3)

    print("Looking for the gift card...")
    botao_presente = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "[capture-custom-sku-name='PRESENTE DIÁRIO']"))
    )
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", botao_presente)
    time.sleep(2)
 
    print("By clicking on the gift card...")
    botao_presente.click()
 
    time.sleep(3)

    print("Looking for the CLAIM GIFT button...")
    botao_confirmar = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='claim-button']"))
    )
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", botao_confirmar)
    time.sleep(2)
 
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='claim-button']")))
 
    print("By clicking on CLAIM GIFT...")
    try:
        botao_confirmar.click()
    except Exception:
        print("Click failed, JavaScript...")
        driver.execute_script("arguments[0].click();", botao_confirmar)
 
    print("Y")
    time.sleep(4)
 
except Exception as e:
    print(f"N: {type(e).__name__}: {e}")

finally:
    driver.quit()