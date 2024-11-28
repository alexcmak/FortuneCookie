from win11toast import toast
from pathlib import Path
import random
import math
import time
import emoji
import argparse

#
# FortuneCookie.py 
#
# Alex Mak
#

def empty_func(args):
    pass


def send_toast(subject, msg, icon):

	toast(subject,
		msg,
		icon=str(Path(icon).resolve()),
	
		on_dismissed=empty_func
)

fortunes = []

def readFortunes(fileName):
	try:
		with open(fileName, "r") as f:
			for line in f:
				fortunes.append(line.rstrip("\n"))
	except IOError:
		print(f"Error: This game requires the fortunes.txt")

def getFortune():
	num = random.random()
	random_int = math.floor(num * len(fortunes))
	return fortunes[random_int]

def sendFortune(x,y, verbose):
	phrase = getFortune()
	tokens = phrase.split('|')

	message = tokens[0]
	icon = tokens[1] + '.ico'

	title = f'Fortune {x} of {y}'

	alias = ''
	if (icon == 'bicep.ico'):
		alias = ':flexed_biceps:'
	elif (icon == 'heart.ico'):
		alias = ':red_heart:'
	elif (icon == 'fortune.ico'):
		alias = ':fortune_cookie:'


	if (verbose):
		print(emoji.emojize(f'{alias} {message}'))

	send_toast(title, message, icon)

def main():

	descStr = "This program sends Windows notifications periodically."
	parser = argparse.ArgumentParser(description=descStr)

	parser.add_argument("-n", type=int, help="number of times")
	parser.add_argument("-s", type=int, help="number of seconds")
	parser.add_argument('-v', '--verbose', action='store_true') 

	args = parser.parse_args()

	n_times = args.n
	seconds = args.s

	if (n_times == None):
		n_times = 100

	if (seconds == None):
		seconds = 600

	print(f'Showing {n_times} fortunes, once every {seconds} seconds.')

	readFortunes("fortunes.txt")
	
	for x in range(1, n_times):
		sendFortune(x, n_times, args.verbose)
		time.sleep(seconds)

if __name__ == "__main__":
    main()