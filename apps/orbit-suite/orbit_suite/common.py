"""Shared GTK 4 / Libadwaita Dracula bootstrap helpers for Orbit Suite."""

from __future__ import annotations

import gi

gi.require_version("Gtk", "4.0")
gi.require_version("Gdk", "4.0")
gi.require_version("Adw", "1")
gi.require_version("GdkPixbuf", "2.0")

from gi.repository import Gdk, Gtk

DRACULA_BASE_CSS = """
@define-color accent_color #bd93f9;
@define-color accent_bg_color #bd93f9;
@define-color accent_fg_color #21222c;
@define-color window_bg_color #282a36;
@define-color window_fg_color #f8f8f2;
@define-color view_bg_color #282a36;
@define-color view_fg_color #f8f8f2;
@define-color headerbar_bg_color #21222c;
@define-color headerbar_fg_color #f8f8f2;
@define-color headerbar_border_color #44475a;
@define-color sidebar_bg_color #21222c;
@define-color sidebar_fg_color #f8f8f2;
@define-color card_bg_color #343746;
@define-color card_fg_color #f8f8f2;
@define-color popover_bg_color #21222c;
@define-color popover_fg_color #f8f8f2;
@define-color dialog_bg_color #282a36;
@define-color dialog_fg_color #f8f8f2;

windowcontrols button.close,
windowcontrols button.maximize,
windowcontrols button.minimize {
    background-image: none;
    border-radius: 9999px;
    min-width: 16px;
    min-height: 16px;
    padding: 0;
    margin: 0 4px;
    box-shadow: none;
    border: none;
    color: transparent;
}

windowcontrols button.minimize { background-color: #ffb86c; }
windowcontrols button.maximize { background-color: #50fa7b; }
windowcontrols button.close    { background-color: #ff5555; }

windowcontrols button.minimize:hover,
windowcontrols button.minimize:active {
    background-color: #ffb86c;
    color: #21222c;
}

windowcontrols button.maximize:hover,
windowcontrols button.maximize:active {
    background-color: #50fa7b;
    color: #21222c;
}

windowcontrols button.close:hover,
windowcontrols button.close:active {
    background-color: #ff5555;
    color: #21222c;
}

windowcontrols button.close:backdrop,
windowcontrols button.maximize:backdrop,
windowcontrols button.minimize:backdrop {
    background-image: none;
    background-color: #6272a4;
    color: transparent;
}
"""


def load_css_string(css: str) -> None:
    """Register Dracula GTK4/Libadwaita CSS and window-control styling on the default display."""
    provider = Gtk.CssProvider()
    provider.load_from_string(DRACULA_BASE_CSS + "\n" + css)
    display = Gdk.Display.get_default()
    if display is not None:
        Gtk.StyleContext.add_provider_for_display(
            display,
            provider,
            Gtk.STYLE_PROVIDER_PRIORITY_USER,
        )
