Для запуска нужен установленый фреймворк behave + 
 selenium WebDriver:

`pip install behave`

`pip install selenium`

Запуска осуществляется из дериктории с файлом README командой -

`behave -i yandex_test.feature`

Само тестирование происходит в хроме с помощью
chromedriver, который уже присутствует в проекте.