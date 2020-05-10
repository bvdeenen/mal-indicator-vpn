# mal-indicator-vpn

# Notes
My first bigger/real github repository, learning git from CLI along the way.

This is a small program displaying an OK or a notOK icon among system ones.  The following lines are my notes when testing it.  Use at your own risk.  Better approach would be to use service (start, status, stop...).

# Prerequisities
Install from repository (using Xubuntu 18.04, sudo apt install...):

    python3
    python3-gi
    emelfm2-svg-icons
    gir1.2-appindicator3-0.1
    protonvpn

I needed account @ <https://protonvpn.com/>. Then I configured it. Username and password are available from <https://account.protonvpn.com/account>.

    sudo protonvpn configure



# Testing
Direct connection: 

    sudo protonvpn c NL-FREE#2 -p tcp

Testing these snippets: 

    sudo bash ./vpn.sh

or

    sudo python3 ./indicator-vpn.py

Manual disconnection from vpn: 

    sudo protonvpn d

# Basic usage
I set up crontab under root:

    sudo su
    crontab -e
    @reboot sleep 30 && /bin/bash <path>/vpn.sh
    exit

# Previews

OK status: 

![](figures/OK.png "An OK icon")

NOT so OK status: 

![](figures/notOK.png  "A not so OK icon")

---

