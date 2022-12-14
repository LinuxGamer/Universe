#!/usr/bin/env python
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

import os
from os.path import exists
from os.path import expanduser
from pathlib import Path

import shutil
import subprocess

home = expanduser("~")
user = os.getlogin()
# source = "/usr/share/applications/universe.desktop"
# dest = home + "/.config/autostart/universe.desktop"
# settings = home + "/.config/universe/settings.conf"

# Window 1 - Main Window
class MyWindow1(Gtk.Window):
    def __init__(self):
        super().__init__(title="Universe")
        super().__init__(icon="universe.jpg")

        self.set_border_width(10)
        self.set_default_size(640, 300)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_resizable(True)

        frame1 = Gtk.Frame(label="Universe")

        grid1 = Gtk.Grid(row_spacing    = 10,
                         column_spacing = 10,
                         column_homogeneous = True)



        label1 = Gtk.Label(label="Welcome " + user + " to your Universe!")
        label1.set_hexpand(True)

        label2 = Gtk.Label(label="Your hub to do basically everything.")
        label2.set_hexpand(True)

        label3 = Gtk.Label(label="About:")
        label3.set_hexpand(True)

        label4 = Gtk.Label(label="Things to do:")
        label4.set_hexpand(True)

        about = Gtk.Button(label="About Universe")
        about.set_hexpand(True)
        about.connect("clicked", self.on_about_clicked)

        contribute = Gtk.Button(label="Contribute")
        contribute.set_hexpand(True)
        contribute.connect("clicked", self.on_contribute_clicked)

        launcher = Gtk.Button(label="App Launcher")
        launcher.set_hexpand(True)
        launcher.connect("clicked", self.on_launcher_clicked)

        dashboard = Gtk.Button(label="Proceed to Dashboard")
        dashboard.set_hexpand(True)
        dashboard.connect("clicked", self.on_dashboard_clicked)

        terminal = Gtk.Button(label="TEST - Terminal (BROKEN)")
        terminal.set_hexpand(True)
        terminal.connect("clicked", self.on_terminal_clicked)

        button7 = Gtk.Button(label="Exit")
        button7.set_hexpand(True)
        button7.connect("clicked", Gtk.main_quit)

        grid1.attach(label1,  0, 2, 3, 2)
        grid1.attach(label2,  0, 4, 3, 2)
        grid1.attach(label3,  0, 6, 3, 1)
        grid1.attach(about, 0, 7, 1, 1)
        grid1.attach(contribute, 1, 7, 1, 1)
#        grid1.attach(launcher, 0, 16, 1, 1)
#        grid1.attach(terminal, 1 ,16, 1, 1)
        grid1.attach(dashboard, 1, 16, 1, 1)
        grid1.attach(button7, 2, 30, 1, 1)
        grid1.attach(label4,  0, 15, 3, 1)

        self.add(frame1)
        frame1.add(grid1)
       

    def on_terminal_clicked(self, widget):
        print("User chose: Launch Terminal")
        subprocess.run(
        win1.hide(),
        win3.show_all())
        
    def on_dashboard_clicked(self, widget):
        print("User chose: Proceed to Dashboard")
        subprocess.run(
        win1.hide(),
        dashboard.show_all())

    def on_about_clicked(self, widget):
        print("User chose: About Universe")
        subprocess.run(["xdg-open", "https://github.com/LinuxGamer/Universe/wiki/About"])

    def on_contribute_clicked(self, widget):
        print("User chose: Contribute")
        subprocess.run(["xdg-open", "https://github.com/LinuxGamer/Universe/blob/main/Docs/CONTRIBUTING.md"])

    def on_launcher_clicked(self, widget):
        print("User chose: App Launcher")
        subprocess.run(
        win1.hide(),
        win2.show_all())

    def save_settings(self, state):
        with open(settings, "w") as f:
            f.write("autostart=" + str(state))
            f.close()

    def load_settings(self):
        line = "True"
        if os.path.isfile(settings):
            with open(settings, "r") as f:
                lines = f.readlines()
                for i in range(len(lines)):
                    if "autostart" in lines[i]:
                        line = lines[i].split("=")[1].strip().capitalize()
                f.close()
        return line

    def startup_toggle(self, widget):
        if widget.get_active() is True:
            if os.path.isfile(source):
                shutil.copy(source, dest)
        else:
            if os.path.isfile(dest):
                os.unlink(dest)
        self.save_settings(widget.get_active())

