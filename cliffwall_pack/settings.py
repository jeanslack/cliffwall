#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
#########################################################
# Name: settings.py (module)
# Porpose: Management of custom rules and storage iptables settings
# Writer: Gianluca Pernigoto <jeanlucperni@gmail.com>
# Copyright: (c) 2013-2015 Gianluca Pernigoto <jeanlucperni@gmail.com>
# license: GPL3
# Version: (Ver.0.11) Friday, 29 July 2012
# Rev (v0.13) 04/02/2015
# Rev (v0.13) 09/02/2015
#########################################################

"""
Module called by /etc/rc.d/rc.firewall. It is consists of two
classes for management options and personal firewall rules.
The class Main_Menu is a derivated (child) class instantiated by 
daemon > settings that inherits from the class Rules_Applied . 
The class Rules_Applied is a simple base class for cmd parameters .
"""
from subprocess import call
import sys
import shelve
from docstring import *

####################################################################

	
class Rules_Applied(object):
	"""
	here are applied all the rules regarding the blocking of web pages 
	and the rules regarding the protocols tcp and udp .
	Also, displays UI formated graphic info that show you the
	current settings of tcp/udp and block sites rules
	
	"""
	############################### BLOCK WEB PAGES RULES
	def IP_insert(self, address, description):
		"""
		Applied rules for blocked webpages
		"""
		
		diz = shelve.open('%s/sites_block.db'% self.pathDB,'c')
		
		if diz.has_key(address) is False:
			
			diz[address] = description
			
			str_cmd = ('-A OUTPUT -p tcp -m string --string "%s" '
						'--algo kmp -j REJECT' % (address))
		else:
			
			diz.close()
			sys.exit("\n\033[31;1m Questa regola di 'blocco pagina "
								"web' risulta già impostata.\033[0m\n")
		
		blocksites_review_graphic()
		
		for key,val in diz.items():
			print("\033[36m  [%s]      --     %s\033[0m" 
												% (str(key), str(val)) )
			
		print("\n\033[1m Regola di 'blocco pagina web' impostata nel "
						"firewall.\033[0m\n")
		diz.close()
		
		return str_cmd
		
		
	################################# DELETTING BLOCK SITE RULES
	def IP_delete(self, address):
		"""
		Delete rules for blocked webpages
		"""
		
		diz = shelve.open('%s/sites_block.db'% self.pathDB,'c') 
		
		if diz.has_key(address):
			
			del diz[address]
			
			str_cmd = ('-D OUTPUT -p tcp -m string --string "%s" '
						'--algo kmp -j REJECT' % (address))
		else:
			
			diz.close()
			sys.exit("\n\033[31;1m Regola inesistente\033[0m")
			
			
		blocksites_review_graphic()
		
		for key,val in diz.items():
			print("\033[36m  [%s]      --     %s\033[0m" 
											% (str(key), str(val)) )
			
		print ("\n\033[1m Regola di 'blocco pagina web' "
									"cancellata nel firewall.\033[0m\n")
		diz.close()
		
		return str_cmd
		
		
	#####################################  SHOW SITES BLOCKED LIST
	def IP_review(self):
		"""
		Shows list with all blocked web sites
		"""
		
		call(['clear'])
		
		diz = shelve.open('%s/sites_block.db'% self.pathDB,'c') 
	
		blocksites_review_graphic()
		
		for key,val in diz.items():
			print("\033[36m  [%s]      --     %s\033[0m" % (str(key), str(val)) )
		print '\n'
		
		diz.close()
		
		
	##################################### TCP/UDP PROTOCOLS APPEND:
	def doors_connect(self, doortarget, description, prtcl, PRTCL, target):
		"""
		Establish the rules for tcp and udp protocols. Here return values are:
		- doortarget > is door number 
		- description > is the service or a little decription
		- prtcl > is a protocol (udp or tcp)
		- PRTCL > is a protocol ID  
		- target > is the rule (ACCEPT, REJECT or DROP)
		"""

		diz = shelve.open('%s/doors_rules_%s.db' % (self.pathDB, PRTCL),'c')
		
		if diz.has_key(doortarget) is True:
			
			nametarg = diz[doortarget]
			
			print ("\n\n\033[31;1m WARNING:\n\033[0m La porta %s %s era già "
					"stata precedentemente sottoscritta alla regola %s \n"
					% (PRTCL, doortarget, nametarg[1]))
			
			print ("\033[34;1m DETTAGLI:\n\033[0m %s protocol\n"
							" Porta: %s\n Servizio: %s\n Target: %s.\n"
							"\n\033[34;1m COMPORTAMENTO:\n\033[0m"
							" La regola non ha subito variazioni\n"
							% (PRTCL, doortarget, nametarg[0], nametarg[1]))
			diz.close()
			
		else:
			
			diz[doortarget] = description,"%s" % target
			
			str_cmd = ('-A %s -p %s -m multiport --dport %s -j %s' 
							% (PRTCL, prtcl, doortarget, target))
			
			add =  ("\n\033[1m |%s protocol|: Porta '%s' del Servizio "
					"'%s' è appesa alla regola '%s' nel firewall.\033[0m\n" 
						%(PRTCL, doortarget, description, target))
			
			tcp_udp_graphic_review(PRTCL)
			
			for key,val in diz.items():
				print("\033[36m  [%s]        --       %s\033[0m" 
						% (str(key), str(val)) )
			print add
			diz.close()
			
			return str_cmd
			
			
			
	##################################### DELETING MULTIPLE PROTOCOLS:
	def doors_delete(self, doortarget, prtcl, PRTCL):
		"""
		deleting previous tcp and udp protocols rules
		"""
		diz1 = shelve.open('%s/doors_rules_%s.db'% (self.pathDB, PRTCL),'c')
						
		if diz1.has_key(doortarget) is True:
			
			nametarg = diz1[doortarget]

			str_cmd = ('-D %s -p %s -m multiport --dport %s -j %s' 
					% (PRTCL, prtcl, doortarget, nametarg[1]))
						
			del diz1[doortarget]
			
			tcp_udp_graphic_review(PRTCL)
			
			for key,val in diz1.items():
				print("\033[36m  [%s]        --       %s\033[0m" 
								% (str(key), str(val)) )
				
			print ("\n\033[1m %s protocol:\n Porta '%s' \n Servizio "
					"'%s'\n Target '%s'\n Regola cancellata nel firewall."
					"\033[0m\n" % (PRTCL, doortarget, nametarg[0], nametarg[1]))
			
			diz1.close()
			
			return str_cmd
			
		else:
			print ("\n\033[31;1m WARNING:\033[0m %s protocol: regola "
						"inesistente nel firewall\n" % PRTCL)
			diz1.close()
			
		
	######################################### OVERVIEW PROTOCOLS RULES
	def doors_review(self, PRTCL):
		"""
		Shows list with all tcp/udp rules
		"""
		#call('clear', shell = True) # this is useless, produce too space
		
		diz = shelve.open('%s/doors_rules_%s.db'% (self.pathDB, PRTCL),'c') 
		
		print '\033[1m\n   LISTA REGOLE PORTE TCP/UDP \033[0m\033[34;1m'
		
		tcp_udp_graphic_review(PRTCL)
		for key,val in diz.items():
			print("\033[36m  [%s]        --       %s\033[0m" 
							% (str(key), str(val)) )
		print '\n'
		diz.close()
		
		
		
