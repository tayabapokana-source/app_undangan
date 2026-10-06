import streamlit as st
import datetime

# 1. Konfigurasi Awal Tampilan Layar (Agar Pas Saat Dibuka di Chrome HP)
st.set_page_config(page_title="Undangan Pernikahan - Budi & Citra", page_icon="💍", layout="centered")

# Menggunakan CSS Kustom untuk membuat tema warna Wedding yang elegan dan estetik
st.markdown("""
    <style>
    .stApp {
        background-color: #FAF6F0; /* Warna cream soft premium */
        color: #4A3E3D; /* Warna teks cokelat gelap hangat */
        font-family: 'Georgia', serif;
    }
    h1, h2, h3 {
        text-align: center;
        color: #8C6239; /* Warna emas tembaga */
    }
    .wedding-box {
        background-color: #FFFFFF;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(140, 98, 57, 0.15);
        border: 1px solid #EADBC8;
        margin-bottom: 20px;
    }
    div.stButton > button:first-child {
        background: linear-gradient(135deg, #8C6239 0%, #B89775 100%);
        color: white;
        border-radius: 8px;
        width: 100%;
        font-weight: bold;
        border: none;
        padding: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# ==============================================================================
# 1. HALAMAN PEMBUKA / HEADER UNDANGAN
# ==============================================================================
st.markdown("<h3 style='text-align: center; font-style: italic;'>The Wedding of</h3>", unsafe_allow_html=True)
st.markdown("<h1 style='font-size: 42px;'>Budi & Citra</h1>", unsafe_allow_html=True)
st.write("---")

# Trik Musik Romantis: Otomatis memutar backsound mp3 gratis dari internet (bisa kamu ganti filenya nanti)
url_musik = "https://soundhelix.com"
st.audio(url_musik, format="audio/mp3", loop=True)
st.caption("🎵 Geser volume di atas untuk menyalakan musik latar")

# ==============================================================================
# 2. PROFIL KEDUA MEMPELAI
# ==============================================================================
st.markdown("<div class='wedding-box'>", unsafe_allow_html=True)
st.markdown("### 💍 Pasangan Mempelai", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.markdown("<h4 style='text-align:center;'>Budi Santoso, S.Kom</h4>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; font-size:12px;'>Putra dari Bp. Ahmad & Ibu Siti</p>", unsafe_allow_html=True)

with col2:
    st.markdown("<h4 style='text-align:center;'>Citra Lestari, S.E</h4>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; font-size:12px;'>Putri dari Bp. Bambang & Ibu Sri</p>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# ==============================================================================
# 3. DETAIL ACARA & MAPS WIDGET
# ==============================================================================
st.markdown("<div class='wedding-box'>", unsafe_allow_html=True)
st.markdown("### 📅 Waktu & Lokasi Acara", unsafe_allow_html=True)

# Menampilkan tanggal dengan widget kalender bawaan streamlit agar rapi
hari_h = <layout>followupButton(query="""Add the The Wedding of Budi & Citra on Sunday, November 8, 2026 to my calendar""", label="""Minggu, 8 November 2026""", variant=FOLLOWUP_BUTTON_VARIANT_DATE_DROPDOWN)</layout>
st.markdown(f"<p style='text-align:center; font-weight:bold;'>Hari/Tanggal: {hari_h}</p>", unsafe_allow_html=True)

st.markdown("""
<p style='text-align:center; margin-bottom:0;'><b>💎 Akad Nikah:</b> 09.00 - 10.00 WIB</p>
<p style='text-align:center;'><b>🎉 Resepsi:</b> 11.00 - 14.00 WIB</p>
<p style='text-align:center; font-style:italic;'><b>📍 Gedung Istana Langit</b><br>Jl. Pahlawan Cinta No. 100, Bandung</p>
""", unsafe_allow_html=True)

# Tombol navigasi penunjuk arah peta lokasi di HP pengantin
st.markdown("<a href='https://google.com' target='_blank'><button style='background-color:#8C6239; color:white; border:none; padding:8px 15px; border-radius:5px; width:100%; cursor:pointer; font-weight:bold;'>🗺️ Buka Rute Google Maps (Klik di HP)</button></a>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# ==============================================================================
# 4. FORM KONFIRMASI KEHADIRAN & UCAPAN (RSVP)
# ==============================================================================
st.markdown("<div class='wedding-box'>", unsafe_allow_html=True)
st.markdown("### 💌 Konfirmasi Kehadiran & Doa", unsafe_allow_html=True)

# Inisialisasi memori database komentar sementara menggunakan Session State
if "database_ucapan" not in st.session_state:
    st.session_state.database_ucapan = [
        {"nama": "Andi Wijaya", "status": "Hadir", "pesan": "Selamat ya Budi & Citra! Semoga samawa selamanya! 🔥"},
        {"nama": "Dewi Sartika", "status": "Tidak Hadir", "pesan": "Happy wedding! Maaf belum bisa hadir karena dinas luar kota, titip doa terbaik yaaa 🥺❤️"}
    ]

# Form input untuk tamu undangan yang membuka lewat HP mereka
with st.form("form_rsvp", clear_on_submit=True):
    nama_tamu = st.text_input("Nama Lengkap Anda:")
    status_hadir = st.radio("Apakah Anda akan hadir?", ["Hadir", "Masih Ragu", "Tidak Hadir"])
    pesan_doa = st.text_area("Tulis Doa & Ucapan Indah:")
    
    tombol_kirim = st.form_submit_button("Kirim Ucapan Ke Mempelai ✨")
    
    if tombol_kirim:
        if nama_tamu and pesan_doa:
            # Menyimpan ucapan baru ke dalam memori database sistem web
            st.session_state.database_ucapan.insert(0, {"nama": nama_tamu, "status": status_hadir, "pesan": pesan_doa})
            st.success("Terima kasih! Ucapan indahmu sudah tersimpan dan berhasil terkirim ke mempelai. 🥰")
            st.rerun()
        else:
            st.warning("Mohon isi nama dan ucapan doanya terlebih dahulu ya.")

st.write("---")
st.markdown("#### 💬 Gulungan Ucapan Tamu:")

# Menampilkan semua daftar ucapan doa yang masuk secara berurutan ke bawah
for data in st.session_state.database_ucapan:
    ikon_hadir = "✅" if data["status"] == "Hadir" else "❌" if data["status"] == "Tidak Hadir" else "⏳"
    st.markdown(f"**{data['nama']}** ({ikon_hadir} {data['status']})")
    st.markdown(f"<p style='font-style:italic; font-size:14px; background-color:#F5EBE0; padding:10px; border-radius:5px;'>\"{data['pesan']}\"</p>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
