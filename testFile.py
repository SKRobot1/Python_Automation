'''
Finding and building strong Xpath
Finding the price of Python programing course on the page
'''

from selenium import webdriver
from selenium.webdriver.common.by import By

class BuildingXpath():

    def test_parent_and_childXpath(self):
         #initiate the driver
        baseURL='https://learn.letskodeit.com/p/practice'
        driver= webdriver.Firefox()
        driver.get(baseURL)
        elem1= driver.find_element(By.XPATH, "//h1[contains(text(), 'Practice Page')]")
        if elem1 is not None:
            print("Login  successfull")

            #find the price of Python course
        try:
            price = driver.find_element(By.XPATH, "//table[@id='product']//td[contains(text(), 'Python Programming Language')]//following-sibling::td ")
            if price is not None:
                txt=price.text
                print("The price of Python Programming course is:" +" $" +str(txt))
        except:
             print("Exception Error: Element not found")

        finally:
             driver.quit()

my_Cl= BuildingXpath()
my_Cl.test_parent_and_childXpath()


