from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

    # Initialize WebDriver
driver = webdriver.Chrome()

    # Set explicit wait
wait = WebDriverWait(driver, 10)

def login():


    # Navigate to the login page
    driver.get('https://hemis.buxiu.uz/')

    # Locate the login fields
    username_field = driver.find_element(By.ID, 'formadminlogin-login')
    password_field = driver.find_element(By.ID, 'formadminlogin-password')

    # Enter credentials
    username_field.send_keys('admin')
    password_field.send_keys('admin2809')

    # Wait for the CAPTCHA image to appear (in case it loads dynamically)
    #captcha_image = wait.until(lambda driver: driver.find_element(By.ID, 'formadminlogin-recaptcha-image').get_attribute('src') != '')
    #captcha_image = wait.until(EC.presence_of_element_located((By.ID, 'formadminlogin-recaptcha-image')))

    # Pause to let you manually solve the CAPTCHA
    input("Solve the CAPTCHA manually, then press Enter to continue...")

    # Submit the form after CAPTCHA is solved
    login_button = driver.find_element(By.XPATH, '//button[@type="submit"]')
    login_button.click()

    time.sleep(3)

    driver.get('https://hemis.buxiu.uz/student/student-edit')
    # Perform further automation after login
def add():

    #Specialty
    specialty_dropdown = wait.until(
    EC.presence_of_element_located((By.ID, '_specialty')))

    # # Step 3: Wait for options to be populated in the specialty dropdown
    # wait.until(lambda driver: len(specialty_dropdown.find_elements(By.TAG_NAME, "option")) > 1)

    # # Step 4: Select an option in the specialty dropdown
    # select_specialty = Select(specialty_dropdown)
    # select_specialty.select_by_value('1') 



    # Interact with elements on the page after login
    passport_number = driver.find_element(By.ID, "passport_number")
    passport_number.send_keys('AD5093306')


    passport_pin = driver.find_element(By.ID, "passport_pin")
    passport_pin.send_keys('62712066400019')


    # Locate the button using XPath based on its onclick function
    search_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@onclick="getCaptchaInfo()"]')))

    # Click the button
    search_button.click()

    # Pause to let you manually solve the CAPTCHA
    input("Solve the CAPTCHA manually, then press Enter to continue...")

      # Locate the button using XPath based on its onclick function
    get_passport_info = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@onclick="getPassportInfo()"]')))

    # Click the button
    get_passport_info.click()

     #Department
    department_dropdown = wait.until(EC.presence_of_element_located((By.ID, '_department')))
    department_select = Select(department_dropdown)
    department_select.select_by_index(1) 

    #Payment
    payment_form_dropdown = wait.until(EC.presence_of_element_located((By.ID, '_payment_form')))
    payment_form_select = Select(payment_form_dropdown)
    payment_form_select.select_by_value("12") 

    #Enroll
    enroll_dropdown = wait.until(EC.presence_of_element_located((By.ID, 'estudent-_decree_enroll')))
    enroll_form_select = Select(enroll_dropdown)
    enroll_form_select.select_by_value("83") 

    student_other = driver.find_element(By.ID, "estudent-other")
    student_other.send_keys('abc')


    time.sleep(10)

    submit_btn = driver.find_element(By.ID, 'submitButton')
    submit_btn.click()

    time.sleep(2)
    driver.get('https://hemis.buxiu.uz/student/student')



login()
add()

# Optional: Wait for a confirmation message or any further actions
# time.sleep(20)

# Close the browser
# driver.quit()


