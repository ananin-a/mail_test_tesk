from pages.base_page import BasePage
from locators.message_sent_page_locators import MessageSentPageLocators as MSPL


class MessageSentPage(BasePage):
    def close_sent_message_page(self):
        self.element_search(MSPL.BUTTON_CLOSE_WINDOW).click()
