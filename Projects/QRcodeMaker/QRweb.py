import qrcode
import streamlit as st
from io import BytesIO

st.title("QR Code Generator")

url = st.text_input("Enter the URL")

if st.button("Generate QR"):
    qr = qrcode.QRCode()
    qr.add_data(url)
    img = qr.make_image()

    # convert image to bytes for displaying on webpage
    buf = BytesIO()
    img.save(buf, format="PNG")
    byte_im = buf.getvalue()

    st.image(byte_im, caption="Your QR Code")

    # download button
    st.download_button(
        label="Download QR Code",
        data=byte_im,
        file_name="qrcode.png",
        mime="image/png"
    )
