#!/bin/bash

set -e

echo "==============================================================="
echo "   Auto-Installer for Cowrie & Extropy by Pixelman0195     "
echo "==============================================================="

echo "[+] Updating system and installing dependencies..."
sudo apt-get update && sudo apt-get upgrade -y

sudo apt-get install -y git python3 python3-pip python3-venv libatlas-base-dev libffi-dev libssl-dev authbind

echo "[+] Creating new user 'cowrie'..."
if id "cowrie" &>/dev/null; then
    echo "User 'cowrie' detected, skipping"
else
    sudo adduser --disabled-password --gecos "" cowrie
fi

echo "[+] Installing Cowrie Honeypot..."
sudo su - cowrie -c "
    if [ ! -d '/home/cowrie/cowrie' ]; then
        git clone http://github.com/cowrie/cowrie /home/cowrie/cowrie
    fi
    cd /home/cowrie/cowrie

    python3 -m venv cowrie-env
    source cowrie-env/bin/activate
    pip install --upgrade pip
    pip install -r requirements.txt
"
echo "[+] Configuring the CTI environment..."
cd ~
if [ ! -d 'Extropy' ]; then
    mkdir Extropy
fi
cd Extropy

python3 -m venv cti-env
source cti-env/bin/activate

echo "Installing Python libraries"
pip install --upgrade pip
pip install folium requests numpy keyring

echo "====================================================="
echo "         Installation completed successfully!        "
echo "====================================================="
echo "In order to start enter:"
echo "sudo su - cowrie"
echo "cd cowrie && source cowrie-env/bin/activate"
echo "cowrie start"
echo "====================================================="
