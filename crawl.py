from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.common.exceptions import ElementNotInteractableException, StaleElementReferenceException
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions() 

options.add_argument('--user-data-dir=C:/Users/Lenovo/AppData/Local/Google/Chrome/User Data')
# options.add_argument('--profile-directory=Profile 1')

driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)

question_class_name = "q-box qu-display--block qu-cursor--pointer qu-hover--textDecoration--underline Link___StyledBox-t2xg9c-0 roKEj"
div_answer_amount = "q-text qu-dynamicFontSize--regular qu-medium qu-color--gray_dark qu-passColorToLinks"
div_answer_box = "CssComponent-sc-1oskqb9-0 cXjXFI"
div_answer_text = "q-text"
div_answer_nodelist_index = 7 #Where answer text (qtext) is at in the answer box
button_comment = "q-click-wrapper ClickWrapper___StyledClickWrapperBox-zoqi4f-0 bIwtPb base___StyledClickWrapper-lx6eke-1 laIUvT   qu-active--bg--darken qu-active--textDecoration--none qu-borderRadius--pill qu-alignItems--center qu-justifyContent--center qu-whiteSpace--nowrap qu-userSelect--none qu-display--inline-flex qu-tapHighlight--white qu-textAlign--center qu-cursor--pointer qu-hover--bg--darken qu-hover--textDecoration--none"
div_sub_comment_button = "q-relative qu-pb--small"

def define_js_function():
    driver.execute_script(open("./js/util.js").read())

def click_comment_btn():
    driver.execute_script(open("./js/click_comment_btn.js").read())
    driver.execute_script("window.click_comment_btn()")
    
def click_more_comment(max_iter=None):
    max_patient = 2
    count_stable = 0
    old_length = None
    while (True):
        clickable_divs = driver.execute_script("return document.getElementsByClassName(\"q-relative qu-pb--small\")")
        if old_length is not None:
            if old_length == len(clickable_divs): count_stable += 1
        if count_stable == max_patient or count_stable == max_iter: break
        for divs in clickable_divs:
            try: divs.click()
            except (ElementNotInteractableException, StaleElementReferenceException): continue
        time.sleep(3)
        print("more : iter :",count_stable)

def extract_answer_div():
    driver.execute_script(open("./js/extract_question.js").read())
    return driver.execute_script("return get_all_answer_div()")


def scroll(max_iter = None):
    lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    match=False
    count = 0
    while(match==False):
        lastCount = lenOfPage
        time.sleep(3)
        lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
        if lastCount==lenOfPage:
            match=True
        if max_iter is not None:
            if max_iter == count: break
        count += 1
    return

def question_scrapper(keyword,max_iter = None):
    driver.get("https://www.quora.com/search?q="+keyword)
    scroll(max_iter)
    element = driver.execute_script("return document.getElementsByClassName(\"" + question_class_name + "\"" + ")")
    result = []
    for e in element:
        result.append({"question":e.text, "url":e.get_attribute('href')})
    return result

define_js_function()

result = question_scrapper("covid",1)

for question in result:
    driver.get(question["url"])
    scroll(1)
    time.sleep(3)
    click_comment_btn()
    time.sleep(3)
    click_more_comment()
    # click_comment_btn()
    print(extract_answer_div())

    

print(result)