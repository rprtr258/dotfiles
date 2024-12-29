#!/bin/bash

sudo apt install git ripgrep flatpak curl wget polybar fonts-liberation rofi imagemagick feh parcellite xclip
# alacritty
flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo
flatpak install flathub org.telegram.desktop

check_go_installed() {
  if [ -z "$(command -v go)" ] || [ "$(go version)" != "go version go1.23.4 linux/amd64" ]; then
    return 0
  else
    return 1
  fi
}
if check_go_installed; then
  wget https://go.dev/dl/go1.23.4.linux-amd64.tar.gz
  sudo rm -rf /usr/local/go && sudo tar -C /usr/local -xzf go1.23.4.linux-amd64.tar.gz
  rm go1.23.4.linux-amd64.tar.gz
  go version
fi
go install github.com/junegunn/fzf@latest

