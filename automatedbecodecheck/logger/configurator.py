import tempfile
import configparser

class Config():
    def __init__(self):
        pass

    #If_configfile doesn't exist yet, generates a config_file with default options
    @staticmethod
    def config_set():
            config = configparser.ConfigParser()
            try :
                config.read(r"automatedbecodecheck/config/config.ini")
                print('Config file does exist.')
            except:
                print("config.ini doesn't exist yet, generating it")
                with open(r'automatedbecodecheck/config/config.ini', 'a+') as config:
                    if not config.has_section("PREFS") or not config.has_section("LOGIN_GITHUB"):
                        config.add_section("PREFS")
                        config.set("PREFS", "download.default_directory", "download_csv")
                        config.set("PREFS", "proxies", "")
                        config.set("PREFS","plugins.always_open_pdf_externally","True")
                        config.set("PREFS", "download.directory_upgrade", "True")
                        config.set("PREFS", "download.prompt_for_download", "False")
                        config.set("PREFS", "safebrowsing.enabled", "True")


    @staticmethod
    def config_read():
        
        # This is a configparser used often for securing/moving the configuration into a text file. 
        # I used for two purpose here, first to log my credentials somewhere and secondly to add a configuration to selenium for the undetected bot. 
        config = configparser.ConfigParser()
        config.read(r"automatedbecodecheck/config/config.ini")

        prefs = dict(config.items('PREFS'))
        return prefs
    
    @staticmethod
    def logging_set():
            config = configparser.ConfigParser()
            try :
                config.read(r"automatedbecodeccheck/config/logging.ini")
                print('logging file does exist.')
            except:
                print("logging.ini doesn't exist yet, generating it")
                with open(r'automatedbecodecheck/config/logging.ini', 'a+') as config:
                    if not config.has_section("LOGIN_GITHUB"):
                        config.add_section("LOGIN_GITHUB")
                        config.set("LOGIN_GITHUB", "login", "#putyourloginhere")
                        config.set("LOGIN_GITHUB", "password", "#putyourpasswordhere")
                        
    @staticmethod
    def logging_read():
        
        # This is a configparser used often for securing/moving the configuration into a text file. 
        # I used for two purpose here, first to log my credentials somewhere and secondly to add a configuration to selenium for the undetected bot. 
        config = configparser.ConfigParser()
        config.read(r"automatedbecodecheck/config/logging.ini")

        logging_creds = dict(config.items('LOGIN_GITHUB'))
        return logging_creds