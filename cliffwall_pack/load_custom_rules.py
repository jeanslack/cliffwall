#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#
#########################################################
# Name: load_custom_rules.py (module)
# Porpose: custom rules runner
# Writer: Gianluca Pernigoto <jeanlucperni@gmail.com>
# Copyright: (c) 2013-2015 Gianluca Pernigoto <jeanlucperni@gmail.com>
# license: GPL3
# Version: (V0.13) 10/02/2015
# Rev: (V0.13) 14/02/2015 add status error
#########################################################

"""
Execute services or rules that was are set with 'cliffwall settings'
command. if one of the databases is empty do not run commands, of course 
"""

import subprocess
import shelve

def load_custom(pathDB):
    """
    This function is called by command 'cliffwall start or restart 
    or reload' and during startup the OS .
    Also, here are applied all personal settings established with 
    command 'cliffwall settings'
    """	
    ################ applies block sites rules
    
    diz = shelve.open('%s/sites_block.db'% pathDB,'c') 
    
    if len(diz) <= 0:
        # nessuna regola di blocco siti web impostata 
        # (No rule to block incoming set)
        diz.close()
        
    else:
        # "Attivo blocco IP [in] personale"
        for key in diz.keys():
            
            try:
                subprocess.check_call('iptables -A OUTPUT -p tcp -m string '
                    '--string "%s" --algo kmp -j REJECT' % (key), shell = True)
                
            except subprocess.CalledProcessError:
                
                sys.exit("\033[31;1m[ERROR]\033[0m subprocess.CalledProcessError: "
                            "firewall daemon > 'load_custom:sites_block.db'")
            #print "check_call(iptables -I INPUT -s %s -j DROP " % key
            
        diz.close()
        
    ################ applies tcp rules
    
    diz = shelve.open('%s/doors_rules_TCP.db'% pathDB,'c') 
    
    if len(diz) <= 0:
        # Nessuna regola TCP impostata"
        diz.close()
        
    else:
        # Attivo apertura connessione TCP personale
        val = diz.values()
        tupla = val[0]
        
        for key in diz.keys():
            
            try:
                subprocess.check_call('iptables -A TCP -p tcp --dport %s -j %s' 
                            %(key, tupla[1]), shell = True)
            
            except subprocess.CalledProcessError:
                
                sys.exit("\033[31;1m[ERROR]\033[0m subprocess.CalledProcessError: "
                            "firewall daemon > 'load_custom:doors_rules_TCP.db'")
            #print "check_call(--dport %s -j %s" %(key, tupla[1])
            
        diz.close()
        
    ################ applies udp rules
    
    diz = shelve.open('%s/doors_rules_UDP.db'% pathDB,'c') 
    
    if len(diz) <= 0:
        # Nessuna regola UDP impostata"
        diz.close()
        
    else:
        # Attivo apertura connesione UDP personale
        val = diz.values()
        tupla = val[0]
        
        for key in diz.keys():
            
            try:
                
                subprocess.check_call('iptables -A UDP -p udp --dport '
                        '%s -j %s' % (key, tupla[1]), shell = True)
            
            except subprocess.CalledProcessError:
                
                sys.exit("\033[31;1m[ERROR]\033[0m subprocess.CalledProcessError: "
                            "firewall daemon > 'load_custom:doors_rules_UDP.db'")
            #print "check_call(--dport %s -j %s" %(key, tupla[1])
            
        diz.close()
