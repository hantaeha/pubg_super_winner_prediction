import streamlit as st
import numpy as np
import pandas as pd
from tensorflow import keras
from sklearn.preprocessing import StandardScaler

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)

st.title("AI-Powered PUBG Winner Prediction")
st.subheader("& Top4 Prediction for Pick'em Challange (Super Rule Only)")

st.markdown("""---""")

st.subheader("MATCHES")
total_rounds = st.number_input("MATCHES PLAYED SO FAR (Before the Pick'em Challange ends)",1)
scaler = StandardScaler()

def average_cal(kill, total):
    place = total-kill
    average_kill = float(kill/total_rounds)
    average_place = float(place/total_rounds)
    return average_kill, average_place

st.markdown("""---""")

st.subheader("TEAM01")
team01 = st.text_input("TEAM01 : NAME")
team01_killpt = st.number_input("TEAM01 : Total Kill Points")
team01_totalpt = st.number_input("TEAM01 : Total Points")
team01_killpt_avearage, team01_placept_average = average_cal(team01_killpt, team01_totalpt)

st.write(' ',team01, "- KILL POINTS AVERAGE : ", team01_killpt_avearage, "PLACE POINTS AVERAGE : ", team01_placept_average)

st.markdown("""---""")

st.subheader("TEAM02")
team02 = st.text_input("TEAM02 : NAME")
team02_killpt = st.number_input("TEAM02 : Total Kill Points")
team02_totalpt = st.number_input("TEAM02 : Total Points")
team02_killpt_avearage, team02_placept_average = average_cal(team02_killpt, team02_totalpt)

st.write(' ',team02, "- KILL POINTS AVERAGE : ", team02_killpt_avearage, "PLACE POINTS AVERAGE : ", team02_placept_average)

st.markdown("""---""")

st.subheader("TEAM03")
team03 = st.text_input("TEAM03 : NAME")
team03_killpt = st.number_input("TEAM03 : Total Kill Points")
team03_totalpt = st.number_input("TEAM03 : Total Points")
team03_killpt_avearage, team03_placept_average = average_cal(team03_killpt, team03_totalpt)

st.write(' ',team03, "- KILL POINTS AVERAGE : ", team03_killpt_avearage, "PLACE POINTS AVERAGE : ", team03_placept_average)

st.markdown("""---""")

st.subheader("TEAM04")
team04 = st.text_input("TEAM04 : NAME")
team04_killpt = st.number_input("TEAM04 : Total Kill Points")
team04_totalpt = st.number_input("TEAM04 : Total Points")
team04_killpt_avearage, team04_placept_average = average_cal(team04_killpt, team02_totalpt)

st.write(' ',team04, "- KILL POINTS AVERAGE : ", team04_killpt_avearage, "PLACE POINTS AVERAGE : ", team04_placept_average)

st.markdown("""---""")

st.subheader("TEAM05")
team05 = st.text_input("TEAM05 : NAME")
team05_killpt = st.number_input("TEAM05 : Total Kill Points")
team05_totalpt = st.number_input("TEAM05 : Total Points")
team05_killpt_avearage, team05_placept_average = average_cal(team05_killpt, team05_totalpt)

st.write(' ',team05, "- KILL POINTS AVERAGE : ", team05_killpt_avearage, "PLACE POINTS AVERAGE : ", team05_placept_average)

st.markdown("""---""")

st.subheader("TEAM06")
team06 = st.text_input("TEAM06 : NAME")
team06_killpt = st.number_input("TEAM06 : Total Kill Points")
team06_totalpt = st.number_input("TEAM06 : Total Points")
team06_killpt_avearage, team06_placept_average = average_cal(team06_killpt, team06_totalpt)

st.write(' ',team06, "- KILL POINTS AVERAGE : ", team06_killpt_avearage, "PLACE POINTS AVERAGE : ", team06_placept_average)

st.markdown("""---""")

st.subheader("TEAM07")
team07 = st.text_input("TEAM07 : NAME")
team07_killpt = st.number_input("TEAM07 : Total Kill Points")
team07_totalpt = st.number_input("TEAM07 : Total Points")
team07_killpt_avearage, team07_placept_average = average_cal(team07_killpt, team07_totalpt)

st.write(' ',team07, "- KILL POINTS AVERAGE : ", team07_killpt_avearage, "PLACE POINTS AVERAGE : ", team07_placept_average)

