
from email.mime import image
import streamlit as st 
import numpy as np 
import pandas as pd
import pickle
import sklearn as sk 
from sklearn.neighbors import NearestNeighbors
st.set_page_config(layout="wide")
# load the files 


book_pivot=pickle.load(open('C:/Users/PRARTHANA/datascience/book_recommendation/book_pivot.pkl','rb'))
book_sparse=pickle.load(open('C:/Users/PRARTHANA/datascience/book_recommendation/book_sparse.pkl','rb'))


book_name_image=pickle.load(open('C:/Users/PRARTHANA/datascience/book_recommendation/book_name_image.pkl','rb'))
book_name_image=pd.DataFrame(book_name_image)


model=NearestNeighbors(metric='cosine',algorithm='brute')
model.fit(book_sparse)

def recommend(book_name):
    book_id = np.where(book_pivot.index==book_name)[0][0]
    distances,suggestions=model.kneighbors(book_pivot.iloc[book_id,:].values.reshape(1,-1),n_neighbors = 25)  
    
                                           
    books=[]
    # images=[]
    for i in range(len(suggestions)):
        # if i==0:
        #     # print("The suggestions for ",book_name,"are : ")
        #     continue
        # if not i:
            books = book_pivot.index[suggestions[i]]
            # images = book_name_image[book_name_image['bookTitle']==books[i]]['imageUrlM'].values[0]
    return books 
# list = recommend(option)

# title of page 
# st.title(' ')
st.title(' Book Recommendation  ')
st.subheader('search simmilar books ')

b_name=book_name_image['bookTitle']
# select book name 
selectedBName = st.selectbox('select book ', b_name)
if st.button('Recommand'):
    #  st.write(option)
    
    list=recommend(selectedBName)
    

    with st.container():
        col1, col2, col3,col4,col5,col6,col7,col8= st.columns(8)
        with col1:
            st.caption(list[1])
            st.image(book_name_image[book_name_image['bookTitle']==list[1]]['imageUrlM'].values[0])
        with col2:
            st.caption(list[2])
            st.image(book_name_image[book_name_image['bookTitle']==list[2]]['imageUrlM'].values[0])
        with col3:
            st.caption(list[3])
            st.image(book_name_image[book_name_image['bookTitle']==list[3]]['imageUrlM'].values[0])
        with col4:
            st.caption(list[4])
            st.image(book_name_image[book_name_image['bookTitle']==list[4]]['imageUrlM'].values[0])
        with col5:
            st.caption(list[5])
            st.image(book_name_image[book_name_image['bookTitle']==list[5]]['imageUrlM'].values[0])
        with col6:
            st.caption(list[6])
            st.image(book_name_image[book_name_image['bookTitle']==list[6]]['imageUrlM'].values[0])
        with col7:
            st.caption(list[7])
            st.image(book_name_image[book_name_image['bookTitle']==list[7]]['imageUrlM'].values[0])
        with col8:
            st.caption(list[8])
            st.image(book_name_image[book_name_image['bookTitle']==list[8]]['imageUrlM'].values[0])

    with st.container():
        col1, col2, col3,col4,col5,col6,col7,col8= st.columns(8)
        with col1:
            st.caption(list[9])
            st.image(book_name_image[book_name_image['bookTitle']==list[9]]['imageUrlM'].values[0])
        with col2:
            st.caption(list[10])
            st.image(book_name_image[book_name_image['bookTitle']==list[10]]['imageUrlM'].values[0])
        with col3:
            st.caption(list[11])
            st.image(book_name_image[book_name_image['bookTitle']==list[11]]['imageUrlM'].values[0])
        with col4:
            st.caption(list[12])
            st.image(book_name_image[book_name_image['bookTitle']==list[12]]['imageUrlM'].values[0])
        with col5:
            st.caption(list[13])
            st.image(book_name_image[book_name_image['bookTitle']==list[13]]['imageUrlM'].values[0])
        with col6:
            st.caption(list[14])
            st.image(book_name_image[book_name_image['bookTitle']==list[14]]['imageUrlM'].values[0])
        with col7:
            st.caption(list[15])
            st.image(book_name_image[book_name_image['bookTitle']==list[15]]['imageUrlM'].values[0])
        with col8:
            st.caption(list[16])
            st.image(book_name_image[book_name_image['bookTitle']==list[16]]['imageUrlM'].values[0])
    with st.container():
        col1, col2, col3,col4,col5,col6,col7,col8= st.columns(8)
        with col1:
            st.caption(list[17])
            st.image(book_name_image[book_name_image['bookTitle']==list[17]]['imageUrlM'].values[0])
        with col2:
            st.caption(list[18])
            st.image(book_name_image[book_name_image['bookTitle']==list[18]]['imageUrlM'].values[0])
        with col3:
            st.caption(list[19])
            st.image(book_name_image[book_name_image['bookTitle']==list[19]]['imageUrlM'].values[0])
        with col4:
            st.caption(list[20])
            st.image(book_name_image[book_name_image['bookTitle']==list[20]]['imageUrlM'].values[0])
        with col5:
            st.caption(list[21])
            st.image(book_name_image[book_name_image['bookTitle']==list[21]]['imageUrlM'].values[0])
        with col6:
            st.caption(list[22])
            st.image(book_name_image[book_name_image['bookTitle']==list[22]]['imageUrlM'].values[0])
        with col7:
            st.caption(list[23])
            st.image(book_name_image[book_name_image['bookTitle']==list[23]]['imageUrlM'].values[0])
        with col8:
            st.caption(list[24])
            st.image(book_name_image[book_name_image['bookTitle']==list[24]]['imageUrlM'].values[0])












