from distutils.core import setup

setup(
	name='CertedUploader',
	version='0.1.7',
	author='wale soyinka',
	author_email='wsoyinka@gmail.com',
	url='',
	description='File Uploader using Client Side Certificate',
	scripts=['bin/uploader.py'],
	packages=['certeduploader'],
	install_requires=[
		"requests >= 2.13.0"
	  ]
	)
