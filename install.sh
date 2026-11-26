#!/usr/bin/env bash
set -euo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

mkdir -p "${HOME}/.config" "${HOME}/.local/bin" "${HOME}/.local/share/applications"

for dir in qtile rofi dunst nvim-hyprland; do
    mkdir -p "${HOME}/.config/${dir}"
    cp -r "${REPO_DIR}/config/${dir}/." "${HOME}/.config/${dir}/"
done
cp "${REPO_DIR}/config/x-orbit-qtile-mimeapps.list" "${HOME}/.config/"

install -m 755 "${REPO_DIR}/bin/start-orbit-qtile" "${HOME}/.local/bin/"
install -m 755 "${REPO_DIR}/bin/orbit-nvim" "${HOME}/.local/bin/"
install -m 755 "${REPO_DIR}/bin/orbit-nvim-cli" "${HOME}/.local/bin/"

"${REPO_DIR}/apps/orbit-files/install-desktop.sh"
"${REPO_DIR}/apps/orbit-suite/install-suite.sh"

if [[ "${1:-}" == "--with-session" ]]; then
    sudo install -m 755 "${REPO_DIR}/bin/start-orbit-qtile" /usr/local/bin/start-orbit-qtile
    sudo install -m 644 "${REPO_DIR}/config/qtile/orbit-qtile.desktop" /usr/share/wayland-sessions/orbit-qtile.desktop
    echo "Installed Orbit Desktop (Qtile) Wayland session."
fi

echo "Orbit Desktop (Qtile) installed successfully."
