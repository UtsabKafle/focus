import pyttsx3
import time
import sys


engine = pyttsx3.init()


class focus:
	def __init__(self,duration=None,work=None):
		self.mins = round(time.monotonic())
		self.duration = float(duration)
		assert type(duration) is int or float
		self.end = self.mins+(60*self.duration)
		self.work = work
		self.speak("Session started !")
		self.speak(f"Crush it.")
 

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
		self.speak("Session over")
		self.speak(f"Did you completed your task : {self.work}")
		done = input("y/n :: ")
		if "y" in done:
			self.speak("Well done. Keep going.")
		if "n" in done:
			self.speak("It is a shame for a man to grow old,")
			self.speak(" without seeing the beauty and strength his body")
			self.speak(" and knowledge and wisdom which his mind is capable of.")
		with open('focus_logs.txt','a+') as db:
			db.write(f"{str(time.asctime()) + ' ~ ' + str(self.duration)} minutes => {self.work} \n")

	def bye(self):
		self.speak("Keep working. Keep crushing.")


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
	a = focus(sys.argv[1],sys.argv[2])
	a.alarm()



if __name__ == "__main__":
	main()