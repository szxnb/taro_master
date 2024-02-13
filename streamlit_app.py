import streamlit as st
from pathlib import Path
from PIL import Image  # pip install pillow

# --- PATH SETTINGS ---
THIS_DIR = Path(__file__).parent if "__file__" in locals() else Path.cwd()
ASSETS_DIR = THIS_DIR / "assets"
STYLES_DIR = THIS_DIR / "styles"
CSS_FILE = STYLES_DIR / "main.css"

# --- GENERAL SETTINGS ---
PAYPAL_CHECKOUT = "http://localhost:3000"
CONTACT_EMAIL = "3500466989@qq.com"

def load_css_file(css_file_path):
    with open(css_file_path) as f:
        return st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css_file(CSS_FILE)



st.title("🧙 Tarot Card Reading")


st.subheader("STEP1:")
st.text_input('请输入想占卜的问题', '请输入想占卜的问题')

st.subheader("STEP2:")
st.subheader("现在，请全神贯注回想你的问题，并且点击抽卡")
st.button("抽三张卡")

features_card = {
    "Feature_1.png": [
        "牌1的名字",
        "这个牌的简短介绍这个牌的简短介绍这个牌的简短介绍这个牌的简短介绍",
    ],
    "Feature_2.png": [
        "牌2的名字",
        "这个牌的简短介绍这个牌的简短介绍这个牌的简短介绍这个牌的简短介绍",
    ],
    "Feature_3.png": [
        "牌3的名字",
        "这个牌的简短介绍这个牌的简短介绍这个牌的简短介绍这个牌的简短介绍",
    ],
}

st.subheader("展示抽到了哪三张卡，卡1含义、卡2含义、卡3含义")

for image ,description in features_card.items():
    image = Image.open(ASSETS_DIR / image)
    st.write("")
    col_1, col_2, col_3 = st.columns(3)
    col_1.image(image, use_column_width=True)
    col_2.write(f"**{description[0]}**")
    col_3.write(description[1])
    

# --- BUY BTN ---
st.markdown(
    f'<a href={PAYPAL_CHECKOUT} class="button">👉 View Divination Report</a>',
    unsafe_allow_html=True,
)

    
# --- User reviews ---
st.write("")
st.write("---")
st.subheader(":rocket: User reviews")
features = {
    "Feature_1.png": [
        "Run Python Files From Excel",
        "After locating your Python interpreter, you can execute Python files directly from Excel. In the Pro Version, you can also add several Python interpreter paths. This is helpful when you need to execute your Python code from different virtual environments.",
    ],
    "Feature_2.png": [
        "Create Pandas Dataframes",
        "Generate Python files with a click of a button. Select the cell range you want to transform, and the add-in creates the Python code to read in the Excel data as a pandas dataframe.Instead of messing around with all of the available options in the pandas ‘read_excel’ method, the add-in does it for you.",
    ],
    "Feature_3.png": [
        "Create Jupyter Notebooks",
        "Have you ever wanted to do some quick analysis of your Excel data in a Jupyter Notebook? MyToolBelt can convert an Excel cell range into a Jupyter Notebook. Just select the cell range, and the add-in will create a new Jupyter Notebook in the workbook’s directory. Inside the Jupyter Notebook, you will find your ready-to-use dataframe based on your selection. This feature is a real time saver!",
    ],
}
for image, description in features.items():
    image = Image.open(ASSETS_DIR / image)
    st.write("")
    left_col, right_col = st.columns(2)
    left_col.image(image, use_column_width=True)
    right_col.write(f"**{description[0]}**")
    right_col.write(description[1])


# --- FAQ ---
st.write("")
st.write("---")
st.subheader(":raising_hand: FAQ")
faq = {
    "Question 1": "Some text goes here to answer question 1",
    "Question 2": "Some text goes here to answer question 2",
    "Question 3": "Some text goes here to answer question 3",
}
for question, answer in faq.items():
    with st.expander(question):
        st.write(answer)

# --- CONTACT FORM ---
st.write("")
st.subheader(":mailbox: Have A Question? Ask Away!")
contact_form = f"""
<form action="https://formsubmit.co/{CONTACT_EMAIL}" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here"></textarea>
     <button type="submit" class="button">Send ✉</button>
</form>
"""
st.markdown(contact_form, unsafe_allow_html=True)
