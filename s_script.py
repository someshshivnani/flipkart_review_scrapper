import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def run_script(text):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
    wait = WebDriverWait(driver, 5)
    driver.get(f'https://www.flipkart.com/search?q={text}')

    try:
        b_arg = '_3wU53n'
        button = driver.find_element_by_class_name(b_arg)
    except:
        b_arg = '_2cLu-l'
        button = driver.find_element_by_class_name(b_arg)
    button.click()

    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])

    x_arg = 'hGSR34'
    rating = wait.until(EC.presence_of_element_located((By.CLASS_NAME, x_arg)))

    rating = rating.text

    total_usr = '_38sUEc'
    total = wait.until(EC.presence_of_element_located((By.CLASS_NAME, total_usr)))
    total_r = total.text

    # print(driver.current_url)


    try:
        vote_ul = '_148m3I'
        vote_review = wait.until(EC.presence_of_element_located((By.CLASS_NAME, vote_ul)))
    except:
        vote_ul = '_2M5FGu'
        vote_review = wait.until(EC.presence_of_element_located((By.CLASS_NAME, vote_ul)))

    image_arg = '/html/body/div[1]/div/div[3]/div[2]/div[1]/div[1]/div[1]/div/div[1]/div[2]/div[1]/div[2]/img'

    image = wait.until(EC.presence_of_element_located((By.XPATH, image_arg)))

    vote_list = str(vote_review.text)

    vote_list = vote_list.replace(",", "")

    vote_list = vote_list.split("\n")

    price = '_1uv9Cb'
    price_x = wait.until(EC.presence_of_element_located((By.CLASS_NAME, price)))
    price_x=price_x.text
    def myfunc(a):
        return int(a)

    votes = map(myfunc, vote_list)
    votes = list(votes)

    # print(votes)
    # print(star)
    positive_votes = votes[0] + votes[1]
    negative_votes = votes[3] + votes[4]
    neutral_votes = votes[2]

    image_src = image.get_attribute('src')
    total_votes = 0
    for i in range(len(votes)):
        total_votes = votes[i] + total_votes
    name = [total_votes, neutral_votes, positive_votes, negative_votes, rating, total_r, image_src,price_x]
    driver.quit()
    return name
