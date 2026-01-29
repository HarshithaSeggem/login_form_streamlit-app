import streamlit as st

st.header("student records management")

st.title("welcome to the student management system")

st.subheader("manage student records efficiently")

st.markdown("-----------------------------------------------------")

st.text("this application allows you to perform the crud opreations")
st.write("hello")
st.write("123")
st.write({"name":"harshitha"})
st.write(['1','2'])
st.markdown("**bold**")
st.markdown("*italic*")
st.markdown("item 1/n item 2")
st.markdown("<h3 style='color:red'>RED-TEXT</h3>",unsafe_allow_html=True )
st.caption("this is caption for sms")
st.code("""
        def add(a,b):
        return a+b
        """,language="python")
st.latex(r'''
         a^2+b^2=c^2
         ''')
st.divider()
if st.button("click me"):
    st.write("button clicked")
    st.success("operation suusccesful")
    st.snow()
else:
    st.write("not clicked")
    st.error("error")
nme=st.text_input("enter your name")
if nme=="":
    st.warning("name cant be empty!")
elif not nme.isalpha():
    st.error("invalid input")
else:    
    st.success(f"HELLO,{nme}!")
feedback=st.text_area("enter the feedback:")
st.write(feedback)

if st.checkbox("i agree to the terms"):
  st.write("thankyou")
gender=st.radio("select your gender:",("male","female","other"))
st.write(f"you selected:{gender}")
country=st.selectbox("selected conntry:",("india","usa","uk"))
st.write(f"you selected:{country}")
skills = st.multiselect(
   "select skills",
   ["python","sql"]
)
st.write("Skills:",skills)
age = st.slider("select your age:",1,2,3)
st.write(f"you are {age} years old.")
uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
    st.success("File uploaded successfully!")
    st.write(f"Filename: {uploaded_file.name}")
with st.form("my_form"):
   name=st.text_input("name")
   age=st.number_input("age",0,100)
   submit=st.form_submit_button("submit")
if submit:
    st.write(name,age)
with st.form("myy_form"):
    uname=st.text_input("uname")
    password= st.text_input("pass",type="password")
    submit=st.form_submit_button("submit")
if submit:
    st.write(uname,password)


col1,col2,col3=st.columns(3)
with col1:
    st.header("column1")
    st.write("this is col1")
with col2:
    st.header("column2")
    st.write("this is col2")
with col3:
    st.header("column3")
    st.write("this is col3")
data = {

    'Name': ['Anurag', 'Sumit', 'Rohit'],

    'Age': [21, 22, 20],

    'Course': ['B.Tech', 'M.Tech', 'BBA']

}

st.table(data)
st.sidebar.title("Menu")

option = st.sidebar.selectbox(

"Choose page",

["Home", "About", "Contact"]

)

st.sidebar.write(f"You selected: {option}")

def load_data():
    return[1,2,3,4]
data=load_data()
st.write(data)
