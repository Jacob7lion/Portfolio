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
        st.title('Участие в программе "УМНИК" ', anchor=False)
        st.write(
            'При студенческом клубе выйграли две наши заявки по проектам "Разработка ПАК по автоматизации складскоой логистики" и "афф"'  # you can write smth about you here more
        )
    with col2:
        st.image('./assets/grant.jpg', width=300)
        st.image('./assets/grant2.jpg', width=700)



# space between text and images
    st.write('\10')


# second columns about achievements
    col1, col2 = st.columns(2, gap='small',
                            vertical_alignment='center')  # create 2 columns ( photo and my name with surname)
    with col1:
        st.title('Участие в гранте ', anchor=False)
        st.write(
            'При студенческом клубе выйграли две наши заявки по проектам'  # you can write smth about you here more
        )
    with col2:
        st.image('./assets/conf2.jpg', width=300)
        st.image('./assets/conf4.jpg', width=300)




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

