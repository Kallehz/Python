# Process ls
#
# Unix based systems provide a command ls to list the contents of a directory.
# By default it displays the contents in multiple columns
# (the number of columns is determined by the width of the console window).
# The space between entries in adjacent columns is at least two spaces.
# An example of the output is as follows.
#
# acpid.pid     console-kit-daemon.pid  lock        pm-utils      sdp                      upstart-socket-bridge.pid
# acpid.socket  crond.pid               mdm.pid     postgresql    sendsigs.omit.d          upstart-udev-bridge.pid
# apache2       crond.reboot            mdm_socket  pppconfig     shm                      user
# apache2.pid   cups                    motd        resolvconf    udev                     utmp
# avahi-daemon  dbus                    mount       rsyslogd.pid  udisks                   wicd
# console       dhclient.pid            network     samba         udisks2                  wpa_supplicant
# ConsoleKit    initramfs               plymouth    screen        upstart-file-bridge.pid
# Write a function process_ls that takes a string, containing the output from a call to ls.
# The function returns a list containing the contents of the directory.
# The order of the contents should be the same as specified in the string,
# i.e. the contents in the first column from top to bottom, then the second column, etc.
#
# Note that the contents of the directory will not contain two adjacent spaces, and will not start or end with a space.
#
# Example
from pprint import pprint
import itertools as it
import re


def process_ls(string):
    lis =[]
    for ls in string.splitlines():
        lis.append(re.split('  +', ls))

    l = list(it.zip_longest(*lis))

    flattened = [val for sublist in l for val in sublist]
    a = [x for x in flattened if x is not None]

    a = list(filter(None, a))
    a = [x.strip('# ') for x in a]

    return a
    # fsasadsadsadasdasdsadsadasdassd
    #return sorted(a, key=lambda x: x.lower(), reverse=False)

