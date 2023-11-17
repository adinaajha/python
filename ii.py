import streamlit as st
from streamlit_option_menu import option_menu
import requests
from streamlit_lottie import st_lottie

st.set_page_config(layout= "wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
      return None
    return r.json()

lottie_coder1 = load_lottieurl("https://lottie.host/34e78baa-759e-4306-b1f0-0ba29c288e9a/uWCV4rF7Wu.json")
lottie_coder2 = load_lottieurl("https://lottie.host/cdbcacd4-abe2-489f-b59a-fd36dc907086/KqckIcezhk.json")
lottie_coder3 = load_lottieurl("https://lottie.host/6b69c3fe-e094-435a-8b5d-affd578c02a2/L3lYYqqt6D.json")
lottie_coder4 = load_lottieurl("https://lottie.host/e991dae4-ad0a-41ad-8a31-942d07f75f80/DZoHPPfOCH.json")
lottie_coder5 = load_lottieurl("https://lottie.host/e8cb280b-0fe1-4065-84aa-2f2bcacdf8c7/IgoKP53Byk.json")
lottie_coder6 = load_lottieurl("https://lottie.host/f44996b0-956f-4b2a-b722-05a23d1d139d/lB4hdrD7MG.json")
                               
st.write("##")
st.subheader("Hey Guys Ini Tugas website portfolio saya:wave:")
st.title("Perkenalkan Nama saya Adina dan saya sedang melakukan study di Universitas Stmik Ikmi Cirebon")
st.write("""Selamat datang di portofolio digital saya untuk mengungkap keahlian, pencapaian, dan potensi kontribusi saya pada organisasi Anda:smile:
""")
st.write("Silahkan Kunjungi link dibawah ini https://adinaajha.github.io/memory/")
st.write('---')

with st.container():
    selected = option_menu(
        menu_title = None,
        options =['About Me','Skill','Goals and Aspiration', 'Contact Page','Home','Settings'],
        icons = ['person','book','bar-chart','mailbox','person','mailbox'],
        orientation= 'horizontal'
    )     
if selected == 'About Me':

    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.write("##")
            st.subheader("Hey Guys :wave:, Perkenalkan saya ADINA dan saya sekarang sedang melakukan study di Stmik ikmi cirebon :snowflake: .")
            st.subheader("Saya seorang profesional yang bermotivasi tinggi dan berorientasi pada hasil dengan hasrat untuk memecahkan masalah dan belajar terus-menerus. Sebagai pemasar berpengalaman, saya berkembang dalam lingkungan yang dinamis dan memiliki rekam jejak dalam menyampaikan kampanye yang sukses. Berdedikasi dan berorientasi pada detail, saya memiliki latar belakang yang kuat di bidang keuangan dan kemampuan yang terbukti untuk menyederhanakan proses. Dengan keterampilan komunikasi yang baik dan pola pikir kolaboratif, saya menikmati bekerja dalam tim yang berbeda-beda.:fist:.")
        with col2:
            st_lottie(lottie_coder1)
    st.write("---")

if selected =="Skill":
    with st.container():
        col3, col4 = st.columns(2)
        with col3:
         st.subheader("""
         Saya Suka Belajar Hal Baru
                      Blogging: CSS, HTML, WordPress, Sistem Manajemen Konten/Content Management System (CMS)
                      Search Engine Optimization (SEO): Google Analytics, Google Search Console, Google Pagespeed Insight, Google Mobile-Friendly Test, Google Ads Keyword Planner, Google Trend, Ahrefs, 
                      Ahrefs’ Backlink Checker, Ahrefs, SEO Toolbar, Moz, SEMrush, GTmetrix, Yoast SEO, Classy Schema Structured Data Viewer, SERP Robot, SERPsim, XML Sitema
                      
Media Sosial: Facebook, Instagram, Pinterest, Twitter, YouTube, Hootsuite
                      Pembuatan Web: Wix, Weebly, Squarespace, WordPress, Web.com, Pembuat Web HubSpot, Gator, Shopify
                      

        """)
        with col4:
            st_lottie(lottie_coder2)
    st.write("---")

if selected == 'Goals and Aspiration':

    with st.container():
        col5, col6 = st.columns(2)
        with col5:
            st.write("##")
            st.write("Halo 👋, saya Adina, dan saat ini saya sedang melakukan study di Stmik ikmi kota cirebon 🎓, dan dengan bangga saya sampaikan bahwa saya telah berhasil menyelesaikan tugas portfolio ini🎖️ .")

        with col6:
            st_lottie(lottie_coder3)
    st.write("---")

 
if selected == 'Home':

    with st.container():
        col7, col8 = st.columns(2)
        with col7:
            st.write("##")
            st.subheader("Hey Guys :wave:, Perkenalkan saya ADINA dan saya sekarang sedang melakukan study di Stmik ikmi cirebon :snowflake: .")
            st.subheader("Saya seorang profesional yang bermotivasi tinggi dan berorientasi pada hasil dengan hasrat untuk memecahkan masalah dan belajar terus-menerus. Sebagai pemasar berpengalaman, saya berkembang dalam lingkungan yang dinamis dan memiliki rekam jejak dalam menyampaikan kampanye yang sukses. Berdedikasi dan berorientasi pada detail, saya memiliki latar belakang yang kuat di bidang keuangan dan kemampuan yang terbukti untuk menyederhanakan proses. Dengan keterampilan komunikasi yang baik dan pola pikir kolaboratif, saya menikmati bekerja dalam tim yang berbeda-beda.:fist:.")
        with col8:
            st_lottie(lottie_coder5)
    st.write("---")

if selected == 'Settings':

    with st.container():
        col9, col10 = st.columns(2)
        with col9:
            st.write("##")
            st.write("")

        with col10:
            st_lottie(lottie_coder6)
    st.write("---")


if selected == 'Contact Page':
    st.header("Get in Touch! Via Mail Or Via github")
    st.write("adinaajha335@gmail.com")
    st.write(" https://adinaajha.github.io/memory/")
    st_lottie(lottie_coder4)
    st.write('---')