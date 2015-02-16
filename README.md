================================================================================ 
Simple Iptables UI for Gnu/Linux (firewall)
================================================================================ 


--------------------------------------------------------------------------------

Copyright © 2010 - 2015 jeanslack 
 
  Author and Developer: jeanslack 
  Mail: <jeanlucperni@gmail.com>
  License: GPL3 (see LICENSE file in the docs folder)

--------------------------------------------------------------------------------

Description:
------- 

cliffwall is a user-interface based on iptables that facilitates the 
configuration of your firewall. Can work with any type of network interface 
and is designed to handle a single PC in a normal home network (single host).

Immediately provides the necessary rules to make stateful firewall and 
quick customizations such as management of TCP/UDP ports and web-sites 
filtering.

Inspired by:
[Simple Stateful Firewall](https://wiki.archlinux.org/index.php/Simple_stateful_firewall)




Dependencies:
-------

python >=2.6, iptables


Features:
-------

* Simple stateful firewall rules

* Easy management for udp/tcp protocol doors rules

* block web sites (for a moderate parental control)

* ..and other

Use
-------
After installation, open a terminal window and type:

		man cliffwall

Or open a terminal window with administrator privileges and type:

		cliffwall -h

Installation
-------

--------------------------------------------------------------------------------

DEBIAN:

--------------------------------------------------------------------------------

Extra dependencies for build package with distutils:

		# apt-get install python-all python-stdeb fakeroot

Enter in unzipped sources folder and type (with not root):

		python setup.py --command-packages=stdeb.command bdist_deb

This should create a python-pyrename_version_all.deb in the new deb_dist directory.

see the setup.py script-file for more info on how-to build .deb package

--------------------------------------------------------------------------------

SLACKWARE:

--------------------------------------------------------------------------------

Require pysetuptools at: [slackbuild.org](http://slackbuilds.org/repository/14.1/python/pysetuptools/)

Then download the SlackBuild: [My-Repo-Slackware](https://github.com/jeanslack/My-Repo-Slackware/tree/master/slackware/security/cliffwall)


--------------------------------------------------------------------------------