# Window 2 - App Launcher
class MyWindow2(Gtk.Window):
    def __init__(self):
        super().__init__(title="Universe: App Launcher")

        self.set_border_width(10)
        self.set_default_size(640, 300)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_resizable(True)

        frame2 = Gtk.Frame(label="App Launcher")

        grid2 = Gtk.Grid(row_spacing    = 10,
                         column_spacing = 10,
                         column_homogeneous = True)

        #image1 = Gtk.Image()
        #image1.set_from_file("/home/dt/nc/Org/test/python-app/image1.png")

        label1 = Gtk.Label(label="App Launcher")
        label1.set_hexpand(True)

        label2 = Gtk.Label()
        label3 = Gtk.Label()

        firefox = Gtk.Button(label="Firefox")
        firefox.set_hexpand(True)
        firefox.connect("clicked", self.on_firefox_clicked)

        alacritty = Gtk.Button(label="Alacritty")
        alacritty.set_hexpand(True)
        alacritty.connect("clicked", self.on_alacritty_clicked)

        code = Gtk.Button(label="Visual Studio Code")
        code.set_hexpand(True)
        code.connect("clicked", self.on_code_clicked)

        blender = Gtk.Button(label="Blender")
        code.set_hexpand(True)
        code.connect("clicked", self.on_blender_clicked)

        writer = Gtk.Button(label="Libreoffice Writer")
        writer.set_hexpand(True)
        writer.connect("clicked", self.on_writer_clicked)

        nitrogen = Gtk.Button(label="Nitrogen")
        nitrogen.set_hexpand(True)
        nitrogen.connect("clicked", self.on_nitrogen_clicked)

        emacs = Gtk.Button(label="Emacs")
        emacs.set_hexpand(True)
        emacs.connect("clicked", self.on_emacs_clicked)

        dolphin = Gtk.Button(label="Dolphin")
        dolphin.set_hexpand(True)
        dolphin.connect("clicked", self.on_dolphin_clicked)

        gimp = Gtk.Button(label="GIMP")
        gimp.set_hexpand(True)
        gimp.connect("clicked", self.on_gimp_clicked)

        chrome = Gtk.Button(label="Chrome")
        chrome.set_hexpand(True)
        chrome.connect("clicked", self.on_chrome_clicked)

        chromium = Gtk.Button(label="Chromium")
        chromium.set_hexpand(True)
        chromium.connect("clicked", self.on_chromium_clicked)

        ls = Gtk.Button(label="LibreSprite (Legacy)")
        ls.set_hexpand(True)
        ls.connect("clicked", self.on_ls_clicked)

        steam = Gtk.Button(label="Steam")
        steam.set_hexpand(True)
        steam.connect("clicked", self.on_steam_clicked)

        button20 = Gtk.Button(label="Back To Main Menu")
        button20.set_hexpand(True)
        button20.connect("clicked", self.on_button20_clicked)

        button21 = Gtk.Button(label="Exit")
        button21.set_hexpand(True)
        button21.connect("clicked", Gtk.main_quit)

        #grid2.attach(image1,   0, 0, 4, 2)
        grid2.attach(label1,   0, 2, 4, 2)
        grid2.attach(label2,   0, 4, 4, 2)

        grid2.attach(label3,   0, 9, 4, 1)
        grid2.attach(button20, 0, 10, 2, 1)
        grid2.attach(button21, 2, 10, 2, 1)
