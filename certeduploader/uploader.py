#!/usr/bin/env python

from sys import  argv
import requests
import argparse

parser = argparse.ArgumentParser(description="Upload File and Pass Client Cert")

parser.add_argument('-u', '--url', metavar='[URL]', required=True,
                      dest='url', action='append',
                       help='destination server URL' )

parser.add_argument('-p', '--payload', metavar='[File-Containing-Payload]',
			 required=True,
			dest='payload', action='append',
			help='FileName of Payload' )

parser.add_argument('-c','--client-cert' , metavar='[Path-to-Client-Certificate]', 
			required=True, dest='client_cert', action='append',
			help='Client Certificate File - PEM format' )

args = parser.parse_args()

def test_stuff():
	print(args.payload[0])
	print(args.client_cert)
	print(args.url)

def upload_file():
	files = { 'args.payload[0]': open(args.payload[0], 'rb') } 
	r = requests.post( args.url[0], files=files, cert=(args.client_cert[0]))

	print(r.status_code,)
	#resp = r.json()
	resp = r.content
#	print(resp)
#	print(args)

if __name__ == '__main__':
	upload_file()
