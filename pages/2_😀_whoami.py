import pandas as pd
import streamlit as st
import plotly.express as px


# Create main info on page
st.title(':violet[Good to see you] 🎸')
st.subheader('There you can check info about me 😉')
col1,col2 =st.columns(2,gap='small', vertical_alignment='center') # create 2 columns ( photo and my name with surname)
with col1:
    st.image('./assets/photo1.jpg',width=200)
with col2:
    st.title('Ivanov Yakov', anchor=False)
    st.write(
        '' # you can write smth about you here more
    )

# write data about Experience
st.write('\n')
st.subheader(':orange[Experience]')
st.write(
 '''
 - Участие в конференциях
 - Летняя стажировка в отделе связи МВД
 - Создание студенческого клуба, где выйграли два гранта по 500 тыс. рублей на проект по БПЛА и Биоинженерии
 - Работа менеджером в музыкальном магазине  Muztorg, подработка репетитором по высшей математике
 - 3 года службы в вертолетной эскадрильи в качестве инженера РЭО  
 '''
)
#create divider between Experience and Hard skills with color (violet)
st.subheader('',divider='violet')

# write data about Hard skilss
st.write('\n')
st.subheader(':blue[Hard skills]')
st.write(
'''
- Опыт работы с ОС Astra Linux, Ubuntu Linux, Kali Linux
- Опыт работы с виртуализацией ОС с помощью Oracle VM VirtualBox
- Опыт работы с платформой Arduino
- Опыт работы с КОМПАС-3D
- Опыт работы с редактором видео VSDC
- Опыт работы с Visual Studio
- Опыт работы в 1С
- Умение пайки
'''
)

# Read excel and put data in value (df)
df=pd.read_excel(
    io='./assets/me.xlsx',
engine='openpyxl',
sheet_name='table',
skiprows=2,
    usecols='A:B',
nrows=8
)

#kill all values which has Null
df.dropna(inplace=True)

# Create donut with data from value (df)
pie=px.pie(df,title='Donut of progress',
           values='values',
           names='skills',
           color_discrete_sequence=['#c700b5','#ffd319','#ff901f']) # choose colors by HEX code
st.plotly_chart(pie)