class Main_Menu(Rules_Applied):
	"""
	Class child that inherit base class Rules_Applied.
	Show a menu with options and then call the method and/or istance
	"""
	
	def __init__(self, pathDB):
		
		self.pathDB = pathDB # pathDB is a path name of database
		
		self.outPut = None # final output state
		
		self.outPut2 = None
		
		call(['clear'])
		
		menu_doc()
		
		choice = raw_input("Attendo un input che corrisponde all'opzione:  > ")
		
		if choice == '1':
			self.IP_insert()
			
		elif choice == '2':
			self.IP_delete()
			
		elif choice == '3':
			self.IP_review() # in the mother class
		
		elif choice == '4':
			self.doors_connect()
			
		elif choice == '5':
			self.doors_delete()
			
		elif choice == '6':
			self.doors_review('TCP') # in the mother class
			self.doors_review('UDP') # in the mother class
			
		elif choice == 'q' or choice == "Q":
			print "cliffwall, Exit"
			sys.exit()
			
		else:
			sys.exit("Errore di immissione, Exit.")
	
	
	def IP_insert(self):
		"""
		Set the variables name and it pass for insert block ip rules
		"""
		call(['clear'])
		
		ip_insert_doc()
		
		address_name_target = raw_input("\n\n\033[1m Parola chiave o address-name,"
							" ['q' per uscire]\033[0m >  ")
		
		if address_name_target == 'q' or address_name_target == 'Q':
			
			sys.exit()
		
		description = raw_input("\n\n\033[1m descrizione del sito.\n\033[0m >  ")
		
		
		self.outPut = Rules_Applied.IP_insert(self, address_name_target, 
										description)
	
	
	def IP_delete(self):
		"""
		Set the variables name and it pass for delete block ip rules
		"""
		
		call(['clear'])
		
		ip_delete_doc()

		address_name_target = raw_input("\n\n\033[1m Parola chiave o "
							"address-name, ['q' per uscire]\033[0m >  ")
		
		if address_name_target == 'q' or address_name_target == 'Q':
			
			sys.exit()
			
		self.outPut = Rules_Applied.IP_delete(self, address_name_target)
		
		
		
	def doors_connect(self):
		"""
		Set the variables name and it pass for new rules at tcp/utp doors
		"""
		call(['clear'])
		
		door_connect_doc()
		
		doortarget = raw_input("\n\n\033[1m Port number to be signed in the "
						 "firewall rules ['q/Q' per uscire]\n\033[0m >  ")
		
		if doortarget == 'q' or doortarget == 'Q':
			
			sys.exit()
	
		if str.isdigit(doortarget) is False:
			sys.exit("\n\n\033[31;1mBad option, is not integer\033[0m")
				
		description = raw_input("\n\n\033[1m Description:\n\033[0m >  ")
		
		protocol = raw_input("\n\n\033[1m Protocols: "
						"\033[32;1m|1|\033[0m(tcp)  \033[32;1m|2|\033[0m(udp)  "
											"\033[32;1m|3|\033[0m(tcp/udp) >  ")
		
		target = raw_input("\n\n\033[1m Target "
					":\033[32;1m|1|\033[0m(drop) \033[32;1m|2|\033[0m(reject) "
								"\033[32;1m|3|\033[0m(accept):\033[0m > N°  ")
		if target == "1":
			target = "DROP"

		elif target == "2":
			target = "REJECT" 

		elif target == "3":
			target = "ACCEPT"
		else:
			sys.exit("\n\n\033[31;1mBad option, invalid target\033[0m")
		
		if protocol == "1":
			self.outPut = Rules_Applied.doors_connect(self, doortarget, 
											 description, 'tcp', 'TCP', target)
			
		elif protocol == "2":
			self.outPut = Rules_Applied.doors_connect(self, doortarget, 
											 description, 'udp', 'UDP', target)
			
		elif protocol == "3":
			self.outPut = Rules_Applied.doors_connect(self, doortarget, 
											 description, 'tcp', 'TCP', target)
			
			self.outPut2 = Rules_Applied.doors_connect(self, doortarget, 
											 description, 'udp', 'UDP', target)
			
		else:
			sys.exit("\n\n\033[31;1mBad option, invalid protocol\033[0m")
			
			
			
	def doors_delete(self):
		"""
		Set the variables name and it pass for deleting rules at 
		tcp/utp doors
		"""
		call(['clear'])
		
		door_delete_doc()
		
		doortarget = raw_input("\n\n\033[1m Numero porta da cancellare dalle "
						"regole del firewall ['q/Q' per uscire]\n\033[0m >  ")
		
		if doortarget == 'q' or doortarget == 'Q':
			
			sys.exit()
	
		protocol = raw_input("\n\n\033[1m Tipo di Protocollo connessione: "
						"\033[32;1m|1|\033[0m(tcp)  \033[32;1m|2|\033[0m(udp)  "
											"\033[32;1m|3|\033[0m(tcp/udp) >  ")
		
		if protocol == "1":
			self.outPut = Rules_Applied.doors_delete(self, doortarget, 'tcp', 
											'TCP')
			
		elif protocol == "2":
			self.outPut = Rules_Applied.doors_delete(self, doortarget, 'udp', 
											'UDP')
			
		elif protocol == "3":
			self.outPut = Rules_Applied.doors_delete(self, doortarget, 'tcp', 
											'TCP')
			self.outPut2 = Rules_Applied.doors_delete(self, doortarget, 'udp', 
											 'UDP')
			
		else:
			sys.exit("\n\n\033[31;1mBad option, invalid protocol\033[0m")
