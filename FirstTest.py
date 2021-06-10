from selenium import webdriver
driver = webdriver.Chrome(executable_path="C:\\Users\Varun Malhotra\\Downloads\\chromedriver_win32 (1)\\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.google.com")
driver.add_cookie()
mypageTitle=driver.title
print(mypageTitle)
assert "Google" in mypageTitle
driver.quit()