# SNMP_parser

Python scripts for taking and parsing data about MAC-addresses from HP switches.

Main idea: collect SNMP data based on specific MIB about mac-addresses in the ARP-tables on switches. Parse it, process and put on the web-server. From some moment (historystart) we check if the mac address presents in history. If not - alert. We have info about port, mac, producer (from oui file), date, time, and (possibly) ip of the new mac.

Before first start we need to launch historystart.py

snmpcron - bash script to run commands in Ubuntu.

parser and parsearp scripts performs data processing.

trigger and arptoalert also.
