#Executing OS commands from python scripts.

import subprocess
from bs4 import BeautifulSoup

process = subprocess.Popen('ls -l; curl -IL httpbin.org', stdin=None, stdout=subprocess.PIPE, stderr=subprocess.PIPE, sh$
for i in range(4):
    output = process.communicate()[i].strip()
    soup = BeautifulSoup(output, 'html.parser')
    print (soup.prettify())
