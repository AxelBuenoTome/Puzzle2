import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib, Pango, Gdk

from threading import Thread
from puzzle1 import RfidReader  # Importa la clase desde el otro archivo

class RFID_GUI(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="NFC Card Reader")
        self.set_default_size(400, 200)

        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.add(self.box)

        # Inicialmente muestra el mensaje de bienvenida
        self.label = Gtk.Label(label="Please, login with your university card", name="label")
        self.label.set_markup('<span size="x-large" weight= "bold" foreground="white">Please, login with your university card</span>')
        self.label.get_style_context().add_class("welcome-label")
        self.label.override_background_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(0, 0, 1, 1))  # Cambia el color de fondo a azul
        self.box.pack_start(self.label, True, True, 0)

        self.clear_button = Gtk.Button(label="Leer otro UID")
        self.clear_button.set_size_request(50, 30)  # Establece el tamaño deseado
        self.clear_button.set_halign(Gtk.Align.CENTER)  # Centra horizontalmente
        self.clear_button.connect("clicked", self.clear_uid)
        self.box.pack_start(self.clear_button, False, False, 0) #Para que el botón no ocupe todo ponemos False
        
        self.rfid = RfidReader()
        self.is_reading = True  # Inicialmente, el programa comienza leyendo automáticamente
        self.read_thread = Thread(target=self.read_uid_thread)
        self.read_thread.start()

    def clear_uid(self, widget):
        
        self.label.set_markup('<span size="x-large" weight= "bold" foreground="white">Please, login with your university card</span>')
        self.label.override_background_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(0, 0, 1, 1))  # Cambia el color de fondo a azul
        self.is_reading = True #una vez pulsemos el botón, hacemos que vuelva a leer un UID
        
    def read_uid_thread(self):
        while True:
            if self.is_reading:
                uid = self.rfid.read_uid()
                GLib.idle_add(self.show_uid, uid)
                self.is_reading = False #cambiamos a False para que no siga leyendo y modificando la interfaz.

    def show_uid(self, uid):
        self.label.set_markup('<span size="xx-large" weight= "bold" foreground="white">UID: {0}</span>'.format(uid))
        self.label.override_background_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(0, 0.85, 0, 1))  # Cambia el color de fondo a verde
        
if __name__ == "__main__":
    win = RFID_GUI()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()
