from gi.repository import Gtk, GLib, Gdk
from puzle1 import*
import threading
import time
import gi

gi.require_version("Gtk", "3.0")


class Window(Gtk.Window):

    def __init__(self):
