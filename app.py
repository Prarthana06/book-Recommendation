import streamlit as st 
import numpy as np 
import pandas as pd 
import pickle 
# st.write
# Write arguments to the app.
st.set_page_config(layout="wide")
# st.markdown(f'''
# <style>
#     section[data-testid="stSidebar"].css-ng1tp40{{width:30px;}}
# </style>

# ''',unsafe_allow_html=True)
book_list=pickle.load(open('book_image.pkl','rb'))



book=pd.DataFrame(book_list)
# print(book)



# st.write("Hello")
# st.header("hello ")
st.title("Book Recommendation ")
st.subheader('Most popular books ')
# book_list=pickle.load(open('book_name_list.pkl','wb'))
# book=pdd.DataFrame(book_list)
# option= st.selectbox('select book ',book['bookTitle'].values)
with st.container():
    # st.write("This is inside the container")

    # You can call any Streamlit command, including custom components:
    col1, col2, col3,col4,col5,col6,col7,col8= st.columns(8)

    with col1:
        st.caption(book.at[0,'bookTitle'])
        st.image(book.at[0,'imageUrlM'])
    with col2:
        st.caption(book.at[1,'bookTitle'])
        st.image(book.at[1,'imageUrlM'])
    with col3:
        st.caption(book.at[2,'bookTitle'])
        st.image(book.at[2,'imageUrlM'])
    with col4:
        st.caption(book.at[3,'bookTitle'])
        st.image(book.at[3,'imageUrlM'])
    with col5:
        st.caption(book.at[4,'bookTitle'])
        st.image(book.at[4,'imageUrlM'])
    with col6:
        st.caption(book.at[5,'bookTitle'])
        st.image(book.at[5,'imageUrlM'])
    with col7:
        st.caption(book.at[6,'bookTitle'])
        st.image(book.at[6,'imageUrlM'])
    with col8:
        st.caption(book.at[7,'bookTitle'])
        st.image(book.at[7,'imageUrlM'])
   

with st.container():
    # st.write("This is inside the container")

    # You can call any Streamlit command, including custom components:
    col1, col2, col3,col4,col5,col6,col7,col8= st.columns(8)
    with col1:
        st.caption(book.at[8,'bookTitle'])
        st.image(book.at[8,'imageUrlM'])
    with col2:
        st.caption(book.at[9,'bookTitle'])
        st.image(book.at[9,'imageUrlM'])

    with col3:
        st.caption(book.at[10,'bookTitle'])
        st.image(book.at[10,'imageUrlM'])
    with col4:
        st.caption(book.at[11,'bookTitle'])
        st.image(book.at[11,'imageUrlM'])
    with col5:
        st.caption(book.at[12,'bookTitle'])
        st.image(book.at[12,'imageUrlM'])
    with col6:
        st.caption(book.at[13,'bookTitle'])
        st.image(book.at[13,'imageUrlM'])
    with col7:
        st.caption(book.at[14,'bookTitle'])
        st.image(book.at[14,'imageUrlM'])
    with col8:
        st.caption(book.at[15,'bookTitle'])
        st.image(book.at[15,'imageUrlM'])
   
with st.container():
    # st.write("This is inside the container")

    # You can call any Streamlit command, including custom components:
    col1, col2, col3,col4,col5,col6,col7,col8= st.columns(8)
    with col1:
        st.caption(book.at[16,'bookTitle'])
        st.image(book.at[16,'imageUrlM'])
    with col2:
        st.caption(book.at[17,'bookTitle'])
        st.image(book.at[17,'imageUrlM'])
    with col3:
        st.caption(book.at[18,'bookTitle'])
        st.image(book.at[18,'imageUrlM'])
    with col4:
        st.caption(book.at[19,'bookTitle'])
        st.image(book.at[19,'imageUrlM'])
    with col5:
        st.caption(book.at[20,'bookTitle'])
        st.image(book.at[20,'imageUrlM'])
    with col6:
        st.caption(book.at[21,'bookTitle'])
        st.image(book.at[21,'imageUrlM'])
    with col7:
        st.caption(book.at[22,'bookTitle'])
        st.image(book.at[22,'imageUrlM'])
    with col8:
        st.caption(book.at[23,'bookTitle'])
        st.image(book.at[23,'imageUrlM'])
   


with st.container():
    # st.write("This is inside the container")

    # You can call any Streamlit command, including custom components:
    col1, col2, col3,col4,col5,col6,col7,col8= st.columns(8)
    with col1:
        st.caption(book.at[24,'bookTitle'])
        st.image(book.at[24,'imageUrlM'])
    with col2:
        st.caption(book.at[25,'bookTitle'])
        st.image(book.at[25,'imageUrlM'])
    with col3:
        st.caption(book.at[26,'bookTitle'])
        st.image(book.at[26,'imageUrlM'])
    with col4:
        st.caption(book.at[27,'bookTitle'])
        st.image(book.at[27,'imageUrlM'])
    with col5:
        st.caption(book.at[28,'bookTitle'])
        st.image(book.at[28,'imageUrlM'])
    with col6:
        st.caption(book.at[29,'bookTitle'])
        st.image(book.at[29,'imageUrlM'])
    with col7:
        st.caption(book.at[30,'bookTitle'])
        st.image(book.at[30,'imageUrlM'])
    with col8:
        st.caption(book.at[31,'bookTitle'])
        st.image(book.at[31,'imageUrlM'])
    
with st.container():
    # st.write("This is inside the container")

    # You can call any Streamlit command, including custom components:
    col1, col2, col3,col4,col5,col6,col7,col8= st.columns(8)



    with col1:
        st.caption(book.at[32,'bookTitle'])
        st.image(book.at[32,'imageUrlM'])
    with col2:
        st.caption(book.at[33,'bookTitle'])
        st.image(book.at[33,'imageUrlM'])
    with col3:
        st.caption(book.at[34,'bookTitle'])
        st.image(book.at[34,'imageUrlM'])
    with col4:
        st.caption(book.at[35,'bookTitle'])
        st.image(book.at[35,'imageUrlM'])
    with col5:
        st.caption(book.at[36,'bookTitle'])
        st.image(book.at[36,'imageUrlM'])
    with col6:
        st.caption(book.at[37,'bookTitle'])
        st.image(book.at[37,'imageUrlM'])
    with col7:
        st.caption(book.at[38,'bookTitle'])
        st.image(book.at[38,'imageUrlM'])
    with col8:
        st.caption(book.at[39,'bookTitle'])
        st.image(book.at[39,'imageUrlM'])

    # st.write("This is inside the container")

    # You can call any Streamlit command, including custom components:
   
# # st.write(my_data_frame)
# # st.write(my_mpl_figure)
# name = st.text_input("bookname")
# c = st.container()
# st.write("This will show last")
# c.write("This will show first")
# c.write("This will show second")

# col1, col2 = st.columns(2)
# col1.write("this is column 1")
# col2.write("this is column 2")
