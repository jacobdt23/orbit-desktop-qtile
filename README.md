# Orbit Desktop (Qtile)

A 100% **Python** desktop environment built on **Qtile (Wayland)** paired with the custom **Orbit Suite** of native Python **GTK 4 + Libadwaita** desktop apps and an isolated **LazyVim** configuration (`NVIM_APPNAME=nvim-hyprland`).

Scoped with `XDG_CURRENT_DESKTOP=X-Orbit-Qtile:Qtile` so it coexists cleanly alongside **COSMIC**, **Omarchy**, and **Orbit Desktop (Hyprland)**.

## What's Inside

- **`config/qtile`** — Modular Python Qtile config (`config.py`, `autostart.sh`, `modules/`) with Tokyo Night frosted palette, dual 1080p@100Hz monitor support, and Orbit Suite keybindings.
- **`apps/orbit-files`** — Python GTK 4 + Libadwaita file manager (tabs, split view, sidebar, preview pane, drag-and-drop, Trash).
- **`apps/orbit-suite`** — Companion Python GTK 4 + Libadwaita apps (`orbit-term`, `orbit-view`, `orbit-launch`, `orbit-edit`).
- **`config/nvim-hyprland`** — Isolated LazyVim setup (`tokyonight-night`).
- **`config/rofi`**, **`config/dunst`**, **`config/x-orbit-qtile-mimeapps.list`** — Notifications, Rofi fallback, and per-session MIME defaults.

## Quick Install

```bash
./install.sh
```

To also install the SDDM Wayland session (`/usr/share/wayland-sessions/orbit-qtile.desktop` and `/usr/local/bin/start-orbit-qtile`):

```bash
./install.sh --with-session
```
