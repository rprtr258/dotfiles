#!/usr/bin/env bash

ROFI_FB_PREV_LOC_FILE=~/.local/share/rofi/rofi_fb_prevloc

# Create the directory for the files of the script
if [ ! -d "$(dirname "${ROFI_FB_PREV_LOC_FILE}")" ]; then
    mkdir -p "$(dirname "${ROFI_FB_PREV_LOC_FILE}")"
fi

if [ -f "${ROFI_FB_PREV_LOC_FILE}" ]; then
    ROFI_FB_CUR_DIR=$(cat "${ROFI_FB_PREV_LOC_FILE}")
fi

if [ $@ ] && [ $@ != "\n" ]; then
    if [[ "$@" == /* ]]; then
        ROFI_FB_CUR_DIR="$@"
    else
        ROFI_FB_CUR_DIR="${ROFI_FB_CUR_DIR}/$@"
    fi
else
    ROFI_FB_CUR_DIR="$HOME"
fi

# If argument is no directory.
if [ ! -d "${ROFI_FB_CUR_DIR}" ]; then
    coproc xdg-open "${ROFI_FB_CUR_DIR}" >/dev/null 2>&1
    if [ -x "${ROFI_FB_CUR_DIR}" ]; then
        # TODO: undo?
        #coproc ( "${ROFI_FB_CUR_DIR}" >/dev/null 2>&1 )
        exec 1>&-
        exit;
    elif [ -f "${ROFI_FB_CUR_DIR}" ]; then
        echo "$HOME" > "${ROFI_FB_PREV_LOC_FILE}"
        exit;
    fi
    exit;
fi

# Process current dir.
if [ -n "${ROFI_FB_CUR_DIR}" ]; then
    ROFI_FB_CUR_DIR=$(readlink -e "${ROFI_FB_CUR_DIR}")
    echo "${ROFI_FB_CUR_DIR}" > "${ROFI_FB_PREV_LOC_FILE}"
    pushd "${ROFI_FB_CUR_DIR}" >/dev/null
fi

# Output to rofi
pwd # TODO: move to message
# TODO: suggest location from prev session
# TODO: bookmarks
echo ".."
ls
# TODO: search in subdirs
#find $(pwd) | xargs -I {} realpath --relative-to="/mnt/hdd/GTD" "{}"

