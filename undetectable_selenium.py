#import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time


if __name__ == "__main__":
    import undetected_chromedriver as uc
    opts = uc.ChromeOptions()
    opts.add_argument("--window-size=1020,900")

    #select the brwser of choice
    broswer = uc.Chrome(options=opts)
    
    try:
        #get the url of the website to be accessed
        broswer.get('https://accounts.google.com/v3/signin/identifier?authuser=0&continue=https%3A%2F%2Fmyaccount.google.com%2F%3Futm_source%3Dsign_in_no_continue%26pli%3D1&ec=GAlAwAE&hl=en&service=accountsettings&flowName=GlifWebSignIn&flowEntry=AddSession&dsh=S657536056%3A1730558590594047&ddm=1')

        #email and the password to login with
        email = "lunaisluna09@gmail.com"
        password = "justluna."

        #get input element to access the webpage
        broswer.find_element(By.ID, 'identifierId').send_keys(email)

        #to access the the enter button on the page
        broswer.find_element(By.CSS_SELECTOR, '#identifierNext > div > button > span').click()

        #the next page to input the password
        password_selector = '#password > div.aCsJod.oJeWuf > div > div.Xb9hP > input'

        #wait for the element to load on the webpage
        WebDriverWait(broswer, 50).until(EC.visibility_of_element_located((By.CSS_SELECTOR, password_selector)))

        #input the password into the text box
        broswer.find_element(By.CSS_SELECTOR, password_selector).send_keys(password)

        #to access the the enter button on the page
        broswer.find_element(By.CSS_SELECTOR, '#passwordNext > div > button > span').click()

        time.sleep(4)
    except TimeoutException:
        print("An element was not found in time.")

    finally:
        # Use `close()` instead of `quit()`, and quit only if necessary
        try:
            broswer.close()
        except OSError:
            print("Handled an error on browser close.")
        finally:
            # Attempt to call quit if close didn’t work
            try:
                broswer.quit()
            except OSError:
                print("Handled an error on browser quit.")







