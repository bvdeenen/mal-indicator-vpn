# mal-indicator-vpn

# Notes
My first bigger/real github repository, learning git from CLI along the way.

This is a small program displaying an OK or notOK icon among system ones.  The following lines are my notes.  Use at your own risk.  Better approach would be to use service (start, status, stop...).

# Prerequisities
Install from repository (using Xubuntu 18.04):
    python3
    python3-gi
    emelfm2-svg-icons
    gir1.2-appindicator3-0.1
    protonvpn

Needed account @ <https://protonvpn.com/>
    sudo protonvpn configure
Username and Password taken from <https://account.protonvpn.com/account>

# Testing
Direct connection: 
    sudo protonvpn c NL-FREE#2 -p tcp
Testing these snippets: 
    sudo bash ./vpn.sh
    sudo python3 ./indicator-vpn.py
Manual disconnect from vpn: 
    sudo protonvpn d

# Basic use
I set up crontab:
    sudo su
    crontab -e
    @reboot sleep 30 && /bin/bash <path>/vpn.sh

