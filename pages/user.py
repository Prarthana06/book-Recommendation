
# from email.mime import image
# from pyrsistent import v
import streamlit as st 
import numpy as np 
import pandas as pd
import pickle
import sklearn as sk 
# from sklearn.neighbors import NearestNeighbors
from sklearn.neighbors import NearestNeighbors
st.set_page_config(layout="wide")
book_pivot=pickle.load(open('C:/Users/PRARTHANA/datascience/book_recommendation/book_pivot.pkl','rb'))
book_sparse=pickle.load(open('C:/Users/PRARTHANA/datascience/book_recommendation/book_sparse.pkl','rb'))

book_name_image=pickle.load(open('C:/Users/PRARTHANA/datascience/book_recommendation/book_name_image.pkl','rb'))
book_name_image=pd.DataFrame(book_name_image)

fr=pickle.load(open('C:/Users/PRARTHANA/datascience/book_recommendation/dict_allData.pkl','rb'))
fr=pd.DataFrame(fr)
model=NearestNeighbors(metric='cosine',algorithm='brute')
model.fit(book_sparse)

def recommend(book_name):
    book_id = np.where(book_pivot.index==book_name)[0][0]
    distances,suggestions=model.kneighbors(book_pivot.iloc[book_id,:].values.reshape(1,-1),n_neighbors = 8)  
                                        
    books=[]
  
    for i in range(len(suggestions)):
       

            books = book_pivot.index[suggestions[i]]
            
    return books 

def userBooks(id):
    df=pd.DataFrame(fr[fr['userId']==id])
    # df=fr[fr['userId']==id]
    df=df.head(7)
    # print(df)
    book_list=df['bookTitle']
    return book_list
 
st.title(' Book Recommendation  ')
st.subheader('User id specific Book Recommendation  ')
u_id=fr.userId.unique()

# b_name=book_name_image['bookTitle']
# select book name 
selectedUid = st.selectbox('select user id',u_id)
if st.button('go..'):
    book_names=userBooks(selectedUid)
    # st.text(len(book_names))
    global list
    list=['a']
    for i in  book_names:
        list1=recommend(i)
        for i in list1:
            if i not in list :
                list.append(i)
    st.subheader("lenght of total books ")
    st.subheader(len(list))

   
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
    #     with st.container():
    #             col1, col2, col3,col4,col5,col6,col7,col8= st.columns(8)
    #             with col1:
    #                 st.caption(list[25])
    #                 st.image(book_name_image[book_name_image['bookTitle']==list[25]]['imageUrlM'].values[0])
    #             with col2:
    #                 st.caption(list[26])
    #                 st.image(book_name_image[book_name_image['bookTitle']==list[26]]['imageUrlM'].values[0])
    #             with col3:
    #                 st.caption(list[27])
    #                 st.image(book_name_image[book_name_image['bookTitle']==list[27]]['imageUrlM'].values[0])
    #             with col4:
    #                 st.caption(list[28])
    #                 st.image(book_name_image[book_name_image['bookTitle']==list[28]]['imageUrlM'].values[0])
    #             with col5:
    #                 st.caption(list[29])
    #                 st.image(book_name_image[book_name_image['bookTitle']==list[29]]['imageUrlM'].values[0])
    #             with col6:
    #                 st.caption(list[30])
    #                 st.image(book_name_image[book_name_image['bookTitle']==list[30]]['imageUrlM'].values[0])
    #             with col7:
    #                 st.caption(list[31])
    #                 st.image(book_name_image[book_name_image['bookTitle']==list[31]]['imageUrlM'].values[0])
    #             with col8:
    #                 st.caption(list[32])
    #                 st.image(book_name_image[book_name_image['bookTitle']==list[32]]['imageUrlM'].values[0])

    #     with st.container():
    #             col1, col2, col3,col4,col5,col6,col7,col8= st.columns(8)
    #             with col1:
    #                 st.caption(list[33])
    #                 st.image(book_name_image[book_name_image['bookTitle']==list[33]]['imageUrlM'].values[0])
    #             with col2:
    #                 st.caption(list[34])
    #                 st.image(book_name_image[book_name_image['bookTitle']==list[34]]['imageUrlM'].values[0])
    #             with col3:
    #                 st.caption(list[35])
    #                 st.image(book_name_image[book_name_image['bookTitle']==list[35]]['imageUrlM'].values[0])
    #             with col4:
    #                 st.caption(list[35])
    #                 st.image(book_name_image[book_name_image['bookTitle']==list[35]]['imageUrlM'].values[0])
    #             with col5:
    #                 st.caption(list[37])
    #                 st.image(book_name_image[book_name_image['bookTitle']==list[37]]['imageUrlM'].values[0])
    #             with col6:
    #                 st.caption(list[38])
    #                 st.image(book_name_image[book_name_image['bookTitle']==list[38]]['imageUrlM'].values[0])
    #             with col7:
    #                 st.caption(list[39])
    #                 st.image(book_name_image[book_name_image['bookTitle']==list[39]]['imageUrlM'].values[0])
    #             with col8:
    #                 st.caption(list[40])
    #                 st.image(book_name_image[book_name_image['bookTitle']==list[40]]['imageUrlM'].values[0])






    # l_iter=iter(list)
    # while True :
    #     i=next(l_iter,"end")
    #     if(i=="end"):
    #         break
    #     else:
    #         st.caption(i)













    # with st.container():
    #     col1, col2, col3,col4,col5,col6,col7,col8,= st.columns(8)
    #     with col1:
    #         st.caption(list[9])
    #         st.image(book_name_image[book_name_image['bookTitle']==list[9]]['imageUrlM'].values[0])
    
    # for i in range(len(list)+1):
    #     col=['col1','col2','col3','col4','col5','col6','col7','col8']
    #     if(i%8):
    #          with st.container():
    #             col=['col1','col2','col3','col4','col5','col6','col7','col8']
    #             col1, col2, col3,col4,col5,col6,col7,col8= st.columns(8) 
    #             co=col[(i-1)%7]
    #             with co: 
    #                 st.caption(list[i])
    #                 st.image(book_name_image[book_name_image['bookTitle']==list[i+1]]['imageUrlM'].values[0])
    #     else:
    #         c1=col[(i-1)%7]
    #         with c1:
    #          st.caption(list[i])
    #          st.image(book_name_image[book_name_image['bookTitle']==list[i+1]]['imageUrlM'].values[0])

    # i=1
    # col=['col1','col2','col3','col4','col5','col6','col7','col8']
    # while i<=40:
    #     with st.container():
    #         col1, col2, col3,col4,col5,col6,col7,col8= st.columns(8)
    #         cola=col[(i-1)%7]
    #         with cola:
    #             st.caption(list[i])
    #             st.image(book_name_image[book_name_image['bookTitle']==list[i]]['imageUrlM'].values[0])
      

# mygrid = make_grid(5,8)
# i=1

# mygrid[0][0].image(book_name_image[book_name_image['bookTitle']==list[i]]['imageUrlM'].values[0])

# mygrid[1][1].write('11')
# mygrid[2][2].write('22')
# mygrid[3][3].write('33')
# mygrid[4][4].write('44')




    # if i==0:
        #     # print("The suggestions for ",book_name,"are : ")
        #     continue
        # if not i:
  # images=[]
# images = book_name_image[book_name_image['bookTitle']==books[i]]['imageUrlM'].values[0]
# def list_of_books(list_main):
#     total_books=['a']
#     for i in  list_main:
#         list1=recommend(i)
#         list=list.extend(list1)
#         for i in list1 :
#     return 