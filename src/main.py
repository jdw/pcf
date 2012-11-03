from fractal import Fractal
from util import drange


def main_urwid():
    import urwid

    def show_or_exit(key):
        if key in ('q', 'Q'):
            raise urwid.ExitMainLoop()
        txt.set_text(repr(key))

    palette = [
        ('standard', 'yellow', 'black')]

    txt = urwid.Text(u"Hello World")
    fill = urwid.Filler(txt, 'top')
    m = urwid.AttrMap(fill, 'standard')
    scr = urwid.raw_display.Screen()
    loop = urwid.MainLoop(m, palette, screen=scr, unhandled_input=show_or_exit)
    loop.run()


def main():
    epsilon = 0.1
    for x in drange(-2, 2, epsilon):
        for y in drange(-2, 2, epsilon):
            print Fractal.CALCULATE((x, y), 30)


if __name__ == "__main__":
    main_urwid()
