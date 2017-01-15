from robot.libraries.BuiltIn import BuiltIn
from selenium import webdriver
import Selenium2Library
import time
  
  
class LibTests(object):
	def __init__(self):
		# Including Selenium2Library
		self._selenium2lib  = BuiltIn().get_library_instance('Selenium2Library')
		
	def waitForTimeout(self, xpath, timeout):
		# Sets Timeout if there is no xpath on the screen
		BuiltIn().log("1: Before setting timeout")
		secondsToWait = int(timeout);
		BuiltIn().log("2: Before checking loop")
		while True:
			BuiltIn().log("3: before mathing xpath")
			count = self._selenium2lib.get_matching_xpath_count(xpath)
			BuiltIn().log("4: before checking results of matching")
			if count > "0":
				BuiltIn().log("5: matched - GO")
				break
			elif secondsToWait == 0:
				BuiltIn().log("6: there is no xpath in the screen but the timeout exceeded ")
				self.CaptureScreenShot()
				BuiltIn().fail("Waiting for xpath %s seconds timeout exceeded (xpath %s found %s times)" % (timeout, xpath, count))
			else:
				BuiltIn().log("7: there is no xpath in the screen - waiting 1 second")
				time.sleep(1)
				BuiltIn().log("8: consuming 1 second of timeout")
				secondsToWait = secondsToWait - 1
				BuiltIn().log("9: repeating the xpath matching")