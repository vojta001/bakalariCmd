from __future__ import print_function
from cmd import Cmd
import getpass
import six
import os

try:
	from bakalari.bakalari import BakalariAPI
except ImportError:
	import sys
	try:
		sys.path.insert(0, os.path.abspath("bakalari"))
		from bakalari.bakalari import BakalariAPI
	except ImportError:
		print("*ERROR* `bakalari` module is missing")
		sys.exit(1)

class MainPrompt(Cmd):
	username = ""
	password = ""
	loggedIn = False
	url = ""
	api = None
	marks = None

	@staticmethod
	def parse_mark(mark):
		if isinstance(mark, six.string_types):
			if len(mark) == 0:
				return float(0)
			part = 0
			if mark.endswith('-'):
				part = 0.5
				mark = mark[0:-1]
			try:
				fMark = float(mark)
			except ValueError:
				return float(0)
			return fMark + part
		else:
			return float(0)

	def get_api(self):
		if not self.loggedIn:
			print("You have to be logged in!")
			self.onecmd("login")
		if self.api == None:
			self.api = BakalariAPI(self.username, self.password, self.url)
			self.api.login()
		return self.api

	def do_login(self, args):
		"""Log in to be able to make API calls (which is necessary to view the marks)"""
		eUrl = None
		eUsr = None
		ePas = None
		if "bakalariUrl" in os.environ:
			eUrl = os.environ["bakalariUrl"]
		if "bakalariUsr" in os.environ:
			eUsr = os.environ["bakalariUsr"]
			if "bakalariPas" in os.environ:
				ePas = os.environ["bakalariPas"]
		try:
			if eUrl == None:
				self.url = raw_input("url: ")
			else:
				self.url = raw_input("url [%s]: " % (eUrl))
				if self.url == "":
					self.url = eUrl
			if eUsr == None:
				self.username = raw_input("username: ")
			else:
				self.username = raw_input("username [%s]: " % (eUsr))
				if self.username == "":
					self.username = eUsr
		except NameError:
			if eUrl == None:
				self.url = input("url: ")
			else:
				self.url = input("url [%s]: " % (eUrl))
				if self.url == "":
					self.url = eUrl
			if eUsr == None:
				self.username = input("username: ")
			else:
				self.username = input("username [%s]: " % (eUsr))
				if self.username == "":
					self.username = eUsr
		if ePas == None:
			self.password = getpass.getpass("password: ")
		else:
			self.password = getpass.getpass("password [<password>]: ")
			if self.password == "":
				self.password = ePas
		self.api = None
		self.loggedIn = True

	def do_update(self, args):
		"""Flush the cache and download new marks"""
		api = self.get_api()
		self.marks = api.znamky()["predmet"]

	def do_all(self, args):
		"""Print summary of all marks"""
		if self.marks == None:
			print("Updating...")
			self.onecmd("update")
		for subject in self.marks:
			print(subject["zkratka"].upper(), end=": ")
			wAvgSum = 0
			wSum = 0
			if subject["znamky"] != None:
				marks = subject["znamky"]["znamka"]
				for mark in marks:
					value = MainPrompt.parse_mark(mark["znamka"])
					if value == 0:
						weight = 0
					else:
						weight = int(mark["vaha"])
					wAvgSum += value * weight
					wSum += weight
					print("%s(%d)" % (mark["znamka"], weight), end=" ")
			print("|", end=" ")
			if "ctvrt" in subject and subject["ctvrt"] != None:
				print("(%s)" % (subject["ctvrt"]), end="")
			if wSum == 0:
				wAvg = 0
			else:
				wAvg = round(wAvgSum / wSum, 2)
			print(" %.2f" % (wAvg))


if __name__ == '__main__':
	prompt = MainPrompt()
	prompt.prompt = '> '
	try:
		prompt.cmdloop()
	except KeyboardInterrupt:
		print("") # do not print the stacktrace, just a newline
