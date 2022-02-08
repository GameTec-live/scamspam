from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
import random
import time
from faker import Faker
from bs4 import BeautifulSoup

#defautl setting
url = """
http://localhost/
"""
timeout = False
emails = ["@gmail.com", "@yahoo.com", "@hotmail.com", "@outlook.com", "@webnet.com", "@comcast.net", "@email.net"]



#def oobe
def yes_or_no(question):
    while "the answer is invalid":
        reply = str(input(question+' (y/n): ')).lower().strip()
        if reply[0] == 'y':
            return True
        if reply[0] == 'n':
            return False


print("\033[31m" + """"
 (                     (                       
 )\ )                  )\ )                    
(()/(        )    )   (()/(          )    )    
 /(_)) (  ( /(   (     /(_))`  )  ( /(   (     
(_))   )\ )(_))  )\  '(_))  /(/(  )(_))  )\  ' 
/ __| ((_|(_)_ _((_)) / __|((_)_\((_)_ _((_))  
\__ \/ _|/ _` | '  \()\__ \| '_ \) _` | '  \() 
|___/\__|\__,_|_|_|_| |___/| .__/\__,_|_|_|_|  
                           |_|                 
""")

url = str(input("\033[32m" + "Enter the URL (https://localhost/): "))
timeout = yes_or_no("\033[32m" + "Do you want to use a timeout?")
print("\033[34m" + str(emails))
print("\033[0m" +"starting...")


char_list = ["^","%","$","#","@","!"]
fake = Faker()
options = Options()
options.headless = False
driver = webdriver.Chrome(options=options)
driver.get(url)
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
form = soup.find("form")

print("this programm will run untill you interrupt it. (ctrl+c)")
try:
    while True:
        for inpt in soup.find_all('input'):
            if inpt.get('type') == 'password':
                password = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//input[@class='%s'][@type='password']" % inpt.get('class')[0])))
                password1 = fake.password(length=random.randint(6, 20))
                password.clear()
                password.send_keys(password1)
            else:
                choice = random.choice(char_list)
                username = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//input[@class='%s']" % inpt.get('class')[0])))
                username1 = fake.name().replace(" ", "") + random.choice(emails)
                username.clear()
                username.send_keys(username1)
        password.submit()
        print("Sent Username: {} Password: {}".format(username1, password1))
        if timeout:
            time.sleep(random.randint(0, 2))
except KeyboardInterrupt:
    print("terminating...")
    driver.close()
    exit()

driver.close()