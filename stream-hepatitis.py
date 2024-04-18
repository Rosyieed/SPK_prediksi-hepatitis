import pickle
import streamlit as st

# membaca model
hepatitis_model = pickle.load(open('hepatitis_model.sav', 'rb'))

#judul aplikasi
st.title('Aplikasi Prediksi Hepatitis')
st.write('')

st.header('Masukkan Gejala Anda:')
st.write('Note: 0 = Tidak, 1 = Ya')
st.write('')

col1,col2,col3,col4 = st.columns(4)


with col1:
    itching = st.selectbox('Apakah Anda Merasakan Gatal-gatal?', [0, 1])
with col2:
    joint_pain = st.selectbox('Apakah Anda Merasakan Nyeri Sendi?', [0, 1])
with col3:
    vomiting = st.selectbox('Apakah Anda Merasakan Mual?', [0, 1])
with col4:
    fatigue = st.selectbox('Apakah Anda Merasakan Lelah?', [0, 1])
    
with col1:
    lethargy = st.selectbox('Apakah Anda Merasakan Lethargy?', [0, 1])
with col2:
    high_fever = st.selectbox('Apakah Anda Merasakan Demam Tinggi?', [0, 1])
with col3:
    yellowish_skin = st.selectbox('Apakah Anda Merasakan Kulit Kuning?', [0, 1])
with col4:
    dark_urine = st.selectbox('Apakah Anda Merasakan Urine Gelap?', [0, 1])
    
with col1:
    loss_of_appetite = st.selectbox('Apakah Anda Merasakan Hilangnya Nafsu Makan?', [0, 1])
    
with col2:
    abdominal_pain = st.selectbox('Apakah Anda Merasakan Nyeri Perut?', [0, 1])
with col3:
    yellow_urine = st.selectbox('Apakah Anda Merasakan Urine Kuning?', [0, 1])
with col4:
    yellowing_of_eyes = st.selectbox('Apakah Anda Merasakan Mata Kuning?', [0, 1])


with col1:
    acute_liver_failure = st.selectbox('Apakah Anda Merasakan Gagal Ginjal?', [0, 1])
with col2:
    malaise = st.selectbox('Apakah Anda Merasakan Malaise?', [0, 1])
with col3:
    family_history = st.selectbox('Apakah Ada Riwayat Keluarga?', [0, 1])
with col4:
    receiving_blood_transfusion = st.selectbox('Apakah Anda Pernah Transfusi Darah?', [0, 1])

with col1:
    receiving_unsterile_injections = st.selectbox('Apakah Anda Pernah Suntik Steril?', [0, 1])
with col2:
    coma = st.selectbox('Apakah Anda Pernah Merasakan Koma?', [0, 1])
with col3:
    stomach_bleeding = st.selectbox('Apakah Anda Pernah Pendarahan Lambung?', [0, 1])

#menampilkan hasil prediksinya
if st.button('Prediksi'):
    # #menyiapkan data untuk diprediksi
    data = [[itching, joint_pain, vomiting, fatigue, lethargy, high_fever, yellowish_skin, dark_urine, loss_of_appetite, abdominal_pain,
    yellow_urine, yellowing_of_eyes, acute_liver_failure, malaise, family_history, receiving_blood_transfusion, receiving_unsterile_injections,
    coma, stomach_bleeding]]
    
    if sum(data[0]) >= 5:
        pred = hepatitis_model.predict(data)
        
        #menampilkan hasil prediksi
        if pred[0] == 'hepatitis A':
            st.success('Anda Terkena Hepatitis A')
        elif pred[0] == 'Hepatitis B':
            st.success('Anda Terkena Hepatitis B')
        elif pred[0] == 'Hepatitis C':
            st.success('Anda Terkena Hepatitis C')
        elif pred[0] == 'Hepatitis D':
            st.success('Anda Terkena Hepatitis D')
        elif pred[0] == 'Hepatitis E':
            st.success('Anda Terkena Hepatitis E')
    else:
        st.warning('Silakan pilih minimal lebih dari 5 gejala.')