#     for i in list :
#         # print(list)
#         st.write(i)
#         # st.image(image[i])

#     # for in in list:
#     #     s
     
# # else:
# #      st.write('Goodbye')








# # book=pd.DataFrame(book_name_image)
# final=book_name_image[book_name_image.bookTitle.isin(list)]
# # print(final)
# with st.container():

#     col1, col2, col3,col4,col5,col6,col7,col8,= st.columns(8)
#     # col1,col2=st.columns(2)
#     with col1:
#         st.caption(list[0])
#         st.image(final[final['bookTitle']==list[0]]['imageUrlM'].values[0])
#     with col2:
        
#        st.caption(list[1])
#        st.image(final[final['bookTitle']==list[1]]['imageUrlM'].values[0])
       
#     with col3:
#        st.caption(list[2])
#        st.image(final[final['bookTitle']==list[2]]['imageUrlM'].values[0])
      
#     with col4:
#        st.caption(list[3])
#        st.image(final[final['bookTitle']==list[3]]['imageUrlM'].values[0])
        
#     with col5:
#        st.caption(list[4])
#        st.image(final[final['bookTitle']==list[4]]['imageUrlM'].values[0])
     
#     with col6:
#        st.caption(list[5])
#        st.image(final[final['bookTitle']==list[5]]['imageUrlM'].values[0])
       
#     with col7:
#        st.caption(list[6])
#        st.image(final[final['bookTitle']==list[6]]['imageUrlM'].values[0])
       
#     with col8:
#        st.caption(list[7])
#        st.image(final[final['bookTitle']==list[7]]['imageUrlM'].values[0])
      

# with st.container():
#     st.write("This is inside the container")

#     # You can call any Streamlit command, including custom components:
#     col1, col2, col3,col4,col5,col6,col7,col8,= st.columns(8)
#     with col1:
#         st.caption(final.at[8,'bookTitle'])
#         st.image(final.at[8,'imageUrlM'])
#     with col2:
#         st.caption(final.at[9,'bookTitle'])
#         st.image(final.at[9,'imageUrlM'])
#     with col3:
#         st.caption(final.at[10,'bookTitle'])
#         st.image(final.at[10,'imageUrlM'])
#     with col4:
#         st.caption(final.at[11,'bookTitle'])
#         st.image(final.at[11,'imageUrlM'])
#     with col5:
#         st.caption(final.at[12,'bookTitle'])
#         st.image(final.at[12,'imageUrlM'])
#     with col6:
#         st.caption(final.at[13,'bookTitle'])
#         st.image(final.at[13,'imageUrlM'])
#     with col7:
#         st.caption(final.at[14,'bookTitle'])
#         st.image(final.at[14,'imageUrlM'])
#     with col8:
#         st.caption(final.at[15,'bookTitle'])
#         st.image(final.at[15,'imageUrlM'])









