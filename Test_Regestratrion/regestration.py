from test_case_reg import TestCase
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

class Regestration(TestCase):

	def test_regestration(self):
	
		self.driver.get("http://automationpractice.com/index.php") #load test page
		
		# gather input data from xlsx file
		input = pd.read_excel("input_test_data_reg.xlsx")
		#print input.head()
		EMAIL = input['User_email'][0]
		PASSWORD = input['User_password'][0]
		FIRST_NAME = input['First_name'][0]
		LAST_NAME = input['Last_name'][0]
		DATE_OF_BIRTH = input['Day_of_birth'][0]
		MONTH_OF_BIRTH = input['Month_of_birth(1-Jan:12-Dec)'][0]
		YEAR_OF_BIRTH = input ['Year_of_birth(1-2020:41-1980)'][0]
		COMPANY = input['Company'][0]
		ADDRESS1 = input['Address1'][0]
		ADDRESS2 = input['Address2'][0]
		CITY = input['City'][0]
		STATE = input['State(1-Alabama itd.)'][0]
		ZIP_CODE = input['Zip_Code'][0]
		if ZIP_CODE:
			ZIP_CODE = str(ZIP_CODE) # change int values into string
		COUNTRY = input['Country(1-USA)'][0]
		ADD_INFO = input['Additional_information'][0]
		HOME_PHONE = input['Home_phone'][0]
		MOBILE_PHONE = input['Mobile_phone'][0]
		if MOBILE_PHONE:
			MOBILE_PHONE = str(MOBILE_PHONE) # change int values into string
		ALIAS = input['Alias'][0]
		
		time.sleep(3)
		#check if page title is proper
		try:
			if self.driver.title == "My Store":
				f = open("test_results.txt", "w")
				time.sleep(2)
				f.write("PASS : Web application was open correctly \n")
		except Exception:
			time.sleep(2)
			f.write("FAIL : Web application was not open correctly \n")
			self.fail("I couldn't enter website")
		# looking for login button	
		try:
			elem = self.driver.find_element_by_class_name("login")
			f.write("PASS : Scrypt found the login button \n")
		except Exception:
			f.write("FAIL : Scrypt could not find the login button n")
			self.fail("Link not found!")
		elem.click()
		time.sleep(3)
		# check if subpage load properly
		try:
			if self.driver.title == "Login":
				f.write("PASS : Scrypt etered the login page \n")
		except Exception:
			f.write("PASS : Scrypt could not enter the login page \n")
			self.fail("I couldn't enter the login page")
		# looking for email text field	
		try:
			time.sleep(3)
			elem = self.driver.find_element_by_name("email_create")
			f.write("PASS : Scrypt found email text field \n")
		except Exception:
			f.write("FAIL : Scrypt could not find the email text field \n")
			self.fail("I couldn't find text field for email creation")
		#entering new user email
		try:
			elem.clear()
			elem.send_keys(EMAIL)
			time.sleep(2)
			elem.send_keys(Keys.RETURN)
			time.sleep(3)
			f.write("PASS : Scrypt entered the email address \n")
		except Exception:
			f.write("FAIL : Scrypt could not eter email adress \n")
			self.fail("I couldn't enter email address")
		
		
		try:
			#PERSONAL DATA ENTERING
			elem = self.driver.find_element_by_id("uniform-id_gender1")
			elem.click()
			time.sleep(1)
			f.write("PASS : Scrypt choosen the gender \n")
			
			elem = self.driver.find_element_by_id("customer_firstname")
			elem.clear()
			elem.send_keys(FIRST_NAME)
			time.sleep(1)
			f.write("PASS : Scrypt entered the first name of the user \n")
			
			elem = self.driver.find_element_by_id("customer_lastname")
			elem.clear()
			elem.send_keys(LAST_NAME)
			time.sleep(1)
			f.write("PASS : Scrypt entered the last name of the user \n")
			
			elem = self.driver.find_element_by_id("email")
			elem.clear()
			elem.send_keys(EMAIL)
			time.sleep(1)
			f.write("PASS : Scrypt entered the email address of the user \n")
			
			elem = self.driver.find_element_by_id("passwd")
			elem.clear()
			elem.send_keys(PASSWORD)
			time.sleep(1)
			f.write("PASS : Scrypt entered the user password \n")
			
			elem = self.driver.find_element_by_id("days")
			elem.click()
			for x in range(DATE_OF_BIRTH):
				elem.send_keys(Keys.DOWN)
				elem.send_keys(Keys.RETURN)
			time.sleep(1)
			f.write("PASS : Scrypt choosen the day of birth of the user \n")
			
			elem = self.driver.find_element_by_id("months")
			elem.click()
			for x in range(MONTH_OF_BIRTH):
				elem.send_keys(Keys.DOWN)
				elem.send_keys(Keys.RETURN)
			time.sleep(1)
			f.write("PASS : Scrypt choosen the month of birth of the user \n")
			
			elem = self.driver.find_element_by_id("years")
			elem.click()
			for x in range(YEAR_OF_BIRTH):
				elem.send_keys(Keys.DOWN)
				time.sleep(0.1)
			elem.send_keys(Keys.RETURN)
			time.sleep(1)
			f.write("PASS : Scrypt choosen the year of birth of the user \n")
			
			elem = self.driver.find_element_by_id("newsletter")
			elem.click()
			time.sleep(1)
			f.write("PASS : Scrypt choosen to receive newsletter from application \n")
			
			elem = self.driver.find_element_by_id("optin")
			elem.click()
			time.sleep(1)
			f.write("PASS : Scrypt choosen to receive optin from application \n")
			
			#USER ADDRESS ADDRESS ENTERING
			
			elem = self.driver.find_element_by_id("company")
			elem.clear()
			elem.send_keys(COMPANY)
			time.sleep(1)
			f.write("PASS : Scrypt entered user company name \n")
			
			elem = self.driver.find_element_by_id("address1")
			elem.clear()
			elem.send_keys(ADDRESS1)
			time.sleep(1)
			f.write("PASS : Scrypt entered user address \n")
			
			elem = self.driver.find_element_by_id("city")
			elem.clear()
			elem.send_keys(CITY)
			time.sleep(1)
			f.write("PASS : Scrypt entered user city \n")
					
			elem = self.driver.find_element_by_id("id_country")
			elem.click()
			elem.send_keys(Keys.DOWN)
			elem.send_keys(Keys.RETURN)
			time.sleep(1)
			f.write("PASS : Scrypt entered user country \n")
			
			elem = self.driver.find_element_by_id("id_state")
			elem.click()
			elem.send_keys(Keys.DOWN)
			elem.send_keys(Keys.RETURN)
			time.sleep(1)
			f.write("PASS : Scrypt entered user state \n")
			
			elem = self.driver.find_element_by_id("postcode")
			elem.clear()
			elem.send_keys("55555")
			time.sleep(1)
			f.write("PASS : Scrypt entered user postcode \n")
			
			elem = self.driver.find_element_by_id("phone_mobile")
			elem.clear()
			elem.send_keys("123456789")
			time.sleep(1)
			f.write("PASS : Scrypt entered user phone number \n")
			
			elem = self.driver.find_element_by_id("alias")
			elem.clear()
			elem.send_keys(ALIAS)
			time.sleep(1)
			f.write("PASS : Scrypt entered user alias \n")
			
			elem = self.driver.find_element_by_id("submitAccount")
			time.sleep(1)
			elem.click()
			f.write("PASS : Scrypt have submitted the account \n")
			
		except:
			f.write("FAIL : Scrypt could not fill all regestration fields \n")
			self.fail("I couldn't fill all regestration fields")
		time.sleep(3)
		# check if new user was created and if account subpage was loaded
		try:
			if self.driver.title == "My account - My Store":
				f.write("PASS : Scrypt created user account and enter to it \n")
		except Exception:
			f.write("FAIL : Scrypt din not create user account \n")
			self.fail("I couldn't create my account")
		f.close()