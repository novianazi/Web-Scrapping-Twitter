from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, urllib.request
import requests
from selenium.webdriver.common.by import By
import os
import pandas as pd

def selenium_twitter(user_name):
    pa = os.getcwd()
    PATH_link = pa+"\chromedriver.exe"
    driver = webdriver.Chrome(PATH_link)

    #show twitter
    link_username = 'https://twitter.com/'+user_name 
    driver.get(link_username)
    time.sleep(5)

    #get name
    name=driver.find_element(By.CSS_SELECTOR, "#react-root > div > div > div.css-1dbjc4n.r-18u37iz.r-13qz1uu.r-417010 > main > div > div > div > div > div > div:nth-child(3) > div > div > div > div > div.css-1dbjc4n.r-6gpygo.r-14gqq1x > div.css-1dbjc4n.r-1wbh5a2.r-dnmrzs.r-1ny4l3l > div > div.css-1dbjc4n.r-1wbh5a2.r-dnmrzs.r-1ny4l3l > div > div > span:nth-child(1) > span").text

    #get username twitter
    username = driver.find_element(By.CSS_SELECTOR,"#react-root > div > div > div.css-1dbjc4n.r-18u37iz.r-13qz1uu.r-417010 > main > div > div > div > div > div > div:nth-child(3) > div > div > div > div > div.css-1dbjc4n.r-6gpygo.r-14gqq1x > div.css-1dbjc4n.r-1wbh5a2.r-dnmrzs.r-1ny4l3l > div > div.css-1dbjc4n.r-1awozwy.r-18u37iz.r-1wbh5a2 > div > div > div > span").text

    #get followers
    followers =  driver.find_element(By.CSS_SELECTOR,"#react-root > div > div > div.css-1dbjc4n.r-18u37iz.r-13qz1uu.r-417010 > main > div > div > div > div.css-1dbjc4n.r-kemksi.r-1kqtdi0.r-1ljd8xs.r-13l2t4g.r-1phboty.r-1jgb5lz.r-11wrixw.r-61z16t.r-1ye8kvj.r-13qz1uu.r-184en5c > div > div:nth-child(3) > div > div > div > div > div.css-1dbjc4n.r-13awgt0.r-18u37iz.r-1w6e6rj > div:nth-child(2) > a > span.css-901oao.css-16my406.r-1nao33i.r-poiln3.r-1b43r93.r-b88u0q.r-1cwl3u0.r-bcqeeo.r-qvutc0 > span").text

    #get following
    following = driver.find_element(By.CSS_SELECTOR,"#react-root > div > div > div.css-1dbjc4n.r-18u37iz.r-13qz1uu.r-417010 > main > div > div > div > div.css-1dbjc4n.r-kemksi.r-1kqtdi0.r-1ljd8xs.r-13l2t4g.r-1phboty.r-1jgb5lz.r-11wrixw.r-61z16t.r-1ye8kvj.r-13qz1uu.r-184en5c > div > div:nth-child(3) > div > div > div > div > div.css-1dbjc4n.r-13awgt0.r-18u37iz.r-1w6e6rj > div.css-1dbjc4n.r-1mf7evn > a > span.css-901oao.css-16my406.r-1nao33i.r-poiln3.r-1b43r93.r-b88u0q.r-1cwl3u0.r-bcqeeo.r-qvutc0 > span").text  

    driver.close()
    #return name, username, link_username, following, following    
    return name, username, link_username, followers, following


if __name__ == '__main__':
    list_data = ['NovianAziSa', 'jokowi', 'Cristiano', 'realmadriden', 'IAmAlanWalker' ]

    #list output
    list_name = []
    list_username = []
    link_link_username = [] 
    list_followers = []
    list_following = []
    

    # scrapping process with selenium
    for i in range(len(list_data)):
        name, username, link_username, followers, following = selenium_twitter(list_data[i]) 
        #append data to list
        list_name.append(name) 
        list_username.append(username) 
        link_link_username.append(link_username) 
        list_followers.append(followers) 
        list_following.append(following) 

    #import data to pandas
    result = pd.DataFrame([*zip(list_name, list_username, link_link_username, list_followers, list_following)])   
    result.columns = ['profile_name', 'username', 'account_twitter', 'jumlah_followers', 'jumlah_following'] 
    print(result)

    #upload data twitter to csv
    path = os.getcwd()
    directory = path+'/'
    if not os.path.exists(directory):
        os.makedirs(directory)
    result.to_csv(f"{directory}twitter_profile.csv", index=False)

    #read CSV file
    data = pd.read_csv(f"{directory}twitter_profile.csv",)
    data

