#A python program to retrieve the different parts of the URL and display them.

import urllib.parse
#take any url
url = 'https://codehunter.cc/a/git/'

tpl = urllib.parse.urlparse(url)
#display the contents of the tuple
print(tpl)

#display different parts of the url
print('Scheme=', tpl.scheme)
print('Net location=', tpl.netloc)
print('Path=', tpl.path)
print('Parameters=', tpl.params)
print('Port number=', tpl.port)
print('Total url=', tpl.geturl())