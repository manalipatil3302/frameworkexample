from selenium import webdriver
class configuration:
    chrome_path = r"C:\Users\New\PycharmProjects\Frameworks\drivers\chromedriver.exe"
    firefox_path=r"C:\Users\New\PycharmProjects\Frameworks\drivers\geckodriver.exe"
    edge_path=r"C:\Users\New\PycharmProjects\Frameworks\drivers\msedgedriver.exe"

    file_path = r'C:\Users\New\PycharmProjects\Frameworks\files\actitime.xlsx'
    sheet = 'LoginPageObjects'
    URL='https://demo.actitime.com/login.do'
    BROWSER_NAME="chrome"