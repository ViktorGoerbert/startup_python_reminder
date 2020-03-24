from pip._vendor.distlib.compat import raw_input
from selenium import webdriver
import time





print("What shall I remind you about?")
text = str(raw_input())
print('How many periods?')
periods = int(raw_input())
print("How many minutes per period?")
local_time = float(raw_input())
local_time = local_time * 60
for x in range(periods):

    time.sleep(local_time)
    print(text)
    driver = webdriver.Chrome('/home/op-goerbert/PycharmProjects/untitled/chromedriver')
    driver.get('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

    play = driver.find_element_by_id('container');
    play.click();
    time.sleep(13)
    driver.quit()