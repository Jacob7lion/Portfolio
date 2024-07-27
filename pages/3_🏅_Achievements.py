import streamlit as st
from streamlit_option_menu import option_menu


#create horizontal bar
selected= option_menu(
    menu_title=None,
    options=['Участия','Проекты'],
    icons=None,
    menu_icon=None,
    default_index=0,
    orientation='horizontal',
)
if selected== 'Участия':

    # first columns about achievements
    col1, col2 = st.columns(2, gap='small',
                            vertical_alignment='center')  # create 2 columns ( photo and my name with surname)
    with col1:
        st.title(' Участие в конференциях ', anchor=False)
        st.write(
        '''
         - Взятие 1-го места в V Всероссийской молодежной научной конференции "Мавлютовские чтения" 2021
        - Взятие 3-го места в конкурсе Паяльник 2021
        - Участие в  XIV Международной Научной-Практической Конференции "Пилотируемые полеты в космос"
        - Участие в XXIII Международной Научно-Технической Конференции ПТиТТ-2021
        - Был слушателем на конференциях "Разумные от народа" и "Волжский диджитал-тур"
        '''
        )
        st.image('./assets/participant3.jpg', width=200)
        st.image('./assets/conf4.jpg', width=300)
    with col2:
        st.image('./assets/1place.jpg', width=300)
        st.image('./assets/participant.jpg', width=300)
        st.image('./assets/conf2.jpg', width=300)
        st.image('./assets/participant2.jpg', width=300)
     #  st.image('./assets/participant3.jpg', width=200)
     #  st.image('./assets/conf4.jpg', width=300)

        # space between text and images
    #st.write('--')
    st.write('\n')
    st.html("<p>"
            "<span style='text-decoration: underline #2de2e6;text-underline-offset: 12px;text-decoration-thickness: 10px; font-size: 50%;font-weight: bold; color:#fbf9f9;'"
            "> fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff<"
            "/span</p>")
    st.write('\n')
    #st.subheader('', divider='violet')
# second columns about achievements

    col1, col2 = st.columns(2, gap='small',
                            vertical_alignment='center')  # create 2 columns ( photo and my name with surname)
    with col1:
        st.title('Участие в программе "УМНИК" ', anchor=False)
        st.write(
            'При кчастии в программе "УМНИК" команда моего студенческого клуба выйграла два гранта по проектам "Разработка ПАК по автоматизации складской логистики" и "Разработка прототипа для восстановления частично утраченного физического контроля"'  # you can write smth about you here more
        )
    with col2:
        st.image('./assets/grant.jpg', width=300)
        st.image('./assets/grant2.jpg', width=700)

if selected== 'Проекты':

    st.markdown("[First project **'Portfolio'**](https://myportfolio1.streamlit.app/)")

# html
#     def change_label_style(label, font_size='24px', font_color='#f6019d', font_family='sans-serif'):
#         html = f"""
#         <script>
#             var elems = window.parent.document.querySelectorAll('p');
#             var elem = Array.from(elems).find(x => x.innerText == '{label}');
#             elem.style.fontSize = '{font_size}';
#             elem.style.color = '{font_color}';
#             elem.style.fontFamily = '{font_family}';
#         </script>
#         """
#         st.components.v1.html(html)
#     label = "My text here"
#     st.text_input(label)
#     change_label_style(label, '24px')

