from framework.web_driver.webdriver_factory import WebDriverFactory
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('-b', '--browser', dest='browser',
                    help='Browser name on which the tests will be run i.e. firefox, chrome',
                    metavar="BROWSER")
args = parser.parse_args()
print(args)

if __name__ == "__main__":
    # 0. install webdrivers automatically (chromedriver, geckodriver, ie driver, safaridriver)
    # 0.1. read input arguments and decide which browser to test
    selected_web_driver = WebDriverFactory.by_browser_name(args.browser)
    selected_web_driver.install()
    selected_web_driver.get()
    # 1. automatically create venv if it does not exist already
    # python -m venv

    # 2. check if all dependencies are installed
    # 4. run all tests using pytest
