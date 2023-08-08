 
while True : 
 with st.container():

            col1, col2, col3,col4,col5,col6,col7,col8= st.columns(8)
            with col1:
                i=next(l_iter,"end")
                if(i!="end"):

                    st.caption(list[1])
                    st.image(book_name_image[book_name_image['bookTitle']==list[1]]['imageUrlM'].values[0])
                
            with col2:
                i=next(l_iter,"end")
                if(i!="end"):
                        st.caption(list[2])
                        st.image(book_name_image[book_name_image['bookTitle']==list[2]]['imageUrlM'].values[0])
                else:
                    break 
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
            