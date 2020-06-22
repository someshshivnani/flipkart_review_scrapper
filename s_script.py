from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def run_script(text):
    options=webdriver.ChromeOptions()
    driver=webdriver.Chrome('chromedriver',chrome_options=options)
    wait = WebDriverWait(driver, 40)
    driver.get(f'https://www.flipkart.com/search?q={text}')
    button = driver.find_element_by_class_name('_3wU53n')

    button.click()

    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])

    x_arg = 'hGSR34'
    rating = wait.until(EC.presence_of_element_located((By.CLASS_NAME, x_arg)))
    rating = rating.text
    # print(f" average rating {rating.text}")

    total_usr = '_38sUEc'
    total = wait.until(EC.presence_of_element_located((By.CLASS_NAME, total_usr)))
    total_r = total.text

    # print(driver.current_url)

    vote_ul = '_148m3I'
    vote_review = wait.until(EC.presence_of_element_located((By.CLASS_NAME, vote_ul)))

    star_ul = '_2M5FGu'

    star_review = wait.until(EC.presence_of_element_located((By.CLASS_NAME, star_ul)))

    star_list = str(star_review.text)
    vote_list = str(vote_review.text)

    star_list = star_list.replace("★", " ")
    vote_list = vote_list.replace(",", "")

    star_list = star_list.split("\n")
    vote_list = vote_list.split("\n")

    def myfunc(a):
        return int(a)

    star = map(myfunc, star_list)
    star = list(star)

    votes = map(myfunc, vote_list)
    votes = list(votes)

    print(votes)
    print(star)
    positive_votes = votes[0] + votes[1]
    negative_votes = votes[3] + votes[4]
    neutral_votes = votes[2]

    total_votes = 0
    for i in range(len(votes)):
        total_votes = votes[i] + total_votes

    print(f"total votes= {total_votes}")
    print(f"neutral votes= {neutral_votes}")
    print(f"positive votes= {positive_votes}")
    print(f"negative votes= {negative_votes}")
    name = [total_votes, neutral_votes, positive_votes, negative_votes, rating, total_r]
    driver.quit()
    return name