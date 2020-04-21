# code not clean

import subprocess,sys,time,random,getpass

def install(name):
    subprocess.call(['pip3', 'install', name])

try:
    from selenium import webdriver
except ImportError:
    install("selenium")
    from selenium import webdriver

try:
    from webdriver_manager.chrome import ChromeDriverManager
except:
    install("webdriver-manager")
    from webdriver_manager.chrome import ChromeDriverManager
        
from selenium.webdriver.common.keys import Keys

if __name__=='__main__':

    args = sys.argv
    n=len(args)

    if n>1:
        url = args[1]
    if n>2:
        code = args[2]
    if n>3:
        email = args[3]
    if n>4:
        passwd = args[4]
    if n>5:
        delay = args[5]
    if n<2:
        url = input('Enter your test url: ')
    if n<3:
        code = input('Enter your test code: ')
    if n<4:
        email = input('Enter your email: ')
    if n<5:
        passwd = getpass.getpass()

    delay = 2
    delay = min(60*60,delay)

    if url[:4]!='http':
        url='https://'+url

    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)

    try:
        driver.get(url)
    except:
        print('\33[91m'+'INVALID URL'+'\033[0m')
        exit()

    for i in driver.find_elements_by_tag_name("a"):
        if i.get_attribute("text")=="Get Started":
            i.click()
            break

    for i in driver.find_elements_by_tag_name("input"):
        if i.get_attribute("name")=="log_userName":
            i.send_keys(email)
        if i.get_attribute("name")=="log_pwd":
            i.send_keys(passwd)
        if i.get_attribute("value")=="Log In":
            i.click()
            break
    try:
        found=False
        for i in driver.find_elements_by_tag_name("input"):
            if i.get_attribute("name")=="activationCode":
                i.send_keys(code)
                found=True
            if found and i.get_attribute("value")=="Get Started":
                i.click()
                break
    except:
        print('\33[91m'+'INVALID LOGIN CREDENTIALS'+'\033[0m')
        exit()

    time.sleep(5)


    try:
        for i in driver.find_elements_by_tag_name("input"):
            if i.get_attribute("value")=="Continue":
                i.click()
                break
    except:
        print('\33[91m'+'INVALID TEST CODE'+'\033[0m')
        exit()

    time.sleep(5)

    ids = 0
    for i in driver.find_elements_by_tag_name("a"):
        if i.get_attribute("id")[:2]=="id":
            ids+=1

    for cnt in range(1,ids+1):
        options=[]

        for i in driver.find_elements_by_tag_name("input"):
            if i.get_attribute("id")=="ch"+str(cnt):
                options.append(i)

        button=random.choice(options)

        button.click()

        if cnt!=ids:
            driver.find_element_by_id("id_"+str(cnt+1)).click()

    time.sleep(delay)

    for i in driver.find_elements_by_tag_name("input"):
        if i.get_attribute("id")=="sub":
            i.click()
            break

    time.sleep(7)

    alert_obj2 = driver.switch_to.alert
    time.sleep(7)
    alert_obj2.accept() 
    