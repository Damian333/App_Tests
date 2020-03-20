from test_case_log import TestCase
import time
import pandas as pd

class Login(TestCase):

	def test_login(self):

		self.driver.get("http://automationpractice.com/index.php") # load test page
		
		time.sleep(2)
		#gather input data from xlsx file
		input = pd.read_excel("input_test_data.xlsx")

		EMAIL = input['User_email'][0]
		PASSWORD = input['User_password'][0]
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
			f.write("PASS : Login button was found")
		except Exception:
			f.write("FAIL : Scrypt could not find login button")
			self.fail("Link not found!")
		elem.click()
		time.sleep(3)
		# check if subpage load properly
		try:
			if self.driver.title == "Login - My Store":
				f.write("PASS : Scrypt etered the login page \n")
		except Exception:
			f.write("FAIL : Scrypt could not enter the login page")
			self.fail("I couldn't enter the login page")
		# loking for login and password text files
		try:
			time.sleep(3)
			elem = self.driver.find_element_by_name("email")
			f.write("PASS : Scrypt found email text field \n")
		except Exception:
			f.write("FAIL : Scrypt could not find the email text field \n")
			self.fail("I couldn't find text field for email creation")	
				
		try:
			elem.clear()
			elem.send_keys(EMAIL)
			f.write("PASS : Scrypt entered the email address \n")
		except Exception:
			f.write("FAIL : Scrypt could not eter email adress \n")
			self.fail("I couldn't enter email address")
		time.sleep(1)
		
		try:
			time.sleep(1)
			elem = self.driver.find_element_by_name("passwd")
			f.write("PASS : Scrypt found password text field \n")
		except Exception:
			f.write("FAIL : Scrypt could not find the password text field \n")
			self.fail("I couldn't fill text field for email creation")
			
		try:
			time.sleep(1)
			elem.clear()
			elem.send_keys(PASSWORD)
			time.sleep(2)
			#elem.send_keys(Keys.RETURN)
			f.write("PASS : Scrypt filled the password field \n")
		except Exception:
			f.write("FAIL : Scrypt could not enter user account \n")
			self.fail("I could not fill the password text file")
		# submitting user input
		try:
			time.sleep(1)
			elem = self.driver.find_element_by_id("SubmitLogin")
			f.write("PASS : Scrypt have submited login data \n")
		except Exception:
			f.write("FAIL : Scrypt could not submit login data \n")
		elem.click()
		time.sleep(3)
		# check if application load user account
		try:
			if self.driver.title == "My account - My Store":
				f.write("PASS : Scrypt entered user account \n")
		except Exception:
			time.sleep(2)
			f.write("FAIL : Scrypt did not enter user account \n")
			self.fail("I couldn't enter user account")
		f.close()
		time.sleep(2)
		