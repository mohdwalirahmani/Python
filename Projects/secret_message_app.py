import streamlit as st
import random
import string

def random3():
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(3))

def encode_message(msg):
    words = msg.split(" ")
    nwords = []
    for word in words:
        if len(word) >= 3:
            r1 = random3()
            r2 = random3()
            stnew = r1 + word[1:] + word[0] + r2
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    return " ".join(nwords)

def decode_message(msg):
    words = msg.split(" ")
    nwords = []
    for word in words:
        if len(word) >= 3:
            stnew = word[3:-3]
            stnew = stnew[-1] + stnew[:-1]
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    return " ".join(nwords)

# UI

st.title("🔐 Secret Message Encoder / Decoder")
st.write("Convert your text into secret code language and decode it back.")

mode = st.radio("Choose Mode:", ["Encode", "Decode"])

text = st.text_area("Enter your message:")

if st.button("Submit"):
    if mode == "Encode":
        output = encode_message(text)
        st.success("Encoded Message:")
        st.code(output)
    else:
        output = decode_message(text)
        st.success("Decoded Message:")
        st.code(output)
