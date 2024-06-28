from base_page import BasePage
import yaml

with open('./locators.yaml') as f:
    locator = yaml.safe_load(f)


class AboutPage(BasePage):
    def get_header_size(self):
        return self.get_element_property(locator['LOCATOR_ABOUT_HEADER'], 'font-size')