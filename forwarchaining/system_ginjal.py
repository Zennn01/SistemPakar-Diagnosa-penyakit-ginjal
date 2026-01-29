import streamlit as st

# =========================
# KNOWLEDGE BASE
# =========================

# Daftar Penyakit
penyakit = {
    "PG1": "Infeksi Ginjal",
    "PG2": "Batu Ginjal",
    "PG3": "Gagal Ginjal Akut",
    "PG4": "Gagal Ginjal Kronis",
    "PG5": "Nefropati Diabetik",
    "PG6": "Sindrom Nefrotik"
}

# Daftar Gejala
gejala = {
    "G1": "Bau urine yang tidak seperti biasa",
    "G2": "Sakit pinggang atau punggung",
    "G3": "Demam",
    "G4": "Mual",
    "G5": "Lemas",
    "G6": "Nyeri pada saat buang air kecil",
    "G7": "Ada darah atau nanah dalam urine",
    "G8": "Sering buang air kecil",
    "G9": "Urine berwarna seperti teh",
    "G10": "Pembengkakan pada bagian kaki",
    "G11": "Jarang buang air kecil",
    "G12": "Sesak nafas",
    "G13": "Nafsu makan menurun",
    "G14": "Sakit di bagian perut",
    "G15": "Tremor pada tangan",
    "G16": "Pucat",
    "G17": "Gatal-gatal",
    "G18": "Kram otot",
    "G19": "Sulit tidur",
    "G20": "Urine berbusa",
    "G21": "Pembengkakan di sekitar mata",
    "G22": "Mual dan muntah",
    "G23": "Pembengkakan pada wajah",
    "G24": "Pembengkakan pada lengan",
    "G25": "Berkurangnya konsentrasi",
    "G26": "Diare",
    "G27": "Berat badan bertambah akibat penumpukan cairan"
}

# Rule (Forward Chaining) – sesuai tabel jurnal
rules = {
    "PG1": ["G1", "G2", "G3", "G4", "G5", "G6", "G7"],
    "PG2": ["G2", "G6", "G8", "G9"],
    "PG3": ["G2", "G3", "G5", "G10", "G11"],
    "PG4": ["G5", "G10", "G12", "G13", "G16", "G17", "G18", "G19"],
    "PG5": ["G4", "G5", "G13", "G20", "G21"],
    "PG6": ["G20", "G21", "G22", "G23", "G24", "G25", "G26", "G27"]
}

# =========================
# FORWARD CHAINING ENGINE
# =========================
def forward_chaining(selected_gejala):
    hasil = []

    for kode_penyakit, rule_gejala in rules.items():
        if set(rule_gejala).issubset(set(selected_gejala)):
            hasil.append(penyakit[kode_penyakit])

    return hasil

# =========================
# STREAMLIT UI
# =========================
# =========================
# STREAMLIT UI
# =========================
st.set_page_config(page_title="Sistem Pakar Ginjal", layout="wide")

st.title("🧠 Sistem Pakar Diagnosa Awal Penyakit Ginjal")
st.write("Metode Inferensi: **Forward Chaining**")
st.write("Silakan pilih gejala yang Anda rasakan:")

# Input gejala
selected_gejala = []

cols = st.columns(2)
i = 0
for kode, nama in gejala.items():
    label = f"{kode} - {nama}"   # ⬅️ tampilkan KODE G
    with cols[i % 2]:
        if st.checkbox(label):
            selected_gejala.append(kode)
    i += 1

st.markdown("---")

# Tombol diagnosa
if st.button("🔍 Diagnosa Penyakit"):
    if not selected_gejala:
        st.warning("Silakan pilih gejala terlebih dahulu.")
    else:
        hasil_diagnosa = forward_chaining(selected_gejala)

        # tampilkan gejala terpilih (biar demo makin jelas)
        st.info(f"Gejala yang dipilih: {', '.join(selected_gejala)}")

        if hasil_diagnosa:
            st.success("✅ Hasil Diagnosa:")
            for h in hasil_diagnosa:
                st.write(f"- **{h}**")
        else:
            st.error("❌ Penyakit tidak dapat ditentukan berdasarkan gejala yang dipilih.")

