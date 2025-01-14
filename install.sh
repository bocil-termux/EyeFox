#!/bin/bash

URL="https://download1592.mediafire.com/x3e53sd62zfgfuKeWqFP3FSOeTdVVIkL5kTz4gHB29pV2UZTxiDrsX1FMxOr_TnF3nQSscdCPuoLv--J3ulChRRnOSDMTBonYRMs7Ot2d4zHg7dMGcR33uF6MSzGTeNx-zqg4r4yRLysdz9EWw_BLPDN_pODUs8AUTUG_Xhwo9Ml/f8d1atyeu6g81fq/EyeFox.zip"

ZIP_FILE="downloaded_file.zip"

DEST_DIR="$HOME"

echo "Memulai proses download..."

wget -O "$ZIP_FILE" "$URL"

if [ $? -ne 0 ]; then
    echo "Gagal mendownload file. Periksa URL dan koneksi internet Anda."
    exit 1
fi

echo "File berhasil didownload ke direktori $(pwd)."

echo "Ekstraksi file ke direktori $DEST_DIR..."

unzip -o "$ZIP_FILE" -d "$DEST_DIR"

if [ $? -ne 0 ]; then
    echo "Gagal mengekstrak file. Pastikan file adalah file ZIP yang valid."
    rm -f "$ZIP_FILE"
    exit 1
fi

echo "Ekstraksi selesai. Tools berada di direktori home dengan nama EyeFox."
