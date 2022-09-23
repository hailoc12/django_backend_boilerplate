#
# Install Firefox
echo "Install Firefox"
sudo apt install firefox

echo "Install Tor"
sudo apt install tor
sudo cp resource/torrc /etc/tor/

# Copy driver to work with selenimum
echo "Copy Geckodriver"
sudo cp resource/geckodriver /usr/bin

# Install python3 lib
echo "Install Python3 lib"
pip3 install -r requirements.txt

echo "Finish !"
