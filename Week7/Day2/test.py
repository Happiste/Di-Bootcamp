from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Remplacez le chemin par celui où votre chromedriver est installé, si nécessaire
service = Service("/path/to/chromedriver")

driver = webdriver.Chrome(service=service)
driver.get("https://www.google.com")
print(driver.title)
driver.quit()