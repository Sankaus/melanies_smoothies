# Import python packages
import streamlit as st
#from snowflake.snowpark.context import get_active_session
from snowflake.snowpark.functions import col

# Write directly to the app
st.title('My parents new healthy dinner')
st.write(
    """Choose the fruits you want in your custom Smoothie!
    """
)

import streamlit as st
cnx = st.connection("snowflake")
session = cnx.session()
name_on_order = st.text_input('Name on Smoothie')
st.write('The name on your Smoothie will be', name_on_order)


#session = get_active_session()
my_dataframe = session.table("smoothies.public.fruit_options").select(col('FRUIT_NAME'))
#st.dataframe(data=my_dataframe, use_container_width=True)

ingredients_list= st.multiselect(
    'chose upto 5 ingrediants:'
    , my_dataframe
    , max_selections=5
    )

if ingredients_list:

 ingredients_string = ''

 for fruit_chosen in ingredients_list:
    ingredients_string += fruit_chosen + ' '
 st.write(ingredients_string)    


 my_insert_stmt = """ insert into smoothies.public.orders(ingredients,name_on_order)
            values ('""" + ingredients_string + """','""" +name_on_order+ """')"""

 #st.write(my_insert_stmt)

    
 time_to_insert = st.button('Submit Order')   

 if ingredients_string:
     session.sql(my_insert_stmt).collect()
        #New Section to display fruityvice nutrition information.
 import requests
 fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
 st.text(fruityvice_response.json())


     
 st.success('Your Smoothie is ordered, MellyMel!', icon="✅")




    
