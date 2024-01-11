import qrcode

def generate_qrcode(url):
    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size = 10,
        border = 4
    )
    
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color = "black", back_color = "white")
    img.save("abimael_doppel.png")

generate_qrcode("https://www.instagram.com/abimael.doppel?utm_source=ig_web_button_share_sheet&igsh=ZDNlZDc0MzIxNw==")
    