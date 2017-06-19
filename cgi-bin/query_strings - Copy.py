#!python
import cgi
import cgitb
cgitb.enable()

import os, pprint

# The HTTP Headers
print("Content-type: text/html;charset=utf-8;")
print()  # This blank print indicates the end of the Headers
# The Content
print("<h1>Hello, World!</h1>")
print("<pre>")
print("{0}".format(pprint.pprint(dict(os.environ))))
print("</pre>")
