#!/usr/bin/env python3
# Author: telekrex
import sys
from platform import system

if system() == 'Windows':
    HOSTS = 'C:\\Windows\\System32\\drivers\\etc\\hosts'
else:
    HOSTS = '/etc/hosts'

try:
    # if the provided arg is to "enable" the muting, (forced lowercase)
    # then set target variable to the content of the 'generated' file
    if str(sys.argv[1]).lower() in ['enable', 'start', 'on']:
        TARGET = 'generated.txt'
        import generate
        generate.build()

    else:
        # if anything other than "enable" was asked for in arg,
        # then we assume "disable" and set target to content
        # of 'default' file
        TARGET = 'default.txt'

    # with target set, we open the system hosts file
    # and replace it with the content of target
    with open(TARGET, 'r') as file:
        contents = file.read()
    with open(HOSTS, 'w') as file:
        file.write(contents)
    # program will exit when finished

except Exception as e:
    # if something went wrong, show me
    print(e)
