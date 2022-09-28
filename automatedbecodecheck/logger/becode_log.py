from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Logger():
    
    global dict_button
    # These represent the check in and out button
    dict_button = {"button_9h":"/html/body/div/div[1]/div[2]/main/div/div[2]/div/div[2]/div[2]/button",
                    "button_12h3":"/html/body/div/div[1]/div[2]/main/div/div[2]/div/div[2]/div[3]/button",
                    "button_13h3":"/html/body/div/div[1]/div[2]/main/div/div[2]/div/div[2]/div[4]/button",
                    "button_17h":"/html/body/div/div[1]/div[2]/main/div/div[2]/div/div[2]/div[5]/button"}
            
    def __init__(self,browser):
        self.browser = browser

    def login_via_github(self, log_creds):
        
        browser = self.browser
        # Types the default url
        browser.get('https://my.becode.org/dashboard')

        # Looks and click on the github button
        button_fullpath = "/html/body/div/main/div/div/div/div/div[1]/button[1]"
        WebDriverWait(browser, 60).until(EC.presence_of_element_located((By.XPATH, button_fullpath)))
        browser.find_element(By.XPATH, button_fullpath).click()

        # Switches the browser to the new window
        browser.switch_to.window(browser.window_handles[1])

        # XPATH seems to be the best way to get the objects
        login_PATH = "/html/body/div[3]/main/div/div[3]/form/input[2]"
        password_PATH = "/html/body/div[3]/main/div/div[3]/form/div/input[1]"
        button_login = "/html/body/div[3]/main/div/div[3]/form/div/input[12]"

        # 1 min waiting in case the load is longer than expected
        WebDriverWait(browser, 60).until(EC.presence_of_element_located((By.XPATH, login_PATH)))

        # XPATH again
        browser.find_element(By.XPATH, login_PATH).send_keys(log_creds['login'])
        browser.find_element(By.XPATH, password_PATH).send_keys(log_creds['password'])
        browser.find_element(By.XPATH,button_login).click()
        
        # Returns the bot's attention the primary window
        browser.switch_to.window(browser.window_handles[0])
        

    def push_the_button(self,is_remote:bool==True,hour_check):
        
        browser = self.browser
        location_key = {"at_becode":"/html/body/div/div[1]/div[2]/main/div/div[2]/div/div[2]/div[1]/div/button[1]","at_home":"/html/body/div/div[1]/div[2]/main/div/div[2]/div/div[2]/div[1]/div/button[2]"}

        if is_remote == True :
            actual_loc = location_key["at_becode"]       
        else :
            actual_loc = location_key["at_home"]
        
        # push the right location button
        browser.find_element(By.XPATH,actual_loc).click()
        
        # push the right hour button
        browser.find_element(By.XPATH,dict_button[hour_check]).click()