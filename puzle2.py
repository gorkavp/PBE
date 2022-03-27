from gi.repository import Gtk, GLib, Gdk
from puzle1 import *
import threading
import gi

gi.require_version("Gtk", "3.0")


class Window(Gtk.Window):

    def __init__(self):

        # Instancia de argumentos
        self.rf = RfidPN532()

        # Creación de la ventana
        super().__init__(title="Puzle 2")
        self.set_position(True)
        self.set_border_width(15)

        # Creación de la Box donde colocaremos los elementos de la ventana
        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=15)
        self.box.set_homogeneous(False)
        self.add(self.box)

        # Creación del label inicial
        self.label = Gtk.Label(label="Please, login with your university card")
        self.label.set_justify(Gtk.Justification.CENTER)
        self.label.set_size_request(500, 200)
        self.box.pack_start(self.label, True, True, 0)

        # Creación y conexión del boton clear
        self.button = Gtk.Button(label="Clear")
        self.button.connect("clicked", self.on_button_clicked)
        self.box.pack_start(self.button, True, True, 0)

        # CSS
        self.cssProvider = Gtk.CssProvider()
        self.cssProvider.load_from_path("style.css")
        self.styleContext = Gtk.StyleContext()
        self.styleContext.add_provider_for_screen(Gdk.Screen.get_default(
        ), self.cssProvider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)
        self.label.get_style_context().add_class("no_uid")
        self.button.set_sensitive(False)

    def on_button_clicked(self, widget):

        self.label.set_markup("Please, login with your university card")
        self.label.get_style_context().remove_class("si_uid")
        self.label.get_style_context().add_class("no_uid")
        self.button.set_sensitive(False)
        thread = threading.Thread(target=self.read_card, daemon=True)
        thread.start()

    def show_uid(self):

        self.label.get_style_context().remove_class("no_uid")
        self.label.get_style_context().add_class("si_uid")
        self.label.set_markup("UID: <b> " + self.uid + "</b>")
        self.button.set_sensitive(True)

    def read_card(self):

        self.uid = self.rf.read_uid()
        if self.uid == "ED677B29":
            GLib.idle_add(self.show_uid)
        else:
            self.read_card()

# Código principal programa


def app_main():

    w = Window()
    w.connect("destroy", Gtk.main_quit)
    w.show_all()

    thread = threading.Thread(target=w.read_card, daemon=True)
    thread.start()


if __name__ == "__main__":
    app_main()
    Gtk.main()
