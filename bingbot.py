from selenium import webdriver
import time
import string
import random
from random import randint
from selenium.webdriver.common.keys import Keys

def random_line_in_file(someFile):
    line = next(someFile);
    for num, aLine in enumerate(someFile):
        if random.randrange(num + 2) : continue;
        line = aLine;
    return line;

def get_list_of_random_words():
    bigTextFile = open('/home/harichetlur/Projects/Python/bingbot/big.txt');
    randomLine = random_line_in_file(bigTextFile);
    listOfRandomWords = randomLine.strip().split(' ');
    bigTextFile.close();
    return listOfRandomWords;

credentialFile = open('/home/harichetlur/Projects/Python/bingbot/creds.txt');

for line in credentialFile :
    
    listOfCredentials = line.strip().split('\t');
    username = listOfCredentials[0];
    passwd = listOfCredentials[1];

    for i in range(2):
        
        if i == 1:
            # Mobile search
            profile = webdriver.FirefoxProfile();
            profile.set_preference("general.useragent.override", "Mozilla/5.0 (iPhone; U; CPU like Mac OS X; en) AppleWebKit/420.1 (KHTML, like Gecko) Version/3.0 Mobile/3B48b Safari/419.3");
            browser = webdriver.Firefox(profile)
        else:
            # Desktop search
            browser = webdriver.Firefox();
         
        browser.get('https://login.live.com/');
        usernameBox = browser.find_element_by_name('loginfmt');
        usernameBox.send_keys(username);
        passwordBox = browser.find_element_by_name('passwd');
        passwordBox.send_keys(passwd + Keys.RETURN);
        time.sleep(5);

        browser.get('https://www.bing.com/');
        time.sleep(5);

        actions = webdriver.ActionChains(browser);
        searchBox = browser.find_element_by_name('q');
        actions.click(searchBox);
        randomWord = random.choice(get_list_of_random_words());
        print randomWord;
        searchBox.send_keys(randomWord + Keys.RETURN);
        time.sleep(5);
        browser.close();

credentialFile.close();
