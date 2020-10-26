import prompt
import os

def welcome_user():
	color_red = "\033[31m"
	color_green = "\033[32m"
	color_end = "\033[0m"
	head = """
	│                            
	├─┐┌─┌─┐╷┌─┐  ┌─┐┌─┐┌┬┐┌─┐╶─╴
	└─┘╵ └─┴╵╵ ╵  └─┤└─┴╵ ╵└─╴╶─╴
        	      ╶─┘            
"""
	
	print("{red}{dashes}{head}{dashes}{end}".format(
						red=color_red,
						dashes="=" * 45,
						head=head,
						end=color_end))
	print("Welcome to the Brain Games!")
	username = prompt.string("What's your name? {green}>>{end} ".format(green=color_green, end=color_end))
	print("Hello, {}".format(username))

	return username
