#!/usr/bin python
# -*- coding: utf-8 -*-

# Klementynka Engine 1.2.2 BETA
# Program jest przystosowany do czatu na serwerze GC2.PL

if __name__ == '__main__':
	__version__ = "1.2.2 BETA"
	
	try:
		from os import path, makedirs, remove, listdir, system
		from pyautogui import typewrite, hotkey, press
		from shutil import rmtree
		from time import strftime
		import zipfile
		import colorama
	except Exception as error_message:
		with open('error.log', 'a') as error_log_file:
			error_log_file.write("Klementynka crashed!\nError message: "+str(error_message)+"\n\n")
		system('crash_msg.vbs')
		raise SystemExit # CRASH!

	def color_print(color, text):
		colorama.init(autoreset = True)
		if color == 'red':
			color_to_print = colorama.Fore.RED
		elif color == 'green':
			color_to_print = colorama.Fore.GREEN
		elif color == 'yellow':
			color_to_print = colorama.Fore.YELLOW
		elif color == 'blue':
			color_to_print = colorama.Fore.BLUE
		elif color == 'magenta':
			color_to_print = colorama.Fore.MAGENTA
		elif color == 'cyan':
			color_to_print = colorama.Fore.CYAN
		else:
			color_to_print = colorama.Fore.WHITE
		print colorama.Style.BRIGHT+color_to_print+text
		colorama.deinit()

	config_filename = 'config.dat'

	system('title Klementynka')

	color_print('cyan', "Klementynka Engine "+__version__+"\n")
	print " _   ___                           _               _         "
	print "| | / / |                         | |             | |        "
	print "| |/ /| | ___ _ __ ___   ___ _ __ | |_ _   _ _ __ | | ____ _ "
	print "|    \| |/ _ \ '_ ` _ \ / _ \ '_ \| __| | | | '_ \| |/ / _` |"
	print "| |\  \ |  __/ | | | | |  __/ | | | |_| |_| | | | |   < (_| |"
	print "\_| \_/_|\___|_| |_| |_|\___|_| |_|\__|\__, |_| |_|_|\_\__,_|"
	print "                                        __/ |                "
	print "                                       |___/                 "
	print ""

	if not path.exists(config_filename):
		color_print('red', "Brakuje pliku '"+config_filename+"' wymaganego do uruchomienia programu.")
		print ""
		system('pause')
		raise SystemExit

	if not path.exists('cmd'):
		color_print('red', "Brakuje folderu 'cmd' wymaganego do uruchomienia programu.")
		print ""
		system('pause')
		raise SystemExit
		
	logs_filename = open(config_filename).read().rstrip()

	try:
		logs = open(logs_filename)
	except IOError:
		color_print('red', "Dane w pliku config.dat sa niepoprawne.")
		print ""
		system('pause')
		raise SystemExit

	system('pause')
	color_print('magenta', "Bot uruchomiony!")
	print "\n"

	def msg_send(msg):
		typewrite('t')
		hotkey('ctrl', 'a')
		hotkey('backspace')
		typewrite(msg)
		hotkey('enter')

	def get_commander_nick(message):
		__temp__user_msg_list = message.split(' ')
		if __temp__user_msg_list[1] == '[':
			pass
		if __temp__user_msg_list[1] == '(':
			pass
		else:
			user_nick = __temp__user_msg_list[2]
		if user_nick[-1] == ':':
			user_nick = user_nick[:-1]
		return user_nick

	def get_target_nick(message):
		__temp__user_msg_list = message.split(' ')
		if __temp__user_msg_list[1] == '[':
			pass
		if __temp__user_msg_list[1] == '(':
			pass
		else:
			target_nick = __temp__user_msg_list[4]
		return target_nick

	def kill_running_cmd():
		build_files = listdir('build')
		main_files = listdir('.')
		try:
			for f in build_files:
				if path.isfile(f):
					remove(f)
				if path.isdir(f):
					rmtree(f)
			for f in main_files:
				if f.endswith('.pyc'):
					os.remove(os.path.join('.', f))
			rmtree('build')
		except Exception as warning_message:
			with open('error.log', 'a') as error_log_file:
				error_log_file.write("["+strftime('%Y-%m-%d %H:%M:%S')+"] Klementynka almost crashed...\nWARNING: "+str(warning_message)+"\n\n")
			return

	logs_size = int(path.getsize(logs_filename))

	lines = logs.readlines()
	if lines:
		first_line = lines[:1]
		last_line = lines[-1]

	try:
		user_msg = ' '.join(last_line.split(' ')[4:])
	except ValueError:
		pass

	print user_msg+"\n"

	while True:
		if logs_size < int(path.getsize(logs_filename)):
			logs_size = int(path.getsize(logs_filename))
			lines = logs.readlines()
			if lines:
				first_line = lines[:1]
				last_line = lines[-1]
			try:
				user_msg = ' '.join(last_line.split(' ')[4:])
			except ValueError:
				pass
			print user_msg+"\n"
			try:
				user_nick = get_commander_nick(user_msg)
				target_nick = get_target_nick(user_msg)
			except IndexError:
				pass
			commands_list = listdir('cmd')
			commands = []
			for cmd_file in commands_list:
				commands.append(path.splitext(cmd_file)[0])
			for cmd in commands:
				if '!'+cmd in user_msg:
					try:
						makedirs('build')
						try:
							zip_ref = zipfile.ZipFile('cmd/'+cmd+'.zip', 'r')
							zip_ref.extractall('build/')
							zip_ref.extractall('.')
							zip_ref.close()
						except:
							pass
						try:
							color_print('yellow', "Trwa wykonywanie komendy !"+cmd+"...")
							execfile('__main__.py')
							kill_running_cmd()
							color_print('green', "Koniec.\n")
						except SystemExit:
							kill_running_cmd()
						except:
							color_print('red', "Dzialanie komendy zostalo niespodziewanie przerwane.\n")
							error_message = "The operation of the command (!"+cmd+") has been unexpectedly interrupted. Possible cause: the command parameters were not specified or were incorrect."
							with open('error.log', 'a') as error_log_file:
								error_log_file.write("["+strftime('%Y-%m-%d %H:%M:%S')+"] Klementynka almost crashed...\nWARNING: "+str(error_message)+"\n\n")
							kill_running_cmd()
					except Exception as error_message:
						kill_running_cmd()
						with open('error.log', 'a') as error_log_file:
							error_log_file.write("["+strftime('%Y-%m-%d %H:%M:%S')+"] Klementynka crashed!\nError message: "+str(error_message)+"\n\n")
						system('crash_msg.vbs')
						raise SystemExit # CRASH!
