from time import sleep
from selene.support.shared import browser

# def implicitly_wait(time_func, element, condition):
#     while time_func != 0:

#         hub_screen.search_icon.with_(Config(timeout=10)).should(be.visible)
#
#         # element_with_condition = element + condition
#
#         sleep(0.5)
#         time_func -= 0.5
x = browser.element('//XCUIElementTypeButton[@name="close white"]').click()
element_with_condition = '//XCUIElementTypeButton[@name="close white"]' + '.click'
print(element_with_condition)
print(type(x))

# hub_screen = None  # Задаем hub_screen как None для примера
#
# # Ваша строка
# command_string = "hub_screen.search_icon.should(be.visible)"
#
# # Выполняем строку с помощью exec()
# exec(command_string)
