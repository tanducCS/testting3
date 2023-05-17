import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import NoSuchElementException


class Utils:
    def login(driver):
        wait = WebDriverWait(driver, 10)    
        username = wait.until(EC.element_to_be_clickable((By.ID, "username")))
        username.clear()
        username.send_keys("student")
        password = driver.find_element(by=By.ID, value="password")
        password.clear()
        password.send_keys("moodle")
        password.send_keys(Keys.RETURN)

class GradeSettingTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service("./chromedriver"))
        self.driver.maximize_window()
        self.driver.get("https://school.moodledemo.net/login/index.php")
        Utils.login(self.driver)
        self.driver.get("https://school.moodledemo.net/mod/assign/view.php?id=999&action=editsubmission")
    def test_0(self):
        driver = self.driver
        
        # Wait for the element to become visible and enabled
        wait = WebDriverWait(driver, 100)

        # AAAAAAAAA

        save_and_returntocourse = wait.until(EC.element_to_be_clickable((By.ID, "id_submitbutton")))
        save_and_returntocourse.click()

        assert "https://school.moodledemo.net/mod/assign/view.php?id=999&action=view" == driver.current_url
    def test_1(self):
        driver = self.driver
        
        # Wait for the element to become visible and enabled
        wait = WebDriverWait(driver, 100)

        # AAAAAAAAA
        addfilebutton = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "fp-btn-add")))
        addfilebutton.click()

        
        #addfilebutton_1 = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "nav-link active")))
        # addfilebutton_1.click()

        addfilebutton1 = wait.until(EC.element_to_be_clickable((By.NAME, 'repo_upload_file')))
        addfilebutton1.send_keys("D:\\HK_222\\KtraPM\\Prj3\\testcase2\\1.txt")

        

        uploadbutton = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Upload this file')]")))
        uploadbutton.click()


        save_and_returntocourse = wait.until(EC.element_to_be_clickable((By.ID, "id_submitbutton")))
        save_and_returntocourse.click()

        assert "https://school.moodledemo.net/mod/assign/view.php?id=999&action=view" == driver.current_url
    def test_2(self):
        driver = self.driver
        
        # Wait for the element to become visible and enabled
        wait = WebDriverWait(driver, 100)

        # AAAAAAAAA
        addfilebutton = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "fp-btn-add")))
        addfilebutton.click()

        
        #addfilebutton_1 = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "nav-link active")))
        # addfilebutton_1.click()

        addfilebutton1 = wait.until(EC.element_to_be_clickable((By.NAME, 'repo_upload_file')))
        addfilebutton1.send_keys("D:\\HK_222\\KtraPM\\Prj3\\testcase2\\2.txt")

        

        uploadbutton = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Upload this file')]")))
        uploadbutton.click()


        save_and_returntocourse = wait.until(EC.element_to_be_clickable((By.ID, "id_submitbutton")))
        save_and_returntocourse.click()

        assert "https://school.moodledemo.net/mod/assign/view.php?id=999&action=view" == driver.current_url
    def test_3(self):
        driver = self.driver
        
        # Wait for the element to become visible and enabled
        wait = WebDriverWait(driver, 100)

        # AAAAAAAAA
        addfilebutton = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "fp-btn-add")))
        addfilebutton.click()

        
        #addfilebutton_1 = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "nav-link active")))
        # addfilebutton_1.click()

        addfilebutton1 = wait.until(EC.element_to_be_clickable((By.NAME, 'repo_upload_file')))
        addfilebutton1.send_keys("D:\\HK_222\\KtraPM\\Prj3\\testcase2\\3.txt")

        

        uploadbutton = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Upload this file')]")))
        uploadbutton.click()


        save_and_returntocourse = wait.until(EC.element_to_be_clickable((By.ID, "id_submitbutton")))
        save_and_returntocourse.click()

        assert "https://school.moodledemo.net/mod/assign/view.php?id=999&action=view" == driver.current_url
    def test_4(self):
        driver = self.driver
        
        # Wait for the element to become visible and enabled
        wait = WebDriverWait(driver, 100)

        # AAAAAAAAA
        addfilebutton = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "fp-btn-add")))
        addfilebutton.click()

        
        #addfilebutton_1 = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "nav-link active")))
        # addfilebutton_1.click()

        addfilebutton1 = wait.until(EC.element_to_be_clickable((By.NAME, 'repo_upload_file')))
        addfilebutton1.send_keys("D:\\HK_222\\KtraPM\\Prj3\\testcase2\\4.txt")

        

        uploadbutton = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Upload this file')]")))
        uploadbutton.click()


        save_and_returntocourse = wait.until(EC.element_to_be_clickable((By.ID, "id_submitbutton")))
        save_and_returntocourse.click()

        assert "https://school.moodledemo.net/mod/assign/view.php?id=999&action=view" == driver.current_url
    def test_5(self):
        driver = self.driver
        
        # Wait for the element to become visible and enabled
        wait = WebDriverWait(driver, 100)

        # AAAAAAAAA
        addfilebutton = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "fp-btn-add")))
        addfilebutton.click()

        
        #addfilebutton_1 = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "nav-link active")))
        # addfilebutton_1.click()

        addfilebutton1 = wait.until(EC.element_to_be_clickable((By.NAME, 'repo_upload_file')))
        addfilebutton1.send_keys("D:\\HK_222\\KtraPM\\Prj3\\testcase2\\5.txt")

        

        uploadbutton = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Upload this file')]")))
        uploadbutton.click()


        save_and_returntocourse = wait.until(EC.element_to_be_clickable((By.ID, "id_submitbutton")))
        save_and_returntocourse.click()

        assert "https://school.moodledemo.net/mod/assign/view.php?id=999&action=view" == driver.current_url
    def test_6(self):
        driver = self.driver
        
        # Wait for the element to become visible and enabled
        wait = WebDriverWait(driver, 100)

        # AAAAAAAAA
        addfilebutton = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "fp-btn-add")))
        addfilebutton.click()

        
        #addfilebutton_1 = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "nav-link active")))
        # addfilebutton_1.click()

        addfilebutton1 = wait.until(EC.element_to_be_clickable((By.NAME, 'repo_upload_file')))
        addfilebutton1.send_keys("D:\\HK_222\\KtraPM\\Prj3\\testcase2\\6.txt")

        

        uploadbutton = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Upload this file')]")))
        uploadbutton.click()


        save_and_returntocourse = wait.until(EC.element_to_be_clickable((By.ID, "id_submitbutton")))
        save_and_returntocourse.click()

        assert "https://school.moodledemo.net/mod/assign/view.php?id=999&action=view" == driver.current_url
    def test_7(self):
        driver = self.driver
        
        # Wait for the element to become visible and enabled
        wait = WebDriverWait(driver, 100)

        # AAAAAAAAA
        addfilebutton = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "fp-btn-add")))
        addfilebutton.click()

        
        #addfilebutton_1 = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "nav-link active")))
        # addfilebutton_1.click()

        addfilebutton1 = wait.until(EC.element_to_be_clickable((By.NAME, 'repo_upload_file')))
        addfilebutton1.send_keys("D:\\HK_222\\KtraPM\\Prj3\\testcase2\\7.txt")

        

        uploadbutton = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Upload this file')]")))
        uploadbutton.click()


        save_and_returntocourse = wait.until(EC.element_to_be_clickable((By.ID, "id_submitbutton")))
        save_and_returntocourse.click()

        assert "https://school.moodledemo.net/mod/assign/view.php?id=999&action=view" == driver.current_url
    def test_8(self):
        driver = self.driver
        
        # Wait for the element to become visible and enabled
        wait = WebDriverWait(driver, 100)

        # AAAAAAAAA
        addfilebutton = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "fp-btn-add")))
        addfilebutton.click()

        
        #addfilebutton_1 = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "nav-link active")))
        # addfilebutton_1.click()

        addfilebutton1 = wait.until(EC.element_to_be_clickable((By.NAME, 'repo_upload_file')))
        addfilebutton1.send_keys("D:\\HK_222\\KtraPM\\Prj3\\testcase2\\8.txt")

        

        uploadbutton = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Upload this file')]")))
        uploadbutton.click()


        save_and_returntocourse = wait.until(EC.element_to_be_clickable((By.ID, "id_submitbutton")))
        save_and_returntocourse.click()

        assert "https://school.moodledemo.net/mod/assign/view.php?id=999&action=view" == driver.current_url
    def test_9(self):
        driver = self.driver
        
        # Wait for the element to become visible and enabled
        wait = WebDriverWait(driver, 100)

        # AAAAAAAAA
        addfilebutton = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "fp-btn-add")))
        addfilebutton.click()

        
        #addfilebutton_1 = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "nav-link active")))
        # addfilebutton_1.click()

        addfilebutton1 = wait.until(EC.element_to_be_clickable((By.NAME, 'repo_upload_file')))
        addfilebutton1.send_keys("D:\\HK_222\\KtraPM\\Prj3\\testcase2\\9.txt")

        

        uploadbutton = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Upload this file')]")))
        uploadbutton.click()


        save_and_returntocourse = wait.until(EC.element_to_be_clickable((By.ID, "id_submitbutton")))
        save_and_returntocourse.click()

        assert "https://school.moodledemo.net/mod/assign/view.php?id=999&action=view" == driver.current_url
    def test_10(self):
        driver = self.driver
        
        # Wait for the element to become visible and enabled
        wait = WebDriverWait(driver, 100)

        # AAAAAAAAA
        addfilebutton = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "fp-btn-add")))
        addfilebutton.click()

        
        #addfilebutton_1 = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "nav-link active")))
        # addfilebutton_1.click()

        addfilebutton1 = wait.until(EC.element_to_be_clickable((By.NAME, 'repo_upload_file')))
        addfilebutton1.send_keys("D:\\HK_222\\KtraPM\\Prj3\\testcase2\\10.txt")

        

        uploadbutton = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Upload this file')]")))
        uploadbutton.click()


        save_and_returntocourse = wait.until(EC.element_to_be_clickable((By.ID, "id_submitbutton")))
        save_and_returntocourse.click()

        assert "https://school.moodledemo.net/mod/assign/view.php?id=999&action=view" == driver.current_url
    def test_11(self):
        driver = self.driver
        
        # Wait for the element to become visible and enabled
        wait = WebDriverWait(driver, 100)

        # AAAAAAAAA
        addfilebutton = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "fp-btn-add")))
        addfilebutton.click()

        
        #addfilebutton_1 = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "nav-link active")))
        # addfilebutton_1.click()

        addfilebutton1 = wait.until(EC.element_to_be_clickable((By.NAME, 'repo_upload_file')))
        addfilebutton1.send_keys("D:\\HK_222\\KtraPM\\Prj3\\testcase2\\11.txt")

        

        uploadbutton = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Upload this file')]")))
        uploadbutton.click()


        save_and_returntocourse = wait.until(EC.element_to_be_clickable((By.ID, "id_submitbutton")))
        save_and_returntocourse.click()

        assert "https://school.moodledemo.net/mod/assign/view.php?id=999&action=view" == driver.current_url
    def test_12(self):
        driver = self.driver
        
        # Wait for the element to become visible and enabled
        wait = WebDriverWait(driver, 100)

        # AAAAAAAAA
        addfilebutton = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "fp-btn-add")))
        addfilebutton.click()

        
        #addfilebutton_1 = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "nav-link active")))
        # addfilebutton_1.click()

        addfilebutton1 = wait.until(EC.element_to_be_clickable((By.NAME, 'repo_upload_file')))
        addfilebutton1.send_keys("D:\\HK_222\\KtraPM\\Prj3\\testcase2\\12.txt")

        

        uploadbutton = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Upload this file')]")))
        uploadbutton.click()


        save_and_returntocourse = wait.until(EC.element_to_be_clickable((By.ID, "id_submitbutton")))
        save_and_returntocourse.click()

        assert "https://school.moodledemo.net/mod/assign/view.php?id=999&action=view" == driver.current_url
    def test_13(self):
        driver = self.driver
        
        # Wait for the element to become visible and enabled
        wait = WebDriverWait(driver, 100)

        # AAAAAAAAA
        addfilebutton = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "fp-btn-add")))
        addfilebutton.click()

        
        #addfilebutton_1 = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "nav-link active")))
        # addfilebutton_1.click()

        addfilebutton1 = wait.until(EC.element_to_be_clickable((By.NAME, 'repo_upload_file')))
        addfilebutton1.send_keys("D:\\HK_222\\KtraPM\\Prj3\\testcase2\\13.txt")

        

        uploadbutton = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Upload this file')]")))
        uploadbutton.click()


        save_and_returntocourse = wait.until(EC.element_to_be_clickable((By.ID, "id_submitbutton")))
        save_and_returntocourse.click()

        assert "https://school.moodledemo.net/mod/assign/view.php?id=999&action=view" == driver.current_url
    def test_14(self):
        driver = self.driver
        
        # Wait for the element to become visible and enabled
        wait = WebDriverWait(driver, 100)

        # AAAAAAAAA
        addfilebutton = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "fp-btn-add")))
        addfilebutton.click()

        
        #addfilebutton_1 = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "nav-link active")))
        # addfilebutton_1.click()

        addfilebutton1 = wait.until(EC.element_to_be_clickable((By.NAME, 'repo_upload_file')))
        addfilebutton1.send_keys("D:\\HK_222\\KtraPM\\Prj3\\testcase2\\14.txt")

        

        uploadbutton = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Upload this file')]")))
        uploadbutton.click()


        save_and_returntocourse = wait.until(EC.element_to_be_clickable((By.ID, "id_submitbutton")))
        save_and_returntocourse.click()

        assert "https://school.moodledemo.net/mod/assign/view.php?id=999&action=view" == driver.current_url
    def test_15(self):
        driver = self.driver
        
        # Wait for the element to become visible and enabled
        wait = WebDriverWait(driver, 100)

        # AAAAAAAAA
        addfilebutton = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "fp-btn-add")))
        addfilebutton.click()

        
        #addfilebutton_1 = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "nav-link active")))
        # addfilebutton_1.click()

        addfilebutton1 = wait.until(EC.element_to_be_clickable((By.NAME, 'repo_upload_file')))
        addfilebutton1.send_keys("D:\\HK_222\\KtraPM\\Prj3\\testcase2\\15.txt")

        

        uploadbutton = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Upload this file')]")))
        uploadbutton.click()


        save_and_returntocourse = wait.until(EC.element_to_be_clickable((By.ID, "id_submitbutton")))
        save_and_returntocourse.click()

        assert "https://school.moodledemo.net/mod/assign/view.php?id=999&action=view" == driver.current_url
    def test_16(self):
        driver = self.driver
        
        # Wait for the element to become visible and enabled
        wait = WebDriverWait(driver, 100)

        # AAAAAAAAA
        addfilebutton = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "fp-btn-add")))
        addfilebutton.click()

        
        #addfilebutton_1 = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "nav-link active")))
        # addfilebutton_1.click()

        addfilebutton1 = wait.until(EC.element_to_be_clickable((By.NAME, 'repo_upload_file')))
        addfilebutton1.send_keys("D:\\HK_222\\KtraPM\\Prj3\\testcase2\\16.txt")

        

        uploadbutton = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Upload this file')]")))
        uploadbutton.click()


        save_and_returntocourse = wait.until(EC.element_to_be_clickable((By.ID, "id_submitbutton")))
        save_and_returntocourse.click()

        assert "https://school.moodledemo.net/mod/assign/view.php?id=999&action=view" == driver.current_url
    def test_17(self):
        driver = self.driver
        
        # Wait for the element to become visible and enabled
        wait = WebDriverWait(driver, 100)

        # AAAAAAAAA
        addfilebutton = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "fp-btn-add")))
        addfilebutton.click()

        
        #addfilebutton_1 = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "nav-link active")))
        # addfilebutton_1.click()

        addfilebutton1 = wait.until(EC.element_to_be_clickable((By.NAME, 'repo_upload_file')))
        addfilebutton1.send_keys("D:\\HK_222\\KtraPM\\Prj3\\testcase2\\17.txt")

        

        uploadbutton = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Upload this file')]")))
        uploadbutton.click()


        save_and_returntocourse = wait.until(EC.element_to_be_clickable((By.ID, "id_submitbutton")))
        save_and_returntocourse.click()

        assert "https://school.moodledemo.net/mod/assign/view.php?id=999&action=view" == driver.current_url
    def test_18(self):
        driver = self.driver
        
        # Wait for the element to become visible and enabled
        wait = WebDriverWait(driver, 100)

        # AAAAAAAAA
        addfilebutton = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "fp-btn-add")))
        addfilebutton.click()

        
        #addfilebutton_1 = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "nav-link active")))
        # addfilebutton_1.click()

        addfilebutton1 = wait.until(EC.element_to_be_clickable((By.NAME, 'repo_upload_file')))
        addfilebutton1.send_keys("D:\\HK_222\\KtraPM\\Prj3\\testcase2\\18.txt")

        

        uploadbutton = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Upload this file')]")))
        uploadbutton.click()


        save_and_returntocourse = wait.until(EC.element_to_be_clickable((By.ID, "id_submitbutton")))
        save_and_returntocourse.click()

        assert "https://school.moodledemo.net/mod/assign/view.php?id=999&action=view" == driver.current_url
    def test_19(self):
        driver = self.driver
        
        # Wait for the element to become visible and enabled
        wait = WebDriverWait(driver, 100)

        # AAAAAAAAA
        addfilebutton = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "fp-btn-add")))
        addfilebutton.click()

        
        #addfilebutton_1 = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "nav-link active")))
        # addfilebutton_1.click()

        addfilebutton1 = wait.until(EC.element_to_be_clickable((By.NAME, 'repo_upload_file')))
        addfilebutton1.send_keys("D:\\HK_222\\KtraPM\\Prj3\\testcase2\\19.txt")

        

        uploadbutton = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Upload this file')]")))
        uploadbutton.click()


        save_and_returntocourse = wait.until(EC.element_to_be_clickable((By.ID, "id_submitbutton")))
        save_and_returntocourse.click()

        assert "https://school.moodledemo.net/mod/assign/view.php?id=999&action=view" == driver.current_url
    def test_20(self):
        driver = self.driver
        
        # Wait for the element to become visible and enabled
        wait = WebDriverWait(driver, 100)

        # AAAAAAAAA
        addfilebutton = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "fp-btn-add")))
        addfilebutton.click()

        
        #addfilebutton_1 = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "nav-link active")))
        # addfilebutton_1.click()

        addfilebutton1 = wait.until(EC.element_to_be_clickable((By.NAME, 'repo_upload_file')))
        addfilebutton1.send_keys("D:\\HK_222\\KtraPM\\Prj3\\testcase2\\20.txt")

        

        uploadbutton = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Upload this file')]")))
        uploadbutton.click()


        save_and_returntocourse = wait.until(EC.element_to_be_clickable((By.ID, "id_submitbutton")))
        save_and_returntocourse.click()

        assert "https://school.moodledemo.net/mod/assign/view.php?id=999&action=view" == driver.current_url
    def test_21(self):
        driver = self.driver
        
        # Wait for the element to become visible and enabled
        wait = WebDriverWait(driver, 100)

        # AAAAAAAAA
        addfilebutton = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "fp-btn-add")))
        addfilebutton.click()

        
        #addfilebutton_1 = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "nav-link active")))
        # addfilebutton_1.click()

        addfilebutton1 = wait.until(EC.element_to_be_clickable((By.NAME, 'repo_upload_file')))
        addfilebutton1.send_keys("D:\\HK_222\\KtraPM\\Prj3\\testcase2\\21.txt")

        

        uploadbutton = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Upload this file')]")))
        uploadbutton.click()


        save_and_returntocourse = wait.until(EC.element_to_be_clickable((By.ID, "id_submitbutton")))
        save_and_returntocourse.click()

        assert "https://school.moodledemo.net/mod/assign/view.php?id=999&action=view" == driver.current_url
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
