import segno

qrcode = segno.make_qr("https://armigergames.itch.io/")
qrcode.save("armiger_games_qr_code.png", scale=15, border=2)