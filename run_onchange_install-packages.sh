#!/bin/bash

sudo apt install git ripgrep flatpak curl alacritty polybar fonts-liberation rofi imagemagick feh parcellite xclip
flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo
flatpak install flathub org.telegram.desktop

