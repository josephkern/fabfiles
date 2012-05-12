fabfiles
========

Fabric Automation and Orchestration for Sysadmin

The files herein are task files for [fabric][fab] a "simple, pythonic
remote execution and deployment" framework.

Getting Started
---------------

These files are currently untested, so take this example with a grain
of salt. I will be setting up a lab shortly to test the cisco commands
to make sure they behave themselves. When I am comfortable running
these in a production environment, I will change `__status__` to
`Production`. Before that, use at your own risk.

__First install fabric__

	pip install fabric
	
__next clone this repo__

	git clone git@github.com:josephkern/fabfiles.git
	cd fabfiles

__List the available commands__

	fab -f cisco.py --list
	fab -H switch1,switch2,switch3 copy_run_start

[fab]: https://github.com/fabric/fabric
