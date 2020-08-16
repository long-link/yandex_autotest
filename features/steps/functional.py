from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

path = r'chromedriver.exe'


# возможно в отдельный файл лучше
class YandexElements:
    LOCATOR_YANDEX_SEARCH_FIELD = (By.ID, 'text')
    LOCATOR_YANDEX_SUGGEST = (By.CLASS_NAME, 'mini-suggest__popup_visible')
    LOCATOR_YANDEX_FIRST_LINK = (By.XPATH, '//*[@id="search-result"]/li[1]/div/div[1]/div[1]/a/b')
    # как оказалось у яндекса есть две версии сайта(есть или нет картинки у элементов бара) где совсем
    # разная структура ссылок. И поиск страницы картинок по такому селектору не всегда проходит.
    LOCATOR_YANDEX_IMAGES_LINK = (By.XPATH, '//a[@data-id="images"]')
    LOCATOR_YANDEX_FIRST_IMG = (By.XPATH, '//*[@id="main"]/div/div/div[1]/div[1]/div/a')
    LOCATOR_YANDEX_ITEM_LEFT = (By.CLASS_NAME, 'cl-viewer-navigate__item_left')
    LOCATOR_YANDEX_ITEM_RIGHT = (By.CLASS_NAME, 'cl-viewer-navigate__item_right')


class Requests:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=path)
        self.driver.maximize_window()

    def get_request(self, url):
        return self.driver.get(url)

    def find_element(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator),
                                                    message=f'Search for locator "{locator}" gave no results')

    @staticmethod
    def check_url(first_link, link):
        assert link == first_link, f'first link is not "{link}""'

    @staticmethod
    def insert_text(elem, text):
        elem.send_keys(text)

    @staticmethod
    def press_enter(elem):
        elem.send_keys(Keys.ENTER)

    @staticmethod
    def click_on_element(elem):
        elem.click()

    def match_check(self, url):
        self.driver.switch_to.window(self.driver.window_handles[1])
        assert self.driver.current_url == url, f'Current page {self.driver.current_url} is' \
                                               f' not {url} yandex images'

    def first_img_link(self):
        current_link = self.driver.current_url
        # не знаю как лучше проверять то, что мы открыли изображение. В принципе ссылка указывает на это =>
        assert 'card' in current_link.split('/'), 'Current page is not image '
        return current_link

    def page_matching_check(self, first_link):
        current_link = self.driver.current_url
        assert current_link != first_link, 'Image not changed'

    def previous_page(self, first_link):
        current_link = self.driver.current_url
        assert current_link == first_link, 'Image is not first'

    def quit(self):
        self.driver.quit()

    # def check_switch_buttons(self, l_btn, r_btn):
    #     self.find_element(r_btn)
    #     try:
    #         self.find_element(l_btn)
    #     except TimeoutException:
    #         print('There is no back button as this is the first image')
