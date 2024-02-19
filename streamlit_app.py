import streamlit as st
from pathlib import Path
from PIL import Image  # pip install pillow
import random
import re

# --- PATH SETTINGS ---
THIS_DIR = Path(__file__).parent if "__file__" in locals() else Path.cwd()
ASSETS_DIR = THIS_DIR / "assets"
ASSETS_CARDS_DIR = THIS_DIR / "assets/cards"
ASSETS_DIR = THIS_DIR / "assets"
STYLES_DIR = THIS_DIR / "styles"
CSS_FILE = STYLES_DIR / "main.css"

# --- Card info ---
features_card = {
    "Fool": [
        "Card_1_Fool.png",
        "The Fool Tarot Card Description",
        "The Fool depicts a youth walking joyfully into the world. He is taking his first steps, and he is exuberant, joyful, excited. He carries nothing with him except a small sack, caring nothing for the possible dangers that lie in his path. Indeed, he is soon to encounter the first of these possible dangers, for if he takes just a step more, he he topple over the cliff that he is reaching. But this doesn't seem to concern him - we are unsure whether he is just naive or simply unaware. The dog at his heels barks at him in warning, and if he does not become more aware of his surroundings soon, he may never see all the adventures that he dreams of encountering.",
    ],
    "Magician": [
        "Card_2_Magician.png",
        "The Magician Tarot Card Description",
        "The Magician is one tarot card that is filled with symbolism. The central figure depicts someone with one hand pointed to the sky, while the other hand points to the ground, as if to say 'as above, so below'. This is a rather complicated phrase, but its summarization is that earth reflects heaven, the outer world reflects within, the microcosm reflects the macrocosm, earth reflects God. It can also be interpreted here that the magician symbolizes the ability to act as a go-between between the world above and the contemporary, human world. ",
    ],
    "Priestess": [
        "Card_3_Priestess.png",
        "The Priestess Tarot Card Description",
        "You've most likely encountered the High Priestess before, but in other forms - she can be seen in the archetypes of Persephone, Artemis, Isis and many more. When you encounter her, you will see her sitting on a cubic stone between the two pillars at Solomon’s Temple, Jachin, and Boaz. Jachin (right) is generally referred to as the Pillar of Establishment and Boaz (left) is the Pillar of Strength. The pillars also depict the duality of nature; masculine and feminine, good and evil, negative and positive.",
    ],
    "Empress": [
        "Card_4_Empress.png",
        "The Empress Tarot Card Description",
        "The Empress depicts a woman sitting on a throne. From the abundant nature that surrounds her, we can assume that this woman represents the Earth Mother archetype, a goddess of fertility. Her world is ruled by venus which means that there is complete love, harmony, fertility and luxury by the grace of this goddess. The woman herself has blonde hair crowned with stars, signaling her divine connection with the mystical realm. She is dressed in a pomegranate-patterned robe that represents fertility, and she is seated on cushions embroidered with a venus sign. She is surrounded by an enchanting green forest with a river streaming through it. The Empress brings abundance and blessings in the readings of those she meets.",
    ],
    "Emperor": [
        "Card_5_Emperor.png",
        "The Emperor Tarot Card Description",
        "In the Emperor tarot card, a stoic ruler figure can be seen on his throne, which is adorned with the heads of four rams, representing his astrological sign - Aries. In one hand, he carries a scepter, representing his reign and his right to rule, and in the other an orb, a symbol of the kingdom that he watches over. The long beard of the emperor represents his vast experience; over time he has learned much about what it takes to rule, to establish power, authority and complete order for the benefit of his people.",
    ],
    "Hierophant": [
        "Card_6_Hierophant.png",
        "The Hierophant Tarot Card Description",
        "The card depicts a religious figure that sits in a rather formal environment characteristic for a church. He is wearing three elaborate vestments which are designated to represent the three different worlds. His right hand is properly raised in an act of benediction, a sign of blessing – it’s the same hand that the Magician has raised. In his other hand, he carries a triple cross, which is associated traditionally with the pope. Each of the horizontal bars in the cross are thought to represent the Father, the Son and the Holy Ghost. Beneath him, two acolytes are seated, representing the transfer of sacred knowledge within institutions. Through these acolytes, the card also comes to represent following the path to knowledge and education."
    ],
    "Lovers": [
        "Card_7_Lovers.png",
        "The Lovers Tarot Card Description",
        "In the Lovers card, the man and the woman in the image are being protected and blessed by an angel above. The couple seems secure and happy in their home, which appears to be the Garden of Eden. The fruit tree with the snake behind the woman is a reference to that story, which tells of humanity's fall into temptation and into the realm of flesh and sensuality. The angel depicted here is Raphael, the angel of air - who is of the same element of the zodiac sign that governs this card: Gemini. Air is associated with mental activity, and communication in particular, which is the foundation for healthy relationships. His blessing seems to give this card a sense of balance and harmony, the symbolization of union in a grand and cosmic sense between two opposing forces. "
    ],
    "Chariot": [
        "Card_8_Chariot.png",
        "The Chariot Tarot Card Description",
        "The Chariot tarot card depicts a figure sitting inside a vehicle that is being driven by two black and white sphinxes. The whole card has a bit of a celestial influence; the figure sits underneath a blue canopy adorned by white stars. On his shoulders, he carries the sign of the crescent moon, representing the spiritual influence under which he is guided. On his head sits a crown, meaning that he is enlightened, and that his will is pure. Emblazoned on his chest is a square, denoting the element of earth, of the material world, which grounds him and his actions.",
    ],
    "Strength": [
        "Card_9_Strength.png",
        "Strength Tarot Card Description",
        "In this tarot card, you will see a woman who calmly holds the jaws of a fully grown lion. Despite the fact that the lion looks menacing and strong, the woman seems to have dominion over it. What is captivating is how gracefully she controls the lion. She is calm and collected, which is representative for being in control and disciplined especially in times of great adversities.The fact that she is also holding the jaws of a lion also shows that she has courage. Her control of the lion without being too rough shows love and compassion. The blue background over the mountains shows stability and the kind of calmness that comes with being stable. ",
    ],
    "Hermit": [
        "Card_10_Hermit.png",
        "The Hermit Tarot Card Description",
        "The Hermit depicts an old man standing alone at the peak of the mountain while holding a lantern in one of his hands and a staff on the other. The mountain denotes accomplishment, development, and success. The hermit tarot card refers to the level of spiritual knowledge that he attained, and that he is ready to impart that knowledge to everyone. There is also a deep commitment he has to his goal and a solid awareness of the path that he is taking. Inside the lantern, you will notice a star with 6 points which is also known as the Seal of Solomon. This symbol represents wisdom. The staff that he holds depicts authority and power.",
    ],
    "WheelofFortune": [
        "Card_11_WheelofFortune.png",
        "The Wheel of Fortune Tarot Card Description",
        "The Wheel of Fortune is one of the most highly symbolic cards in the deck, filled with signs that each have its own meaning. At the center of the card, lies a giant wheel, covered in esoteric symbols. There are different creatures that surround the wheel; the angel, the eagle, the bull and the lion. They are related to four fixed signs in the zodiac - leo, taurus, scorpio and aquarius. These four animals are also representatives for the four evangelists in Christian traditions, which is perhaps the reason that they are all adorned with wings.",
    ],
    "Justice": [
        "Card_12_Justice.png",
        "The Justice Tarot Card Description",
        "The Justice tarot card is a symbol of truth, fairness, and law. As she sits in her chair, the scales in her left hand represent how intuition should balance logic. She symbolizes impartiality with the double-edged sword in her right hand. The clarity in thought which is required to dispense justice are symbolized by the square on the crown she wears. Behind her, there is a purple cloak and standing grey pillars. Beneath her red cloak, which is held together by a clasp, she shows the tip of a white shoe. This is a spiritual reminder that what she delivers are the outcomes of their actions.",
    ],
    "HangedMan": [
        "Card_13_HangedMan.png",
        "The Hanged Man Tarot Card Description",
        "In this card, it depicts a man who is suspended upside-down, and he is hanging by his foot from the living world tree. This tree is rooted deep down in the underworld, and it is known to support the heavens. It is believed that the hanging man is actually positioned there by his own free will. We believe this because of the serene expression which is on his face. His right foot is bound to the branches, but his left foot remains perfectly free. At the same time, he is holding his hands behind his back in a way which forms an inverted triangle. His wearing of red pants are a representation of the physical body and human’s passion, while the blue that he wears in his shirt are representative of calm emotions, a color combination that is commonly seen in saints. His intellect is symbolized by the yellow color of his shoes, hair and halo. ",
    ],
    "Death": [
        "Card_14_Death.png",
        "Death Tarot Card Description",
        "Here, we see Death riding a beautiful white horse while holding up a black flag with a white pattern. It is portrayed as a living skeleton, the bones being the only part of the human body existing after death. He wears armor, which gives him his invincibility - signaling that no one can destroy Death. The white horse that he rides stands for purity, as Death purifies everyone. Beneath him, all classes of humans lie in the dirt - a king, and a pauper, meant to remind us that death does not differentiate between class, race, gender. ",
    ],
    "Temperance": [
        "Card_15_Temperance.png",
        "Temperance Tarot Card Description",
        "On the Temperance card, there is an angel with wings, whose gender is not immediately obvious, which suggests that there is a balance between the sexes. One foot of the angel is in water, to represent the subconscious, while the other foot is on dry land, a representation of the material world. On her robe, there is a square, which has a triangle inscribed inside, another echo of the tangible earth in union with the holy trinity. She holds two cups in a manner where she can mix the waters, which represent the super and subconscious minds. The water flows between them, suggesting union and infinity.",
    ],
    "Devil": [
        "Card_16_Devil.png",
        "The Devil Tarot Card Description",
        "This card shows the Devil represented in his most well-known satyr form, otherwise known as Baphomet. Along with being half goat and half man, the devil has bat wings and an inverted pentagram on his forehead. He is standing on a pedestal, to which are chained a nude man and woman, as if to show that he has dominion over them.Both the man and the woman have horns, as if to show that the more time they spend with the Devil, the less human they become. The chains make it appear as though the devil has taken them captive. The man has a flame on his tail while a woman has a bowl of grapes on her tail, which symbolizes their addiction to power and finer things in life, respectively. ",
    ],
    "Tower": [
        "Card_17_Tower.png",
        "The Tower Tarot Card Description",
        "The Tower card depicts a high spire nestled on top of the mountain. A lightning bolt strikes the tower which sets it ablaze. Flames are bursting in the windows and people are jumping out of the windows as an act of desperation. They perhaps signal the same figures we see chained in the Devil card earlier. They want to escape the turmoil and destruction within. The Tower is a symbol for the ambition that is constructed on faulty premises. The destruction of the tower must happen in order to clear out the old ways and welcome something new. Its revelations can come in a flash of truth or inspiration. ",
    ],
    "Star": [
        "Card_18_Star.png",
        "The Star Tarot Card Description",
        "The Star card shows a woman kneeling at the edge of a small pond. She is holding two containers of water. One container pours the water out to the dry land, as if to to nourish it and ensure its fertility. The lush green land around her seems to say that it is working. One foot is inside the water which shows the spiritual abilities and inner strength of the woman. The other foot on the ground shows her practical abilities and strengths. Behind her, there is a large central star surrounded by seven small stars which represent the chakras. There is bird standing at a tree branch which represents the holy ibis of thought. The Star's astrological correspondent is Aquarius.",
    ],
    "Moon": [
        "Card_19_Moon.png",
        "The Moon Tarot Card Description",
        "When we encounter the Moon, we see a path that leads off into the distance. On either side of the path stand a wolf and a dog, representing our animalistic nature - one is civilized, and the other wild and feral. There is a crawfish that is crawling out of the pond from which the path stems from. In the distance, we can see two towers flanking the central path, once again alluding to the doubles visible in this card. Everything in this card seems to echo the other, as if to allude to two possibilities. When we walk down the path, we walk the fine line between conscious and unconscious, between the tamed side of civilization of the dog, and the forces of nature represented by the wolf. ",
    ],
    "Sun": [
        "Card_20_Sun.png",
        "The Sun Tarot Card Description",
        "The Sun card presents an feeling of optimism and fulfillment. This card represents the dawn which follows the darkest of nights. The Sun is the source of all the life on our planet, and it represents life energy itself. There is a child depicted in the card, playing joyfully in the foreground. A symbol of our innocence, it represents the happiness that occurs when you are in alignment with your true self. The child is naked, meaning that he has absolutely nothing to hide. The card also depicts the childhood innocence and absolute purity. This is particularly emphasized through the white horse upon which the child is riding. The horse here is also a symbol of strength and nobility.",
    ],
    "Judgement": [
        "Card_21_Judgement.png",
        "Judgement Tarot Card Description",
        "This card depicts what one would imagine the last judgment would be, in the various forms that takes in many mythologies. The image in the Judgement card shows women, men, and children who are rising from the grave to respond to Gabriel’s trumpet call. Their outstretched arms symbolize that they are ready to be judged by the universe. They are about to meet their creator, their actions weighed, and find out where they will spend the remainder of eternity: in heaven or in hell. The massive tidal wave in the background signify that judgement is unavoidable, and that this judgement will be final.",
    ],
    "World": [
        "Card_22_World.png",
        "The World Tarot Card Description",
        "The World card in the tarot deck has a dancing figure at the center. The dancing figure on the card has one leg crossed over the other and holds a wand in either hand. She symbolizes balance and evolution in movement. The fulfillment and unity that she represents is not one that is static, but ever-changing, dynamic and eternal.The green wreath of flowers that surrounds the central figure is a symbol of success, while the red ribbons that wrap around it are reminiscent of infinity. There are four figures on each corner of the card - and they are the same ones that are in the Wheel of Fortune. The four figures represent Scorpio, Leo, Aquarius and Taurus - representative of the four corners of the universe, the four elements, and the four evangelicals. Together, they symbolize the harmony between all of their energies.",
    ],
}

