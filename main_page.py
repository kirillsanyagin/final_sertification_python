from base_page import BasePage
import yaml

with open('./locators.yaml') as f:
    locator = yaml.safe_load(f)


class MainPage(BasePage):
    def go_to_about_page(self):
        self.find_element(locator['LOCATOR_ABOUT_BUTTON']).click()