from appium  import webdriver
class AppiumTest:
    def setup(self):
        self.desire_cap = {
            "platformName" :'Android',
            "deviceName":'127.0.0.1:52001',
            'appPackage':'',
            'appActivity':''
        }
        self.driver=webdriver.Remote('http://127.0.0.1:4723/wb/hub',self.desire_cap)
