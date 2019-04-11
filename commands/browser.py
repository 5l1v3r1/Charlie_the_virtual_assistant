from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#options.headless = True



def google():    
    options = Options()
    driver = webdriver.Chrome(executable_path='G:/Python/Charlie/commands/chromedriver.exe', chrome_options=options)

    driver.get("http://google.com/")

def youtube():
    options = Options()
    driver = webdriver.Chrome(executable_path='G:/Python/Charlie/commands/chromedriver.exe', chrome_options=options)

    driver.get("http://www.youtube.com")


