#!/usr/bin/env python
# -*- coding: UTF-8 -*-

def menu_doc():
	
	print """\033[1m 
  In questo spazio è possibile gestire alcune regole personali
  nel firewall e tenerne traccia.\033[0m

  inserire numero o lettera opzionali:


  ------------------------------------------------------
        \033[1mBLOCCO DEI SITI WEB NON GRADITI:\033[0m

  \033[32;1m|1|\033[0m   Blocca siti non graditi
  \033[32;1m|2|\033[0m   Cancella regole siti non graditi
  \033[32;1m|3|\033[0m   Visualizza la lista dei siti bloccati.  
  -----------------------------------------------------
        \033[1mIMPOSTAZIONI REGOLE TCP/UDP\033[0m

  \033[32;1m|4|\033[0m   Aperture/chiusura delle porte sui protocolli tcp/udp
  \033[32;1m|5|\033[0m   Cancella regole precedentemente impostate tcp/udp
  \033[32;1m|6|\033[0m   Visualizza la lista regole tcp/udp
  -----------------------------------------------------

  \033[31;1m|Q|\033[0m   Esci\n"""
  
def ip_insert_doc():
	
	print '''
  Il blocco dei siti non graditi avviene immettendo una parola chiave
  che identifica il sito, per esempio: google . 
  Per volere limitare il blocco solo a www.google.com ma non a 
  www.google.it, si potrebbe restringere il campo immettendo un indirizzo
  nella sua interezza, per esempio: www.google.com
  
  Svuotare i dati dal proprio browser rende effettiva la nuova regola. 
  '''

def ip_delete_doc():
	
	print '''
  La procedura per rimuovere le regole precedentemente sottoscritte av-
  viene similmente a quella della loro sottoscrizione, cioè immettendo
  la parola o address-name esattamente corrispondente.
  Per vedere quali regole sono già state sottoscritte, tornare al menu
  e usare l'opzione che visualizza la loro lista. 
  '''
  
def door_connect_doc():
	
	print '''\n
  Le porte TCP/UDP sono tutte controllate dalle nuove chain (-N TCP, -N UDP)
  impostate in modo predefinito nel firewall. Tuttavia è possibile operare 
  per poter aprire/chiudere determinate porte o eliminare delle regole.
  Ogni regola è costituita da tre target (drop, accept, reject) che deter-
  minano l'azione sulla porta: drop rifiuta e scarta il pacchetto, accept
  lo consente e reject lo respinge al mittente.
  Qui le porte devono essere indicate con un numero (o una lista di numeri 
  delimitati da una virgola fino ad un massimo di 15) o un range (8990:9000), 
  dei protocolli e un target.
  
  esempi:
  
  NUMERO: 6890 
  LISTA DI NUMERI: 22,25,53,80,433,465,5222,5269,5280,8999:9003
  PROTOCOLLO: TCP, UDP o TCP/UDP
  TARGET: drop (chiude la porta)
          accept (apre la porta)
          reject ( chiude la porta e respinge al mittente)
          
  NOTA: per includere un range o intervallo di porte usa per esempio 6890:6895
  '''
  
def door_delete_doc():
	
	print '''\n
  La procedura per rimuovere le regole precedentemente sottoscritte av-
  viene similmente a quella della loro sottoscrizione, cioè immettendo
  il numero della porta TCP o UDP che sottointende la regola da eliminare.
  Per vedere quali regole sono già state sottoscritte, tornare al menu
  e usare l'opzione che visualizza la loro lista.
  '''
  
def tcp_udp_graphic_review(arg):
	"""
	Simples graphic for tcp and udp port protocol list
	"""
	
	graphic_rules_TCP = '''\033[34;1m
  ------------------------------------------------     
  TCP PORT:                NAME:     TARGETS:
  ------------------------------------------------\033[0m'''
  
	graphic_rules_UDP = '''\033[34;1m
  ------------------------------------------------     
  UDP PORT:                NAME:     TARGETS:
  ------------------------------------------------\033[0m'''
	
	if arg == 'TCP':
		print graphic_rules_TCP
			
	if arg == 'UDP':
		print graphic_rules_UDP
		
		
		
def blocksites_review_graphic():
	"""
	View a simple graphic for websites list
	"""
	
	print '''\n\033[1m  Blocked Websites List \033[0m \033[34;1m
  ------------------------------------------------     
  KEY WORD:                         DESCRIPTION:
  ------------------------------------------------\033[0m'''
