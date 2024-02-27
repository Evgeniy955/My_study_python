from time import sleep
from selene.support.shared import browser

def implicitly_wait(time_func, element):
    while time_func != 0:
        # hub_screen.search_icon.should(be.visible)
        try:
            if element:
                break
            else:
                sleep(0.5)
                time_func -= 0.5
        except ElementExeption:
            print("Element not found")

implicitly_wait(10, hub_screen.search_icon.should(be.visible))
