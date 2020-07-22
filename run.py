import random
import string

class Engine:

	def __init__(self):
		
		self.input_key = None
		self.input_key_new = ""
		self.letters = string.ascii_letters


	def _do(self):

		for i in self.input_key:
			i = random.choice(self.letters)
			self.input_key_new += i

	def _to_txt(self):

		with open("key.txt", "w+", encoding = "utf-8") as f:
			f.write(self.input_key_new)

	def _get_input(self):

		self.input_key = input("Text to be encrypted: ")

	def run(self):

		self._get_input()
		self._do()

		while True:

			tick = input("--------------\nTo txt file ? (y/n):\n--------------\n:")

			if (tick == "y"):
				self._to_txt()
				print("**************Writed to txt file.**************")
				break

			elif (tick == "n"):
				print("Quiting...")
				break

			else:
				print("Invalid option.")


app = Engine()
app.run()