# --- GENERAL SETTINGS ---
PAYPAL_CHECKOUT = "http://34.214.168.14:3000"
CONTACT_EMAIL = "3500466989@qq.com"


def load_css_file(css_file_path):
    with open(css_file_path) as f:
        return st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css_file(CSS_FILE)

#### 页面布局  ####

banner_image = Image.open(ASSETS_DIR / 'bannerimage7.png')
st.image(banner_image, use_column_width = True)

st.title("🧙 Tarot Card Reading")

user_question = st.text_input('Please enter the question you want to divine (eg: Will my love go smoothly in the next month?)', '')

def get_unique_elements(d, count):
        keys = list(d.keys())
        random.shuffle(keys)
        return keys[:count]

def draw_card():
        if user_question == '':
            st.warning("Please enter your question first")
        else:
            pre_user_question = user_question
            #一共有22张卡牌，不重复地抽3张卡
            unique_elements = get_unique_elements(features_card, 3)
            st.subheader("The 3 cards you drew:")

            # 给卡牌赋一下值，方便下一步传参
            user_card1 = unique_elements[0]
            user_card2 = unique_elements[1]
            user_card3 = unique_elements[2]

            # 展示卡牌
            col1, col2, col3 = st.columns(3)
            with col1:
                image1 = Image.open(ASSETS_CARDS_DIR / features_card[user_card1][0])
                st.image(image1 ,caption='Card1: '+ user_card1)

            with col2:
                image2 = Image.open(ASSETS_CARDS_DIR / features_card[user_card2][0])
                st.image(image2 ,caption='Card2: '+ user_card2)

            with col3:
                image3 = Image.open(ASSETS_CARDS_DIR / features_card[user_card3][0])
                st.image(image3 ,caption='Card3: '+ user_card3)

            # 展示卡牌
            # for card_name, card_info in features_card.items():
            #     for element in unique_elements:
            #         if element == card_name:
            #             image = Image.open(ASSETS_CARDS_DIR / card_info[0])
            #             col_1, col_2 = st.columns(2)
            #             col_1.image(image, use_column_width=True)
            #             col_2.subheader(card_info[1])
            #             col_2.write(card_info[2])

            # 传参并且显示购买按钮
            show_buy_btn(user_card1, user_card2, user_card3)


