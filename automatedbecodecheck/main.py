from logger import configurator
from logger import browser_backbone as bb
from logger import Logger
from logger import Clock
from logger.becode_log import dict_button

if __name__ == '__main__':

    # Loads configuration & credentials 
    conf = configurator.Config()
    prefs = conf.config_read()
    log_creds = conf.logging_read()

    # Loads the options 
    options = bb.ChromeOptions()
    options.add_experimental_option("prefs", prefs)

    # These options could have been loaded from the config file but they're buggy, so I'd rather have them here for later purpose
    # options.add_experimental_option('useAutomationExtension', False)

    # This is a very important method, as most bot detectors actually detect the size of a windows to judge whether it's a human or a bot.
    options.add_argument('--start-maximized')

    # This disabled option allow for use without any window popping, probably fine to activate. Weirdly enough it's not detected by most detectors.
    # options.add_argument('--headless')       
        
    # Monitors the date and the time 
    curr_clock = Clock()
    hour_check = curr_clock.monitor_datetime()
           
    while hour_check not in dict_button.keys() :
        pass

    else:
        # Loads the uc browser    
        browser = bb.ChromeWithPrefs(options=options) 

        # Selenium will only create a session within the necessary timeframe, instead of always have it up
        logger = Logger(browser=browser)
        
        # if the hour is in the dict of the check in or check out, push the appropriate button
        logger.login_via_github(log_creds)
        logger.push_the_button(is_remote=False, hour_check=hour_check)