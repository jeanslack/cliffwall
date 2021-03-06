--------------------------------------------
Simple Iptables UI for Gnu/Linux (firewall)
--------------------------------------------

Copyright © 2013 - 2017 by Gianluca Pernigotto aka jeanslack   
Author and Developer: Gianluca Pernigotto   
Mail: <jeanlucperni@gmail.com>   
License: GPL3 (see LICENSE file in the doc folder)

--------------------------------------------

Description:
------- 

cliffwall is a command line user-interface based on iptables for a firewall 
configurations. Can work with any type of network interface with a typical 
home networking 

Inspired by:
[Simple Stateful Firewall](https://wiki.archlinux.org/index.php/Simple_stateful_firewall)

Dependencies:
-------

python >=2.6, iptables


Features:
-------

* Simple stateful firewall rules

* Management for udp/tcp protocol doors rules

* Blocking functions (web sites, network) for a moderate parental control

* ..and other

Building packages:
----
See the INSTALL file in the sources folder for more complete details

* DEBIAN:

Install extra dependencies for build package with distutils:

		# apt-get install python-all python-stdeb fakeroot

Enter in unzipped sources folder and type (with not root):

		python setup.py --command-packages=stdeb.command bdist_deb   

This should create a python-cliffwall.deb in the new deb_dist directory.   
See the INSTALL file for more details and info on how-to build .deb package   
[https://github.com/jeanslack/cliffwall/blob/master/INSTALL](https://github.com/jeanslack/cliffwall/blob/master/INSTALL)

* SLACKWARE:

Require pysetuptools (is not installed for 14.1 and previous version of Slackware:)   
[slackbuild.org](http://slackbuilds.org/repository/14.1/python/pysetuptools/)

Then, download my SlackBuild for compile the binary package:   
[jeanslack slackbuilds](https://github.com/jeanslack/slackbuilds/tree/master/cliffwall)   

See the INSTALL file in the sources folder for more complete details:    [https://github.com/jeanslack/cliffwall/blob/master/INSTALL](https://github.com/jeanslack/cliffwall/blob/master/INSTALL)


--------------------------------------------------------------------------------
