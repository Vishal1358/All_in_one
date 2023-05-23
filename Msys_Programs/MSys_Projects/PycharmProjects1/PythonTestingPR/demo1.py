from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

d = webdriver.Chrome(ChromeDriverManager().install())
d.get("https://www.facebook.com/")
d.close()