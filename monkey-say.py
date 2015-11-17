import sys
import json
import urllib2


########## config
_url = "http://httpbin.org/post"

def main(args):
    # join arguments into a sentence
    message = ' '.join(args)

    req = urllib2.Request(_url)
    req.add_header('Content-Type', 'application/json')

    res = urllib2.urlopen(req, json.dumps({'message': message}))

    print(res.read())

    pass

if __name__ == "__main__":
    main(sys.argv[1:])
