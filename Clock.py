""""
Prequsite before Execution
1. Android Device/AVD
	Enable USB Debugging 
	Connect your device via USB/adb over Wifi 
	Verify Device is connected: "adb devices"
	Set Screen timeout to 30 minutes
	Set Screen lock to None 
2. Python 2/3
3. Install uiautomator
   pip install uiautomator
   uiautomator: This module is a Python wrapper of Android uiautomator testing framework.
4. AOSP Clock 

Author: Pranshu Pratyay 
"""

from uiautomator import device as d
import subprocess
import time

def Launch_clock():

	Launch_clock = subprocess.Popen('adb shell am start -a android.intent.action.MAIN -n com.google.android.deskclock/com.android.deskclock.DeskClock', stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE,shell=True)
	if Launch_clock.returncode:
		print("Clock App unable to launch")
	else:
		if d.exists(text="Stopwatch"):
			print("Clock App Launched Successfully")	
	Launch_clock.stdout.close()


def Test_Clock_1():
	"""Clock_1: To verify that user is able to Launch Clock""" 
 	print("TEST Clock_1: 'To verify that user is able to Launch Clock' ")
 	print("Execution Started")
 	try: 
	 	Launch_clock()
	 	time.sleep(1)
	 	d.press.back()
		print('Test Case "Clock_1: To verify that user is able to Launch Clock" executed successfully!! ')
	except:
		print("Test Case failed")

def Test_Clock_2():
	"""To verify that user is able to create an alarm""" 
 	print("TEST Clock_2: To verify that user is able to create an alarm")
 	print("Execution Started")
 	d.wakeup()

 	try:
 		Launch_clock()
	 	d(text="Alarm").click()
	 	time.sleep(2)
	  	if d(resourceId="com.google.android.deskclock:id/fab").click():
	 		if d(resourceId="android:id/toggle_mode").click():
	 			minutes = d(resourceId="android:id/input_minute").info
	 			setmin = int(minutes[u'text']) + 2
	 			print("Alarm created")
	 			print("Wait for 2 minutes")
	 	if d(resourceId="android:id/input_minute").exists:
	 		d(resourceId="android:id/input_minute").clear_text() # clear the text
			d(resourceId="android:id/input_minute").set_text(setmin)

		if d(text="OK").exists:
			d(text="OK").click()
			d.press.back()

		if d(text="DISMISS").wait.exists(timeout=120000):
			print("Alarm started ringing")
		 	if d.open.notification():
				if d(text="DISMISS").click():
					print("Alarm dismissed")
					d.press.back()
					print('Test Case "Clock_2: To verify that user is able to create an alarm" executed successfully!! ')
	except:
		print("Test Case failed")

def Test_Clock_4():
	"""Clock_1: To verify that user is able to Launch Clock""" 
 	print("TEST Clock_4: 'To verify that user is able to set a timer inside the clock app' ")
 	print("Execution Started")
 	try:
 		Launch_clock()
		if d(text="Timer").click():
			if d(text="Delete").exists:
				d(text="Delete").click()
			print("Timer opened ")
			d(text="2").click()
			d(text="0").click()
			d(resourceId="com.google.android.deskclock:id/fab").click()
			print("Countdown Started......")

		if d(text="STOP").wait.exists(timeout=20000):
			print("Time's up")
		 	if d.open.notification():
				if d(text="STOP").click():
					print("Timer Stopped")
					d.press.back()
					print('Test Case "Clock_4: To verify that user is able to set a timer inside the clock app" executed successfully!! ')
	except:
		print("Test Case failed")

def Test_Clock_5():
	"""Clock_1: To verify that user is able to Launch Clock""" 
 	print("TEST Clock_5: 'To verify that user is able to use stopwatch inside clock app' ")
 	print("Execution Started")
 	Launch_clock()
 	try:
		if d(text="Stopwatch").click():
			if d(text="Reset").exists:
				d(text="Reset").click()
			print("Stopwatch opened ")
			print("Test Case failed")
	except:
		print("Unable to Open Stopwatch ")
		print("Test Case failed")
	try:
		if d(resourceId="com.google.android.deskclock:id/fab").click():
			print("Stopwatch Started......")
			time.sleep(20)
			if d(text="Reset").click():
				print("Stopwatch Reseted")
				d.press.back()
				print('Test Case "Clock_5: To verify that user is able to use stopwatch inside clock app" executed successfully!! ')
	except:
		print("unable to start Stopwatch")
		print("Test Case failed")


