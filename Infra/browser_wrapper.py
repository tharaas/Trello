from selenium import webdriver

from Utils.config_loader import ConfigLoader


class BrowserWrapper:
    def __init__(self):
        self.driver = None
        print('test has started')
        self.config_loader = ConfigLoader()
        self.config = self.config_loader.load_config()
        self.website_url = self.config['url']

    def set_up_capabilities(self, browser_type):
        options = None
        if browser_type.lower() == 'chrome':
            options = webdriver.ChromeOptions()
        elif browser_type.lower() == 'firefox':
            options = webdriver.FirefoxOptions()
        if options is not None:
            platform_name = self.config["platform"]
            options.add_argument(f'--platformName={platform_name}')
            return options
        else:
            raise ValueError("Unsupported browser type")

    def get_driver(self, browser='chrome'):
        if self.config["grid"]:
            options = self.set_up_capabilities(browser)
            self.driver = webdriver.Remote(command_executor=self.config["hub"], options=options)
        else:
            if browser == 'chrome':
                self.driver = webdriver.Chrome()
            elif browser == 'firefox':
                self.driver = webdriver.Firefox()
        url = self.config["url"]
        self.driver.get(url)
        self.driver.maximize_window()
        return self.driver
