#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#
#########################################################
# Name: conf_parser.py (module)
# Porpose: make parsing at iface.conf
# Writer: Gianluca Pernigoto <jeanlucperni@gmail.com>
# Copyright: (c) 2013-2015 Gianluca Pernigoto <jeanlucperni@gmail.com>
# license: GPL3
# Version: (V0.13) 13/02/2015
# Rev 
#########################################################


import sys


def parser(pathrule):
	"""
	execute a parsing on iface.conf for established which interfaces
	are uncomment on the file and ready to be pass at iptables command.
	"""
	
	iface_conf = '%s/iface.conf' % pathrule
	
	uncomment = []

	fconf = open(iface_conf, 'r')
	list_lines = fconf.readlines()
	fconf.close()

	for line in list_lines:
		if not line.startswith('#'):
			uncomment.append(line.strip()) # strip rimuove tutti \n + spazi e tab
			
	#   rimuovere le stringhe vuote da una lista:
	#cleaned = filter(None, uncomment)
	#   Note however, that filter returns a list in Python 2, but a 
	#   generator in Python 3. You will need to convert it into a list
	#   in Python 3 :
	#cleaned = list(filter(None, uncomment)) 
	#   or use the list comprehension solution:
	cleaned = [x for x in uncomment if x]

	if cleaned == []:
		
		sys.exit('[ERROR]: %s (nessuna interfaccia di rete disponibile)' % 
													iface_conf)
		
	if len(cleaned) > 1: 
		
		sys.exit('[ERROR]: %s (troppe righe decommentate?)' % iface_conf)
		
	if cleaned[0].startswith('interface_all'):
		
		return 'start', ""
		
	elif cleaned[0].startswith('interface_list='):
		
		slicing = cleaned[0] # the row
		interfaces = slicing[15:] # interfaces only of the row
		
		if slicing[15:] == '':
			
			sys.exit('[ERROR]: %s (la lista su "interface_list=" risulta '
											'essere vuota)' % iface_conf)
		return 'start_types', interfaces
			
		
	elif cleaned[0].startswith('interface_match=eth+'):
		
		return 'start', cleaned[0]
		
	else:
		sys.exit('[ERROR]: %s (Colonne malformate)' % iface_conf) 
