import pyttsx3
import time
import sys
import pynput
from pynput.keyboard import Controller, Key
engine = pyttsx3.init()

keyboard = Controller()

class waste:
	def __init__(self,duration=None,work=None):
		self.mins = round(time.monotonic())
		self.duration = float(duration)
		assert type(duration) is int or float
		self.end = self.mins+(60*self.duration)
		self.work = work
		self.speak("Session started !")
		self.speak(f"use it wisely.")
 

	def get_time(self):
		self.mins = round(time.monotonic())
		return self.mins

	def set_alarm(self,duration):
			self.after = self.get_time() + duration


	def speak(self,text):
		engine.say(text)
		print(text)
		engine.runAndWait()

	def ask(self):
		with open('waste_logs.txt','a+') as db:
			db.write(f"{str(time.asctime()) + ' ~ ' + str(self.duration)} minutes => {self.work} \n")

	def quit_(self):
		with keyboard.pressed(Key.alt):
			keyboard.press(Key.f4)
			keyboard.release(Key.f4)

	def enter(self):
		keyboard.press(Key.enter)

	def bye(self):
		self.quit_()
		self.quit_()
		self.enter()
		self.speak("done.")
		self.speak("Start working.")


	def alarm(self):
		c_hour = self.get_time()
		r_time = self.end - c_hour
		if self.end:
			if int(self.end)  < int(c_hour):
				self.ask()
				self.bye()

			else:
				print(f"{round(r_time/60)} minutes remaining")
				time.sleep(10)
				self.alarm()
		

def main():
	# print()
	a = waste(sys.argv[1],sys.argv[2])
	a.alarm()



if __name__ == "__main__":
	main()