# a b c d e f g h i j k l m n o p q r s t u v w x y z
        grid2.attach(alacritty,  0, 6, 1, 1)
        grid2.attach(blender, 1, 6, 1, 1)
        grid2.attach(chrome, 2, 6, 1, 1)
        grid2.attach(chromium, 3, 6, 1, 1)
        grid2.attach(dolphin, 0, 7, 1, 1)
        grid2.attach(emacs, 1, 7, 1, 1)
        grid2.attach(firefox,  2, 7, 1, 1)
        grid2.attach(gimp, 3, 7, 1, 1)
        grid2.attach(ls, 0, 8, 1, 1)
        grid2.attach(steam, 1, 8, 1, 1)
        grid2.attach(writer, 2, 8, 1, 1)
        grid2.attach(nitrogen, 3, 8, 1, 1)
        grid2.attach(code, 0, 9, 1, 1)







        self.add(frame2)
        frame2.add(grid2)

    def on_firefox_clicked(self, widget):
        print("Launcher: Firefox")
        subprocess.run(["firefox"])

    def on_alacritty_clicked(self, widget):
        print("Launcher: Alacritty")
        subprocess.run(["alacritty"])

    def on_code_clicked(self, widget):
        print("Launcher: Visual Studio Code")
        subprocess.run(["code"])

    def on_ls_clicked(self, widget):
        print("Launcher: LibreSprite (Legacy)")
        subprocess.run(["libresprite"])

    def on_steam_clicked(self, widget):
        print("Launcher: Steam")
        subprocess.run(["steam"])

    def on_blender_clicked(self, widget):
        print("Launcher: Blender")
        subprocess.run(["blender"])
    
    def on_writer_clicked(self, widget):
        print("Launcher: Libreoffice Writer")
        subprocess.run(["libreoffice --writer"])

    def on_nitrogen_clicked(self, widget):
        print("Launcher: Nitrogen")
        subprocess.run(["nitrogen"])

    def on_emacs_clicked(self, widget):
        print("Launcher: Emacs")
        subprocess.run(["emacs"])
    
    def on_dolphin_clicked(self, widget):
        print("Launcher: Dolphin")
        subprocess.run(["dolphin"])
    
    def on_gimp_clicked(self, widget):
        print("Launcher: GIMP")
        subprocess.run(["gimp"])
    
    def on_chrome_clicked(self, widget):
        print("Launcher: Chrome")
        subprocess.run(["chrome"])

    def on_chromium_clicked(self, widget):
        print("Launcher: Chromium")
        subprocess.run(["chromium"])
    
    def on_button20_clicked(self, widget):
        print("Back To Main Menu")
        win2.hide()
        win1.show_all()

    def on_button21_clicked(self, widget):
        print("Exit")
        button21.connect("clicked", Gtk.main_quit)

# Window 3 - Terminal
class MyWindow3(Gtk.Window):
    def __init__(self):
        super().__init__(title="Universe: Terminal Emulator")

        self.set_border_width(10)
        self.set_default_size(640, 300)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_resizable(True)
      
        
        
        frame3 = Gtk.Frame(label="Terminal Emulator")
        
        self.add(frame3)

        grid3 = Gtk.Grid(row_spacing    = 10,
                         column_spacing = 10,
                         column_homogeneous = True)

        exit = Gtk.Button(label="Exit")
        exit.set_hexpand(True)
        exit.connect("clicked", Gtk.main_quit)
        
        label1 = Gtk.Label(label="Terminal")
        label1.set_hexpand(True)

        menu = Gtk.Button(label="Back To Main Menu")
        menu.set_hexpand(True)
        menu.connect("clicked", self.on_menu_clicked)

        grid3.attach(label1, 1, 1, 1, 1)
        grid3.attach(menu, 1, 8, 1, 1)
        grid3.attach(exit, 2, 8, 1, 1)
        
        frame3.add(grid3)
        
    def on_menu_clicked(self, widget):
            print("Back To Main Menu")
            win3.hide()
            win1.show()

    def on_exit_clicked(self, widget):
            print("Exit")
            exit.connect("clicked", Gtk.main_quit)

        
class MyWindow4(Gtk.Window):
    def __init__(self):
        super().__init__(title="Universe: Dashboard")

        self.set_border_width(10)
        self.set_default_size(640, 300)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_resizable(True)



        frame3 = Gtk.Frame(label="Universe: Dashboard")

        self.add(frame3)

        grid3 = Gtk.Grid(row_spacing    = 10,
                         column_spacing = 10,
                         column_homogeneous = True)



win1 = MyWindow1()
win2 = MyWindow2()
win3 = MyWindow3()
dashboard = MyWindow4()

win1.connect("destroy", Gtk.main_quit)
win2.connect("destroy", Gtk.main_quit)
win3.connect("destroy", Gtk.main_quit)
dashboard.connect("destroy", Gtk.main_quit)


win1.show_all()
Gtk.main()
