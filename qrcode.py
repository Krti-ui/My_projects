import qrcode

data = "https://www.amazon.in/LEGO-Mercedes-AMG-Performance-Pull-Back-42165/dp/B0CFVYZRN1/ref=sr_1_14?crid=373G8ZWRPHHPU&dib=eyJ2IjoiMSJ9.HBgEnS20x6F6R14L9h96n-XHSNDWcWCmxPk4joySp5pynrN04DnFBD4VOJDHBvl43keCWOlMtGkaFPYA9Qlgg4qMsbZ_CJUzUwLg98-Lam2rgHbI_DED_mrZ7dY5Z4In0om0jGQJul9eNm6UnIQE-r4y2PmIlMmu9_SJFG574t3h36UopslbYfBfXu91KyLcQbNHa5_U-2YJ7sVWOELDFQtMD33VL4pDGPl1D2dYrRz5Z8iBVDfI45VTbGr7ZBKwHanJMvGLdpqqeoG4BDbi-YoljQKepUuPgVoFmDh_LpA.Lrh43pO7p7aBEVYUblwWgaMi6TkErFIO9T1lFNJ6DXc&dib_tag=se&keywords=f1&qid=1753597202&sprefix=f1%2Caps%2C326&sr=8-14"

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
img.save("okay.png")
