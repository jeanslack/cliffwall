#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# First release: October 07 2014
#
#
#########################################################
# Name: setup.py
# Porpose: script for building cliffwall package
# Platform: Linux Slackware
# Writer: Gianluca Pernigoto <jeanlucperni@gmail.com>
# Copyright: (c) 2014-15 Gianluca Pernigoto <jeanlucperni@gmail.com>
# license: GPL3
# Rev 16/02/2015
#########################################################

from distutils.core import setup
from setuptools import setup
import platform
from glob import glob
import sys
import os

NAME = 'cliffwall'
VERSION = '0.13'
LICENSE = 'Gnu GPL3 (See LICENSE)'
DESCRIPTION = 'Firewall iptables based'

LONG_DESCRIPTION = """ cliffwall is a user-interface based on iptables that facilitates 
the configuration of your firewall. Can work with any type of network 
interface and is designed to handle single hosts.
Immediately provides the necessary rules to make stateful firewall and 
quick customizations such as management of TCP/UDP ports and web-sites 
filtering.
"""
URL = 'https://github.com/jeanslack/cliffwall'


def glob_files(pattern):
	"""
	this is a simple function for globbing that iterate 
	for list files in dir
	"""
	
	return [f for f in glob(pattern) if os.path.isfile(f)]



def  LINUX_SLACKWARE(id_distro, id_version):
	"""
		------------------------------------------------
		setup build cliffwall slackware package
		------------------------------------------------
		
		TOOLS: 
			- setuptools

		USAGE: 
		- In combination with SlackBuild script use:
		python setup.py install --root=$PKG
	"""
	
	
	DATA_FILES = [
		('/lib/cliffwall', ['config/daemons/cliffwall-init'],),
		('/lib/cliffwall', ['config/daemons/cliffwall-init-functions'],),
				]
		# this is DATA_FILE structure: 
		# ('dir/file destination of the data', ['dir/file on current place sources']
		# even path must be relative-path
		# use absolute path where you want copying in different location instead
		# usr:
	
	setup(name = NAME,
		version = VERSION,
		description = DESCRIPTION,
		long_description = LONG_DESCRIPTION,
		author = 'Gianluca Pernigotto',
		author_email = 'jeanlucperni@gmail.com',
		url = URL,
		license = LICENSE,
		platforms = ['Gnu/Linux (%s %s)' % (id_distro, id_version)],
		packages = ['cliffwall_pack'],
		data_files = DATA_FILES,
		scripts = [NAME],
		)
		
	
def LINUX_DEBIAN(id_distro, id_version):
	"""
		------------------------------------------------
		setup build cliffwall debian package
		------------------------------------------------
		
		TOOLS: 
		apt-get install python-all python-stdeb fakeroot

		USAGE: 
		- for generate both source and binary packages :
			python setup.py --command-packages=stdeb.command bdist_deb
			
		- Or you can generate source packages only :
			python setup.py --command-packages=stdeb.command sdist_dsc
			
		RESOURCES:
		- look at there for major info:
			https://pypi.python.org/pypi/stdeb
			http://shallowsky.com/blog/programming/python-debian-packages-w-stdeb.html
	"""
	
	# this is DATA_FILE structure: 
	# ('dir/file destination of the data', ['dir/file on current place sources']
	# even path must be relative-path
	DATA_FILES = [
		('share/man/man8', ['man/cliffwall.8.gz'],), 
		('share/doc/python-cliffwall', glob_files('docs/*'),),
		('share/doc/python-cliffwall', ['AUTHORS', 'BUGS', 'CHANGELOG', 
		'COPYING', 'README.md', 'TODO']),
		('/etc/init.d', ['config/daemons/cliffwall-init'],),
		('/lib/cliffwall', ['config/daemons/cliffwall-init-functions'],),
		('/etc/cliffwall', glob_files('config/rules/*'),),
		('/etc/sysctl.d', ['config/cliffwall10net.conf'],),
				]
	
	DEPENDENCIES = ['python >=2.6']
	
	setup(name = NAME,
		version = VERSION,
		description = DESCRIPTION,
		long_description = LONG_DESCRIPTION,
		author = 'Gianluca Pernigotto',
		author_email = 'jeanlucperni@gmail.com',
		url = URL,
		license = LICENSE,
		platforms = ['Gnu/Linux (%s %s)' % (id_distro, id_version)],
		scripts = [NAME],
		packages = ['cliffwall_pack'],
		data_files = DATA_FILES,
		install_requires = DEPENDENCIES,
		)

	
##################################################

if sys.platform.startswith('linux2'):
	
	dist_name = platform.linux_distribution()[0]
	dist_version = platform.linux_distribution()[1]
	
	if dist_name == 'Slackware ':
		LINUX_SLACKWARE(dist_name, dist_version)
		
	elif dist_name == 'debian': # debian use the sistemd services
		LINUX_DEBIAN(dist_name, dist_version)
		
	else:
		print 'this platform is not yet implemented: %s %s' % (dist_name, dist_version)
		

else:
	print 'OS not supported'