st.markdown("""---""")

st.subheader("TEAM08")
team08 = st.text_input("TEAM08 : NAME")
team08_killpt = st.number_input("TEAM08 : Total Kill Points")
team08_totalpt = st.number_input("TEAM08 : Total Points")
team08_killpt_avearage, team08_placept_average = average_cal(team08_killpt, team08_totalpt)

st.write(' ',team08, "- KILL POINTS AVERAGE : ", team08_killpt_avearage, "PLACE POINTS AVERAGE : ", team08_placept_average)

st.markdown("""---""")

st.subheader("TEAM09")
team09 = st.text_input("TEAM09 : NAME")
team09_killpt = st.number_input("TEAM09 : Total Kill Points")
team09_totalpt = st.number_input("TEAM09 : Total Points")
team09_killpt_avearage, team09_placept_average = average_cal(team09_killpt, team09_totalpt)

st.write(' ',team09, "- KILL POINTS AVERAGE : ", team09_killpt_avearage, "PLACE POINTS AVERAGE : ", team09_placept_average)

st.markdown("""---""")

st.subheader("TEAM10")
team10 = st.text_input("TEAM10 : NAME")
team10_killpt = st.number_input("TEAM10 : Total Kill Points")
team10_totalpt = st.number_input("TEAM10 : Total Points")
team10_killpt_avearage, team10_placept_average = average_cal(team10_killpt, team10_totalpt)

st.write(' ',team10, "- KILL POINTS AVERAGE : ", team10_killpt_avearage, "PLACE POINTS AVERAGE : ", team10_placept_average)

st.markdown("""---""")

st.subheader("TEAM11")
team11 = st.text_input("TEAM11 : NAME")
team11_killpt = st.number_input("TEAM11 : Total Kill Points")
team11_totalpt = st.number_input("TEAM11 : Total Points")
team11_killpt_avearage, team11_placept_average = average_cal(team11_killpt, team11_totalpt)

st.write(' ',team11, "- KILL POINTS AVERAGE : ", team11_killpt_avearage, "PLACE POINTS AVERAGE : ", team11_placept_average)

st.markdown("""---""")

st.subheader("TEAM12")
team12 = st.text_input("TEAM12 : NAME")
team12_killpt = st.number_input("TEAM12 : Total Kill Points")
team12_totalpt = st.number_input("TEAM12 : Total Points")
team12_killpt_avearage, team12_placept_average = average_cal(team12_killpt, team12_totalpt)

st.write(' ',team12, "- KILL POINTS AVERAGE : ", team12_killpt_avearage, "PLACE POINTS AVERAGE : ", team12_placept_average)

st.markdown("""---""")

st.subheader("TEAM13")
team13 = st.text_input("TEAM13 : NAME")
team13_killpt = st.number_input("TEAM13 : Total Kill Points")
team13_totalpt = st.number_input("TEAM13 : Total Points")
team13_killpt_avearage, team13_placept_average = average_cal(team13_killpt, team13_totalpt)

st.write(' ',team13, "- KILL POINTS AVERAGE : ", team13_killpt_avearage, "PLACE POINTS AVERAGE : ", team13_placept_average)

st.markdown("""---""")

st.subheader("TEAM14")
team14 = st.text_input("TEAM14 : NAME")
team14_killpt = st.number_input("TEAM14 : Total Kill Points")
team14_totalpt = st.number_input("TEAM14 : Total Points")
team14_killpt_avearage, team14_placept_average = average_cal(team14_killpt, team14_totalpt)

st.write(' ',team14, "- KILL POINTS AVERAGE : ", team14_killpt_avearage, "PLACE POINTS AVERAGE : ", team14_placept_average)

st.markdown("""---""")

st.subheader("TEAM15")
team15 = st.text_input("TEAM15 : NAME")
team15_killpt = st.number_input("TEAM15 : Total Kill Points")
team15_totalpt = st.number_input("TEAM15 : Total Points")
team15_killpt_avearage, team15_placept_average = average_cal(team15_killpt, team15_totalpt)

st.write(' ',team15, "- KILL POINTS AVERAGE : ", team15_killpt_avearage, "PLACE POINTS AVERAGE : ", team15_placept_average)

st.markdown("""---""")

