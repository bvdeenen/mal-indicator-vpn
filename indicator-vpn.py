#!/usr/bin/env python3


# python libraries to be loaded
import gi
import os
import signal
import subprocess

# necessary steps for gi
gi.require_version('Gtk','3.0') 
from gi.repository import Gtk as gtk
gi.require_version('AppIndicator3', '0.1') 
from gi.repository import AppIndicator3 as appindicator
from gi.repository import GLib

# Setting up OK and notOK images
imagefolder="figures" # To Be Changed
OK=os.path.join(imagefolder, "OK.png")          # To Be Changed
NOTOK=os.path.join(imagefolder, "notOK.png")     # To Be Changed

class TheCore:
  APPINDICATOR_ID = 'malipivo-openvpn'

  def __init__(self):
      self.indicator = appindicator.Indicator.new(TheCore.APPINDICATOR_ID, os.path.abspath(NOTOK), appindicator.IndicatorCategory.SYSTEM_SERVICES)
      self.indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
      self.indicator.set_menu(self.build_menu())

  def main(self):
      self.updateme()
      GLib.timeout_add_seconds(60,self.updateme) # testing vpn every 60 seconds
      gtk.main()

  def hlavni(self):
    self.moje = "Connected" in subprocess.getoutput("protonvpn status").split()

    if self.moje:
      self.indicator.set_icon_full( os.path.abspath(OK), "connected" )    # vpn is working well
    else:
      self.indicator.set_icon_full( os.path.abspath(NOTOK), "not connected" ) # vpn is not working, we are not connected
    return self.moje

  def updateme(self):
    self.moje=self.hlavni()
    #print(moje)
    if not self.moje:
      os.system("sudo protonvpn c --cc es") # I am not connected, formally disconnect me and try to connect me again.
      self.hlavni()
    return True

  def build_menu(self): # This is a simple menu with one item: quit
      self.menu = gtk.Menu()
      self.item_quit = gtk.MenuItem(label='Quit')
      self.item_quit.connect('activate', self.quit)
      self.menu.append(self.item_quit)
      self.menu.show_all()
      return self.menu

  def quit(self,source): # disconnect vpn when quitting icon
    os.system("sudo protonvpn d")
    gtk.main_quit()

if __name__ == "__main__":
  signal.signal(signal.SIGINT, signal.SIG_DFL)
  TheCore().main()

