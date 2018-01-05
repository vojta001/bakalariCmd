from cmd import Cmd
import getpass

try:
	from bakalari.bakalari import BakalariAPI
except ImportError:
	try:
		from .bakalari.bakalari import BakalariAPI
	except ImportError:
		import sys
		print("*ERROR* `bakalari` module is missing")
		sys.exit(1)

class MainPrompt(Cmd):
	username = ""
	password = ""
	url = ""
	api = None
	marks = None

	def get_api(self):
		if self.api == None:
			self.api = BakalariAPI(self.username, self.password, self.url)
			self.api.login()
		return self.api

	def do_login(self, args):
		"""Log in to be able to make API calls (which is necessary to view the marks)"""
		try:
			self.url = raw_input("url: ")
			self.username = raw_input("username: ")
		except NameError:
			self.url = input("url: ")
			self.username = input("username: ")
		self.password = getpass.getpass("password: ")
		self.api = None

	def do_update(self, args):
		"""Flush the cache and download new marks"""
		api = self.get_api()
		self.marks = api.znamky()

	def do_all(self, args):
		"""Print summary of all marks"""
		print(self.marks)


if __name__ == '__main__':
	prompt = MainPrompt()
	prompt.prompt = '> '
	try:
		prompt.cmdloop()
	except KeyboardInterrupt:
		print("") # do not print the stacktrace, just a newline
