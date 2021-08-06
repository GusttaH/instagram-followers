from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.command import Command
import time
import re

chrome_options = Options()
chrome_options.add_argument('log-level=3')
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135")

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.instagram.com/")
driver.maximize_window()

followers = [...] # deve conter o array com o @ dos usuários.


def execute():
  print('login')
  for follower in followers:
    print('> Current follower...', follower)
    driver.get('https://www.instagram.com/{}/'.format(follower))
    time.sleep(1)
    try:
      pub = driver.find_element_by_class_name('-nal3').text
      pub_number = int(re.findall(r'\d+', pub)[0])
    except Exception as Ex:
      print('Error on hitting page')    

    if (pub_number < 4):
      try:
        driver.find_element_by_class_name('glyphsSpriteFriend_Follow').click()
        time.sleep(1)
        driver.find_element_by_class_name('-Cab_').click()
        print('> You\'re nor following "{}" anymore...'.format(follower))
      except Exception as ex:
        print(ex)   

  print('> Process completed successfully')     


execute()