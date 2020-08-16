Feature: Checking search

    Scenario: search in yandex
    Given website "https://yandex.ru/"
    When search field exist
    Then write in search field "Тензор"
    Then check that the suggestion table exist
    When ENTER is pressed, search results appear
    Then first link is "tensor.ru"

    Scenario: search img in yandex
    Given website yandex "https://yandex.ru/"
    When these is a link on images
    Then click on link
    When current link "https://yandex.ru/images/"
    Then click on first img
    Then img opens and there button back and forward buttons
    When forward button is tap img chenges on next img
    When back button pressing, exist that we going back to first img

