#!/usr/bin/env python 
"""cisco fabric automation file

   invoke with:

       $fab -f cisco.py --list
"""
from fabric.api import *

#I am going to be very honest here, if you can't figure out what these
# commands do on your switch or router, DO NOT RUN THEM. Know what you
# are doing before you do it.

__author__ = "Joseph Kern"
__status__ = "Testing/Unstable"


# Privileges. Not sure what to do if prompted for a config t password
# from an enabled prompt ...

@task(alias="en")
def enable():
    run("enable")

@task(alias="conft")
def config_t():
    run("config t")


# Show commands. Mostly harmless.

@task(alias="shmac")
def show_mac_address_table():
    run("show mac address-table")

@task(alias="shver")
def show_version():
    run("show version")

@task(alias="shrun")
def show_running_config():
    run("show running config")

@task(alias="shstar")
def show_startup_config():
    run("show startup config")


# Commands that modify something.
 
@task(alias="corust")
def copy_run_start():
    run("copy run start")
