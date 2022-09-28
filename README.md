# BeCode_Logger

## Why

I didn't want to make an actual logger, I felt it would be a path of trouble to actually use it. But as a proof of concept, I thought the project was fun to try and create, as myBecode dashboard was actually sensing any "bot" used, so I took it as a challenge. 
An easier solution would be to send the same requests. 

## How 

This project revolves mostly around Selenium, the whole idea is to make it undetectable and people have already did so (eg: Undetected_browser module ), I needed to make the closest human-like logger.
*Note* : This project is actually very messy and amateurish, I solve a lot of issues with small fixes that aren't that secure. I'm improving on it whenever I understand better ways to do it. I invite you to fork, ask me or suggest any other method. You can even practice by adding a linkedin option. 

### Prefs

After running into problems to create an undetected instance with prefs, I used this [solution](https://github.com/ultrafunkamsterdam/undetected-chromedriver/issues/524) as a single unit incorporated into the whole project. The prefs are configuration for Selenium to tweak the automated browser and avoid simple bot detection.
 
### Clock monitor

Another decision I've made is to expect that application to be a stand-alone, to run in the background/in a server/on docker, rather than be launched either manually around the hours of check-in or via a cronjob, which would have been the easiest way. I felt that activating it from outside the script itself would defeat the purpose of automated logging. Hence the is the clock_monitor project.

### Project structure 

```bash
.
├── automatedbecodecheck        ## Project Folder
│   ├── config                  ## Configuration Folder 
│   │   ├── config.ini
│   │   └── logging.ini
│   ├── driver                  ## Drivers for chrome browser
│   │   └── chromedriver
│   ├── logger                  ## Python Submodules Folder
│   │   ├── becode_log.py       ## HTML targetting for login and check-in
│   │   ├── browser_backbone.py ## Selenium configuration to be undetected
│   │   ├── clock_monitor.py    ## Simple date and time monitor
│   │   ├── configurator.py     ## Config reader & creator with confParser
│   │   └── __init__.py
│   └── main.py ## main py file to manage everything

```


## Installation 

```
git clone https://github.com/BSD-Yassin/BeCode_Logger
cd BeCode_Logger
pip3 -r install requirements.txt
```

## Setup Post-configuration

*These instruction are not optional.* 


### Chrome

The easiest way to get the browser working is to get Chrome installed in your distribution. Per default Selenium will look for the Chrome path to get the driver (Without interfering with your local Chrome !)

##### Chromedriver (optional)

You don't necessarly need to use the chrome driver to run it, but you can tinker with the execution path and the chrome path, or even change it to another browser, it doesn't take much work.  More infos on [here](https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/)

### Github Login

- Edit the *logging_template.ini* file with your login and password and remove the *logging.ini* 
If you are experiencing an error on this step, you are probably using a password with a special character. So you have to double a adding the special character, or escape it.


--------- 


"Oh no, I'm soooo going to be late
because I never learned to clock in with Python"


<img src="https://www.cornel1801.com/disney/Alice-Wonderland-1951/characters/im-late-for-a-very-important-date.jpg " width="200" height="200" />    
