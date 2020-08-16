from behave import *
from functional import Requests, YandexElements

page_requests = Requests()
ya_elem = YandexElements()


# search in yandex
@Given('website "{url}"')
def step(context, url):
    page_requests.get_request(url)


@when('search field exist')
def step(context):
    context.search_field = page_requests.find_element(ya_elem.LOCATOR_YANDEX_SEARCH_FIELD)


@Then('write in search field "{text}"')
def step(context, text):
    page_requests.insert_text(context.search_field, text)


@Then('check that the suggestion table exist')
def step(context):
    page_requests.find_element(ya_elem.LOCATOR_YANDEX_SUGGEST)


@When('ENTER is pressed, search results appear')
def step(context):
    page_requests.press_enter(context.search_field)


@Then('first link is "{link}"')
def step(context, link):
    context.first_link = page_requests.find_element(ya_elem.LOCATOR_YANDEX_FIRST_LINK)
    page_requests.check_url(context.first_link.text, link)


# search image in yandex
@Given('website yandex "{url}"')
def step(context, url):
    page_requests.get_request(url)


@When('these is a link on images')
def step(context):
    context.img_link = page_requests.find_element(ya_elem.LOCATOR_YANDEX_IMAGES_LINK)


@Then('click on link')
def step(context):
    page_requests.click_on_element(context.img_link)


@When('current link "{url}"')
def step(context, url):
    page_requests.match_check(url)


@Then('click on first img')
def step(context):
    context.needed_element = page_requests.find_element(ya_elem.LOCATOR_YANDEX_FIRST_IMG)
    page_requests.click_on_element(context.needed_element)


@Then('img opens and there button back and forward buttons')
def step(context):
    context.first_img_link = page_requests.first_img_link()
    context.r_btn = page_requests.find_element(ya_elem.LOCATOR_YANDEX_ITEM_RIGHT)


@When('forward button is tap img chenges on next img')
def step(context):
    page_requests.click_on_element(context.r_btn)
    page_requests.page_matching_check(context.first_img_link)


@When('back button pressing, exist that we going back to first img')
def step(context):
    context.l_btn = page_requests.find_element(ya_elem.LOCATOR_YANDEX_ITEM_LEFT)
    page_requests.click_on_element(context.l_btn)
    page_requests.previous_page(context.first_img_link)
    page_requests.quit()