st.subheader("TEAM16")
team16 = st.text_input("TEAM16 : NAME")
team16_killpt = st.number_input("TEAM16 : Total Kill Points")
team16_totalpt = st.number_input("TEAM16 : Total Points")
team16_killpt_avearage, team16_placept_average = average_cal(team16_killpt, team16_totalpt)

st.write(' ',team16, "- KILL POINTS AVERAGE : ", team16_killpt_avearage, "PLACE POINTS AVERAGE : ", team16_placept_average)

st.markdown("""---""")
st.title("MATCH HISTORY")

st.subheader("Current Average State")

def standardization(data):
    standardized_data = (data-np.mean(data,axis=0))/np.std(data, axis=0)
    return standardized_data

KILL_AVERAGE = [team01_killpt_avearage, team02_killpt_avearage, team03_killpt_avearage, team04_killpt_avearage,team05_killpt_avearage,team06_killpt_avearage,team07_killpt_avearage,team08_killpt_avearage,team09_killpt_avearage,team10_killpt_avearage,team11_killpt_avearage,team12_killpt_avearage,team13_killpt_avearage,team14_killpt_avearage,team15_killpt_avearage,team16_killpt_avearage]
PLACE_AVERAGE = [team01_placept_average,team02_placept_average,team03_placept_average,team04_placept_average,team05_placept_average,team06_placept_average,team07_placept_average,team08_placept_average,team09_placept_average,team10_placept_average,team11_placept_average,team12_placept_average,team13_placept_average,team14_placept_average,team15_placept_average,team16_placept_average]

KILL_STANDARDIZED = standardization(KILL_AVERAGE)
PLACE_STANDARDIZED = standardization(PLACE_AVERAGE)

df_show = pd.DataFrame({
                    'RANK':['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16'],
                    'TEAM':[team01, team02, team03, team04, team05, team06, team07, team08, team09, team10, team11, team12, team13, team14, team15, team16],
                    'KILL':[team01_killpt_avearage, team02_killpt_avearage, team03_killpt_avearage, team04_killpt_avearage,team05_killpt_avearage,team06_killpt_avearage,team07_killpt_avearage,team08_killpt_avearage,team09_killpt_avearage,team10_killpt_avearage,team11_killpt_avearage,team12_killpt_avearage,team13_killpt_avearage,team14_killpt_avearage,team15_killpt_avearage,team16_killpt_avearage],
                    'PLACE':[team01_placept_average,team02_placept_average,team03_placept_average,team04_placept_average,team05_placept_average,team06_placept_average,team07_placept_average,team08_placept_average,team09_placept_average,team10_placept_average,team11_placept_average,team12_placept_average,team13_placept_average,team14_placept_average,team15_placept_average,team16_placept_average]
                    })

df_show = df_show.set_index('RANK')
st.dataframe(df_show, 512, 512)

df = pd.DataFrame({
                    'RANK':['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16'],
                    'TEAM NAME':[team01, team02, team03, team04, team05, team06, team07, team08, team09, team10, team11, team12, team13, team14, team15, team16],
                    'KILL STANDARDIZED':KILL_STANDARDIZED,
                    'PLACE STANDARDIZED':PLACE_STANDARDIZED
                    })

df = df.set_index('RANK')

model = keras.models.load_model("model/prediction_model.h5")

def rank_prediction():
    dataset = df.values
    team = dataset[:,0]
    X_prediction = dataset[:,1:3]
    Y_Prediction = model.predict(X_prediction.astype(np.float32))
    result_all = []

    for i in range(16):
        team_result = []
        team_name = team[i]
        prediction = Y_Prediction[i]   
        team_result.append((16-float(np.argmax(prediction)+1))+float(np.max(prediction)))
        team_result.append(team_name)
        result_all.append(team_result) 

    result_all.sort(reverse=True)

    final_prediction_rank = []
    final_prediction_team_name = []
    for i in range(len(result_all)):
            final_prediction_rank.append(i+1)
            final_prediction_team_name.append(result_all[i][1])
    final_prediction = pd.DataFrame({"RANK":final_prediction_rank, "TEAM NAME":final_prediction_team_name})
    final_prediction = final_prediction.set_index('RANK')
    st.dataframe(final_prediction)

    return

st.markdown("""---""")
st.title("Who's the Winner?")

if st.button("PREDICT NOW!"):
    rank_prediction()
else:
    st.write("Put Points & Predict Winner")