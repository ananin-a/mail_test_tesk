from selenium.webdriver.common.by import By


class MessageSentPageLocators:
    """Locators on the sent messages page"""
    BUTTON_CLOSE_WINDOW = (By.XPATH, '//span[@tabindex="1000"]')