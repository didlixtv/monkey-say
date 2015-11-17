import sys
import json
import urllib2


########## config
_url = "http://httpbin.org/post"

def main(args):
    # join arguments into a sentence
    message = ' '.join(args)

    req = urllib2.Request(_url)
    req.add_header('content-type', 'application/json')

    res = urllib2.urlopen(req, json.dumps({'message': message}))

    # print the result of request, just cos'
    print(res.read())

if __name__ == "__main__":
    main(sys.argv[1:])