def show_buy_btn(user_card1, user_card2, user_card3):
    st.markdown(
        f'''
            <a href="{PAYPAL_CHECKOUT}?question={user_question}&card1={user_card1}&card2={user_card2}&card3={user_card3}" class="button">👉 View Divination Report</a>
        ''',
        unsafe_allow_html=True,
    )

if st.button("Click to draw 3 card"):
   draw_card()

# --- User reviews ---
# st.write("")
# st.write("---")
# st.write(f"\n")


# st.subheader(":rocket: User reviews")
# features = {
#     "Feature_1.png": [
#         "Run Python Files From Excel",
#         "After locating your Python interpreter, you can execute Python files directly from Excel. In the Pro Version, you can also add several Python interpreter paths. This is helpful when you need to execute your Python code from different virtual environments.",
#     ],
#     "Feature_2.png": [
#         "Create Pandas Dataframes",
#         "Generate Python files with a click of a button. Select the cell range you want to transform, and the add-in creates the Python code to read in the Excel data as a pandas dataframe.Instead of messing around with all of the available options in the pandas ‘read_excel’ method, the add-in does it for you.",
#     ],
#     "Feature_3.png": [
#         "Create Jupyter Notebooks",
#         "Have you ever wanted to do some quick analysis of your Excel data in a Jupyter Notebook? MyToolBelt can convert an Excel cell range into a Jupyter Notebook. Just select the cell range, and the add-in will create a new Jupyter Notebook in the workbook’s directory. Inside the Jupyter Notebook, you will find your ready-to-use dataframe based on your selection. This feature is a real time saver!",
#     ],
# }
# for image, description in features.items():
#     image = Image.open(ASSETS_DIR / image)
#     st.write("")
#     left_col, right_col = st.columns(2)
#     left_col.image(image, use_column_width=True)
#     right_col.write(f"**{description[0]}**")
#     right_col.write(description[1])


# --- FAQ ---
st.write("---")
st.subheader(":raising_hand: FAQ")
faq = {
    "Payment failed": "Please refresh this page and reinitiate payment or contact our email",
    "Didn’t receive report email in email": "Please make sure you have paid for your order and provided your correct email address. Or you can check the trash in the email. The email may be converted to spam and blocked.",
    "Don't know how to ask a question": "You can only ask one question at a time. Please describe your problem within 50 words.",
}
for question, answer in faq.items():
    with st.expander(question):
        st.write(answer)

# --- CONTACT FORM ---
st.write("---")
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


#### 页面布局  ####
