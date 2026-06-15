import streamlit as st

st.title("Chat IA de Dayana")

mensaje = st.text_area("Escribe tu mensaje")

if st.button("Analizar"):

    texto = mensaje.lower()

    if "matricula" in texto:
        st.success("Intención detectada: Matrícula")

    elif "contraseña" in texto:
        st.success("Intención detectada: Acceso a plataforma")

    elif "pago" in texto:
        st.success("Intención detectada: Consulta de pagos")

    else:
        st.warning("Intención no identificada")