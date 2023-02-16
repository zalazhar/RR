from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from selenium.webdriver import FirefoxOptions

options = FirefoxOptions()
options.add_argument("--start-maximized")
options.set_preference("print.always_print_silent", True)
options.set_preference("print.printer_Mozilla_Save_to_PDF.print_to_file", True)
options.set_preference("print_printer", "Mozilla Save to PDF")



import time
import logging
import os


def init_browser(): 
    
    profile_path = "/Users/zalazhar/Library/Application Support/Firefox/Profiles/2ije50f5.default-release"

    driver = webdriver.Firefox(options = options) 
    
    url = driver.command_executor._url       #"http://127.0.0.1:60622/hub"
    #driver = webdriver.Remote(command_executor=url,desired_capabilities={})
    session_id = driver.session_id

    return driver



def get_pdf(url = "https://issuu.pdf-downloader.com/",  rr_file ="https://issuu.com/reviewofreligions/docs/nov_1904", to_path= "/Users/zalazhar/projects/RR/pdfs" ):



    #after initialization and setting: 
    try: 
        driver = init_browser()
        driver.get(url)

        text_box_xhr =   '//*[@id="issuuurl"]' 
        text_box = driver.find_element(By.XPATH, text_box_xhr) 

        file_name =  rr_file.replace("https://issuu.com/reviewofreligions/docs/","")

        text_box.send_keys(rr_file)

        button_download_xhr = '//*[@id="download"]'
        button_download = driver.find_element(By.XPATH, button_download_xhr)
        button_download.click()

        time.sleep(15)
        button_print_xhr = '//*[@id="download"]'
        button_print = driver.find_element(By.XPATH, button_print_xhr)
        button_print.click()

        time.sleep(10)

        window_after = driver.window_handles[1]
        driver.switch_to.window(window_after)
        time.sleep(5)
        driver.execute_script("window.print();")

        time.sleep(30)
        driver.quit()  

        os.system(f"cp mozilla.pdf {to_path}/{file_name}.pdf")
    except:
        print("error")


def get_pdf_titles(url = "https://issuu.com/reviewofreligions"):
    driver = init_browser()
    driver.get(url)

    time.sleep(10)
    
    SCROLL_PAUSE_TIME = 0.5

# Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
    elems = driver.find_elements(By.CLASS_NAME, "ixu-link")
    links = []
    for elem in elems:
        links.append(elem.get_attribute("href"))
    
    #undouble the links
    links = list(set(links))
    

    driver.close()
    return (links)


