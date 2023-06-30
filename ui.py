from fastapi.encoders import jsonable_encoder
import streamlit as st
import requests

fastapi_url = "http://localhost:8000"

st.set_page_config(page_title="Pizza Delivery Service", page_icon=":🍕:", layout="wide")

with st.container():
    st.write("SPECIAL OFFER FLAT 70%OFF ON ALL YOURS FAVOURITE PIZZA")


with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.write("Please signup here! if not a customer already")
        if st.button("Sign-up"):
            user = {
                "username": "saurabh",
                "email": "e@.com",
                "password": "password"
            }
            response = requests.post(url=f"{fastapi_url}/auth/signup", json=user)
            st.write(response)
            # if response.status_code == 201:
            #     st.success("User created successfully!")
            #     user_data = response.json()
            #     st.write("New user details:")
            #     st.write(f"Username: {user_data['username']}")
            #     st.write(f"Email: {user_data['email']}")
            #     # Display other user details if needed
            # elif response.status_code == 400:
            #     st.error("Error: User with the email or username already exists")
            # else:
            #     st.error("Error: Something went wrong")



    with right_column:
        st.write("Please login here! if you are a customer already")
        st.button("Login")
