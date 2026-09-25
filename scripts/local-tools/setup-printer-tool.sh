#!/usr/bin/env bash
# Klont das MXW01-Thermodrucker-Tool lokal als Abhängigkeit für create-account-printout.py.
# Wird nicht committed (siehe .gitignore) — das Tool hat keine LICENSE-Datei im Repo.
set -euo pipefail

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENDOR_DIR="$DIR/vendor/mxw01"
VENV_DIR="$DIR/venv"

if [ ! -d "$VENDOR_DIR" ]; then
  mkdir -p "$DIR/vendor"
  git clone --depth 1 https://github.com/PinThePenguinOne/MXW01_Thermal-Printer-Tool.git "$VENDOR_DIR"
  rm -rf "$VENDOR_DIR/.git"
else
  echo "MXW01-Tool liegt schon unter $VENDOR_DIR — überspringe Klonen."
fi

python3 "$DIR/patch-mxw01.py"

if [ ! -d "$VENV_DIR" ]; then
  # macOS/Homebrew-Python verweigert systemweite pip-Installs (PEP 668) — daher venv
  python3 -m venv "$VENV_DIR"
else
  echo "venv liegt schon unter $VENV_DIR — überspringe Erstellen."
fi

"$VENV_DIR/bin/pip" install --quiet --upgrade pip
"$VENV_DIR/bin/pip" install --quiet -r "$VENDOR_DIR/requirements.txt"

echo ""
echo "Fertig. Als nächstes:"
echo "  cp $DIR/.env.example $DIR/.env   # und ausfüllen"
echo "  python3 $DIR/create-account-printout.py <benutzername> kinder   # startet sich selbst im venv neu"
