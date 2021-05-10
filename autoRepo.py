from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

import time

import os


def createRepo(uname, pswd, repoName):
    driver = webdriver.Chrome(executable_path=r'D:\\Driver\\chromedriver.exe')

    driver.get('https://github.com/new')

    # username = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='login']")))
    # password = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

    username = driver.find_element_by_css_selector("input[type='text']")
    password = driver.find_element_by_css_selector("input[type='password']")

    username.clear()
    password.clear()

    username.send_keys(uname)
    password.send_keys(pswd)
    # username.send_keys('checkRepo')
    # password.send_keys('mob.publications1')

    driver.find_element_by_css_selector("input[type='submit']").click()

    name = driver.find_element(By.ID, 'repository_name')
    name.clear()
    name.send_keys(repoName)
    # name.send_keys('testRepo1')

    time.sleep(2)

    if driver.find_element_by_class_name("btn-primary").is_enabled():
        driver.find_element_by_class_name("btn-primary").click()
    else:
        print('A repository with this name is already created on your account. Try with a different name.')
        # print(f'Your repository with name {repoName} was created!!!')

    return driver.current_url

def commit(url):
    os.system("git init -b main")
    os.system("git add .")
    os.system('git commit -m "First commit"')
    os.system(f"git remote add origin {url}")
    os.system("git push origin main")

if __name__ == "__main__":

    print("\t\t*********Creaditentials*********")
    uname = input("GitHub username or email >>> ")
    pswd = input('GitHub Password >>> ')
    repoName = input("Name of Repository >>> ")

    url = createRepo(uname, pswd, repoName)
    print(f"\nYour Repo url: {url}")

    commit(url)