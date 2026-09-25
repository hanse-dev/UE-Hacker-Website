#!/usr/bin/env bash
# Klont das MXW01-Thermodrucker-Tool lokal als Abhängigkeit für create-account-printout.py.
# Wird nicht committed (siehe .gitignore) — das Tool hat keine LICENSE-Datei im Repo.
set -euo pipefail

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENDOR_DIR="$DIR/vendor/mxw01"

if [ -d "$VENDOR_DIR" ]; then
  echo "MXW01-Tool liegt schon unter $VENDOR_DIR — nichts zu tun."
  exit 0
fi

mkdir -p "$DIR/vendor"
git clone --depth 1 https://github.com/PinThePenguinOne/MXW01_Thermal-Printer-Tool.git "$VENDOR_DIR"
rm -rf "$VENDOR_DIR/.git"

echo ""
echo "Fertig. Als nächstes:"
echo "  pip install -r $VENDOR_DIR/requirements.txt"
echo "  cp $DIR/.env.example $DIR/.env   # und ausfüllen"
