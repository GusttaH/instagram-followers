from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.command import Command
import time

chrome_options = Options()
# chrome_options.add_argument("--headless")        
chrome_options.add_argument('log-level=3')
#configurando o user-agent
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135")
#desabilitando imagens
prefs = {"profile.managed_default_content_settings.images": 2}
chrome_options.add_experimental_option("prefs", prefs)
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")


driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.instagram.com/")
driver.maximize_window()

def execute():
  
  login()
  # get_followers()
  get_following()

def login():
  username = driver.find_element_by_name('username')
  password = driver.find_element_by_name('password')
  username.send_keys('user')
  password.send_keys('senha')

  time.sleep(1)
  driver.find_elements_by_tag_name('button')[1].click()
  time.sleep(2)

def get_followers():
  driver.get('') # https://www.instagram.com/@user/followers
  time.sleep(1)
  div_scroll = driver.find_element_by_class_name('isgrP')
  div_items = driver.find_element_by_class_name('PZuss')
  followers = []
  while len(followers) < 2078:
    print('followers collected', len(followers))
    followers = []
    items = div_items.find_elements_by_class_name('FPmhX')
    driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', div_scroll)
    time.sleep(.5)
    followers = items
  
  


def get_following():
  driver.get('') # https://www.instagram.com/@user/followers
  time.sleep(1)
  div_scroll = driver.find_element_by_class_name('isgrP')
  div_items = driver.find_element_by_class_name('PZuss')
  following = []
  while len(following) < 1331:
    print('following collected', len(following))
    items = div_items.find_elements_by_class_name('FPmhX')
    driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', div_scroll)
    time.sleep(.5)
    following.append(items)
  



execute()
