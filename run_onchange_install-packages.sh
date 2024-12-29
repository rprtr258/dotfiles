#!/bin/bash

sudo apt install git ripgrep flatpak curl wget polybar fonts-liberation rofi imagemagick feh parcellite xclip
# alacritty
flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo
flatpak install flathub org.telegram.desktop

wget https://go.dev/dl/go1.23.4.linux-amd64.tar.gz
rm -rf /usr/local/go && tar -C /usr/local -xzf go1.23.4.linux-amd64.tar.gz
rm go1.23.4.linux-amd64.tar.gz
export PATH=$PATH:/usr/local/go/bin
go version

