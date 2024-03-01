import qrcode
from PIL import Image

def generate_qr_code(url, color, background="#FFFFFF00"):

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color=color, back_color=background[:7])
    img = img.convert("RGBA")  
    data = img.getdata()

    new_data = []
    for item in data:
        if item[:3] == tuple(int(background[i:i+2], 16) for i in (1, 3, 5)):
            new_data.append(tuple(int(background[i:i+2], 16) for i in (1, 3, 5)) + (0,))  # Keep background transparent
        else:
            new_data.append(tuple(int(color[i:i+2], 16) for i in (1, 3, 5)) + (255,))  # Color QR code modules

    img.putdata(new_data)
    img.save("qr_code.png", format="PNG")

if __name__ == "__main__":
    
    generate_qr_code('URL', 'DESIRED COLOR IN #XXXX')
