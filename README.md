# AI-Powered PUBG Winner Prediction 

This project aims to predict the final top 4 teams of [PUBG](https://www.pubgesports.com/) e-sports game using the Machine learning technology.  
It was created based on [Super Rule](Introduction/super_v3_0_0.pdf).  
('WWCD Format' Games are also possible)  
You can use this Machine learning Model to compare the overall power of participating teams.  
This project can be used for Pick'em Challange's Top 4 Prediction event.  
  
이 프로젝트는 머신러닝 기술을 사용하여 PUBG 이스포츠의 최종 상위 4팀을 예측합니다.  
[Super Rule](Introduction/super_v3_0_0.pdf)을 기반으로 제작되었습니다.  
('WWCD 포맷' 경기에도 사용 가능합니다)  
본 머신러닝 모델로 참가 팀의 전반적인 전력을 비교할 수 있습니다.  
이 프로젝트는 Pick'em Challange의 Top 4 예측 이벤트에 사용될 수 있습니다.  
  
# Required Environment  
- Python 3.6.13
- Tensorflow 2.0.0
- Keras 2.3.1
  
# Data  
'Mean value of Place Points', 'Mean value of Kill Points' and 'Rank' by team were used as training data. 
  
팀별 'Place Point 평균', 'Kill Point 평균' 그리고 '순위'를 훈련 데이터로 사용했습니다.  
  
Type (형태)   
||X1|X2|Y|
|---|---|---|---|
|TEAM|MEAN VALUE OF PLACE POINTS|MEAN VALUE OF KILL POINTS|RANK|
|팀명|PLACE POINT 평균|KILL POINT 평균|순위|

  
Example (예시)    
|TEAM|MEAN VALUE OF PLACE POINTS|MEAN VALUE OF KILL POINTS|RANK|
|---|---|---|---|
|GEN|3.1|4.5|1|
|META|2.7|4.6|2|
|IFTY|2|5|3|
|DA|2.8|4.1|4|
  
For more information about data, refer to 'Sheet' & 'Train_Data' folders.  
  
데이터에 대한 자세한 내용은 'Sheet' 및 'Train_Data' 폴더를 참조하십시오.  
  
# Model Design  
- Two Pre-Trained Model
- Sequential Model
- Activation Functions : Sigmoid, ReLu, Softmax  
  
![image](model/model.png)  
  
### Model 1. PGIS_W5_Prediction_Model.h5
This model aimed to predict the winner of the PGI.S 2021 Weekly Final Week6.  
It was created based on the results until PGI.S Week5('Super Rule' games Only).  
272 data used.  
30,000 epochs completed.  
  
이 모델은 PGI.S 2021 Weekly Final 6주 차의 상위 4팀 예측을 목표로 합니다.  
PGI.S 5주 차까지의 경기 데이터를 기반으로 제작되었습니다(Super Rule 게임만).  
272개의 데이터가 사용되었습니다.  
30,000번 학습되었습니다.  
  
![image](Introduction/PGIS_W5_Prediction_Model.png)  
Model Download Link : [PGIS_W5_Prediction_Model Download](Model/PGIS_W5_Prediction_Model.h5)  
  
### Model 2. PGIS_ESL_Prediction_Model.h5
Extended model of 'PGIS_W5_Prediction_Model.h5'.  
It was created based on the results of PGI.S, ESL PUBG Masters: Americas Phase 1 and ESL PUBG Masters 2021 Europe Spring(Super Rule Games Only).  
336 data used.  
50,000 epochs completed.  
  
'PGIS_W5_Prediction_Model.h5'의 확장 모델입니다.  
PGI.S, ESL PUBG Masters: Americas Phase 1, ESL PUBG Masters 2021 Europe Spring 경기 결과가 사용되었습니다(Super Rule 게임만).  
336개의 데이터가 사용되었습니다.  
50,000번 학습되었습니다.  
  
![image](Introduction/PGIS_ESL_Prediction_Model.png)  
Model Download Link : [PGIS_ESL_Prediction_Model Download](Model/PGIS_ESL_Prediction_Model.h5)  
  
# Results  
  
### PGI.S 2021 Weekly 5 Final   
|RANK|PREDICTION|RESULT|
|---|---|---|
|1|***META***|***GEN***|
|2|VP|***META***|
|3|***GEN***|IFTY|
|4|SQ|DA|
  
Model : PGIS_W4_Prediction_Model.h5 
  
### PGI.S 2021 Week 6 Final    
|RANK|PREDICTION|RESULT|
|---|---|---|
|1|STK|***SQ***|
|2|***SQ***|ZEN|
|3|FAZE|MCG|
|4|IFTY|4AM|
  
Model : PGIS_W5_Prediction_Model.h5  
  
### PGC 2021 Week 1 Final    
|RANK|PREDICTION|RESULT|
|---|---|---|
|1|ENCE|KPI|
|2|GEN|GBL|
|3|***TL***|***OATH***|
|4|***OATH***|***TL***|
  
Model : PGIS_ESL_Prediction_Model.h5  
  
### PGC 2021 Week 2 Final  
|RANK|PREDICTION|RESULT|
|---|---|---|
|1|NH|***TL***|
|2|ENCE|GNL|
|3|***TL***|***VP***|
|4|***VP***|GEX|
  
Model : PGIS_ESL_Prediction_Model.h5    
  
### PGC 2021 Week 3 Final  
|RANK|PREDICTION|RESULT|
|---|---|---|
|1|***NH***|GEN|
|2|OATH|NAVI|
|3|TL|***NH***|
|4|GBL|GEX|
  
Model : PGIS_ESL_Prediction_Model.h5      

### PGC 2021 Grand Final 
|RANK|PREDICTION|RESULT|
|---|---|---|
|1|***NH***|***NH***|
|2|ENCE|HERO|
|3|TL|VP|
|4|GEN|TSM|
  
Model : PGIS_ESL_Prediction_Model.h5     
  
# Demo (Google Colab) 
  
You can predict the results using the Google Colab environment.  
  
Google Colab 환경에서 직접 예측하실 수 있습니다.  
  
Google Colab Link : [PUBG Super Rule Winner Prediction](https://colab.research.google.com/drive/17Y2pWz-iTXwxVTYHqD-5v8V3-reOOaIh?usp=sharing)  
Prediction Format Sheet : [Prediction Format Sheet](https://docs.google.com/spreadsheets/d/1BS1k9RSjcRc8ogW5Yf6vVraSqg4jPZPPmJN266yQXI8/edit?usp=sharing)  
  
PGC 2021 Logfile : [PGC 2021 Logs](https://docs.google.com/spreadsheets/d/1P-AcOAdprDz88VZLE3pAafsXZadtaPIR1kEyflPmATw/edit?usp=sharing)  
PGC 2021 Prediction Format : [PGC 2021 Prediction Format Sheet](https://docs.google.com/spreadsheets/d/1YD3XXJyhQj73Bj-hpjKQkfP-_pNZvLpzB9sYmnUnhYc/edit?usp=sharing)  
  
# Future Plan  
  
Creating Prediction Models by Maps (Miramar & Erangel)  
Creating Prediction Models optimized for the 'WWCD Format'  
Adding the data of PGC 2021 games to the New Prediction Model
   
맵별 예측 모델 생성 (미라마 & 에란겔)  
'WWCD 포맷'에 최적화된 예측 모델 생성  
PGC 2021 데이터를 추가한 새로운 모델 생성
