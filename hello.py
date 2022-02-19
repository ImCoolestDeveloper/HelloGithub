import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

class Image(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)
        self.set_title("Hellooooo!")
        self.connect("destroy", Gtk.main_quit)
        
        screen = Gdk.Screen.get_default()
        provider = Gtk.CssProvider()
        style_context = Gtk.StyleContext()
        style_context.add_provider_for_screen(
            screen, provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )
        css = b"""
        imgg  {
			border: solid 2px red;
        }
        """
        provider.load_from_data(css)
        image = Gtk.Image()
        image.set_from_file("hello.png")     
        eb = Gtk.EventBox()   
        img_context = image.get_style_context()
        img_context.add_class("imgg")     
        eb.add(image)
        self.add(eb)

window = Image()
window.show_all()

Gtk.main()