def Test_Clock_3():
	"""Clock_1: To verify that user is able to Launch Clock""" 
 	print("TEST Clock_3: 'To verify that user is able to add time of different desired cities inside clock app' ")
 	print("Execution Started")
 	Launch_clock()
 	try:
		if d(text="Clock").click():
			if d(text="New York").exists:
				d(text="New York").drag.to(resourceId="com.google.android.deskclock:id/fab",steps=50)
				d(resourceId="com.google.android.deskclock:id/fab").click()
				d(resourceId="com.google.android.deskclock:id/search_src_text").set_text("New York")
				print("Desire city searched")
			else:
				d(resourceId="com.google.android.deskclock:id/fab").click()
				d(resourceId="com.google.android.deskclock:id/search_src_text").set_text("New York")
				print("Desire city searched")

	except:
		print("Unable to Search desired city")
		print("Test Case failed")

	d(resourceId="com.google.android.deskclock:id/city_name").wait.exists(timeout=10000)
	try:
		if d(resourceId="com.google.android.deskclock:id/city_name").click():
			if d(text="New York").exists:
				print("Time of desired city added in clock app")
				print('Test Case "Clock_3: To verify that user is able to add time of different desired cities inside clock app" executed successfully!! ')
	except:
		print("Unable to add time of different City")
		print("Test Case failed")

def Test_Clock_6():
	"""Clock_1: To verify that user is able to Launch Clock""" 
 	print("TEST Clock_6: 'To verify that user is able to access settings inside clock app' ")
 	print("Execution Started")
 	Launch_clock()
 	try:
		if d(description="More options").exists:
			d(description="More options").click()
			if d(text="Settings").exists:
				d(text="Settings").click()    
	except:
		print("Unable to Open Settings")
		print("Test Case failed")

	try:
		if d(text="Style").sibling(resourceId="android:id/summary").wait.exists(timeout=3000):
			print("User is able to access settings inside clock app")
 			print("Test Case TEST Clock_6: 'To verify that user is able to access settings inside clock app' executed successfully!! ")
 	except:
		print("Unable to access Settings")
		print("Test Case failed")		

def Test_Clock_7():
	"""Clock_1: To verify that user is able to Launch Clock""" 
 	print("TEST Clock_7: 'To verify that user is able to change Style to Digital inside clock app' ")
 	print("Execution Started")
 	Launch_clock()
 	try:
		if d(description="More options").exists:	
			d(description="More options").click()
		if d(text="Settings").exists:
			d(text="Settings").click()
		if d(text="Style").exists:
			d(text="Style").click()
		if d(text="Digital").exists:
			d(text="Digital").click()

	except:
		print("Unable to Open Settings")
		print("Test Case failed")

	try:
		if d(text="Digital").sibling(text="Style").exists:
			d.press.back()
			d(text="Clock").click()
			if d(resourceId="com.google.android.deskclock:id/digital_clock").exists:
				print("User is able to change Style to Digital clock app")
				print("Test Case TEST Clock_7: 'To verify that user is able to change Style to Digital inside clock app' executed successfully!! ")
	except:
		print("Unable to change Style to Digital clock app")
		print("Test Case failed")



def Test_Clock_8():
	"""Clock_1: To verify that user is able to Launch Clock""" 
 	print("TEST Clock_8: 'To verify that user is able to change Style to Analouge inside clock app' ")
 	print("Execution Started")
 	Launch_clock()
 	try:
		if d(description="More options").exists:	
			d(description="More options").click()
		if d(text="Settings").exists:
			d(text="Settings").click()
		if d(text="Style").exists:
			d(text="Style").click()
		if d(text="Analogue").exists:
			d(text="Analogue").click()

	except:
		print("Unable to Open Settings")
		print("Test Case failed")

	try:
		if d(text="Analogue").sibling(text="Style").exists:
			d.press.back()
			d(text="Clock").click()
			if d(resourceId="com.google.android.deskclock:id/analog_clock").exists:
				print("User is able to change Style to Digital clock app")
				print("Test Case TEST Clock_7: 'To verify that user is able to change Style to Analouge inside clock app' executed successfully!! ")
	except:
		print("Unable to change Style to Analouge clock app")
		print("Test Case failed")


Test_Clock_1()
Test_Clock_2()
Test_Clock_3()
Test_Clock_4()
Test_Clock_5()
Test_Clock_6()
Test_Clock_7()
Test_Clock_8()