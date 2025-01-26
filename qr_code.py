import streamlit as st
import qrcode
from io import BytesIO
import os
st.title('QR Code Generator')
st.write('Create a QR Code for any text or URL')

data = st.text_area('Enter the text or URL: ').strip()
file_name = st.text_input('Enter the filename. (without extension)').strip()

if file_name:
    folder_path = 'QR Codess'
    os.makedirs(folder_path, exist_ok=True)
    file_path = os.path.join(folder_path, file_name + ".png")
else:
    file_path = None
if st.button('Make QR'):
    if not data:
        st.error("Please enter some text or URL to generate the QR code.")
    else:
        qr = qrcode.QRCode(box_size=10, border=4)
        qr.add_data(data)
        qr.make(fit=True)
        image = qr.make_image(fill_color="black", back_color="white")

        buffer = BytesIO()
        image.save(buffer, format="PNG")
        buffer.seek(0)

        st.image(buffer, caption="Your QR Code")

        if file_path:
            try:
                image.save(file_path)
                st.success(f"QR Code saved as {file_name}.png")
            except Exception as e:
                st.error(f"Error saving file: {e}")
        else:
            st.warning("No file name provided. QR Code not saved.")
