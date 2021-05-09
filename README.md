# ML-BASED PUBG 'SUPER RULE' WINNER PREDICTION  

This project aims to predict the final winner of PUBG Series.  
It was created based on 'Super Rule'.  
('WWCD Rule' Games are also possible)  
Users can use this Machine Learning Model to compare the overall power of PUBG team.  
This Machine Learning Model can also be used for Pick'em Challange's Top 4 Prediction event.  
  
이 프로젝트는 PUBG 시리즈의 최종 승자를 예측하는 것을 목표로 합니다.  
'Super Rule'을 기반으로 제작되었습니다.  
('WWCD 규칙' 경기에도 사용 가능합니다)  
본 머신러닝 모델로 여러 팀의 전반적인 전력을 비교할 수 있습니다.  
이 모델은 Pick'em Challange의 Top4 예측 이벤트에도 사용될 수 있습니다.  
  
# Required Environment  
- Python 3.6.13
- Tensorflow 2.0.0
- Keras 2.3.1
  
# Data  
'The average of Place Points', 'The average of Kill Points' and 'Rank' by team were used as training data. 
  
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
- Two Sequential Model
- Activation functions : sigmoid, relu, softmax

### Model 1. PGIS_W5_Prediction_Model.h5
This model aimed to predict the winner of the PGI.S 2021 Weekly Final Week6.  
It was created based on the results until PGI.S Week5('Super Rule' games Only).  
272 data used.  
30,000 epochs completed.  
  
이 모델은 PGI.S 2021 Weekly Final 6주 차의 최종 승자를 예측하는 것을 목표로 합니다.  
PGI.S 5주 차까지의 경기 데이터를 기반으로 제작되었습니다(Super Rule 게임만).  
272개의 데이터가 사용되었습니다.  
30,000번 학습되었습니다.  
  
### Model 2. PGIS_ESL_Prediction_Model.h5
Extended model of 'PGIS_W5_Prediction_Model.h5'.  
It was created based on the results of PGI.S, ESL PUBG Masters: Americas Phase 1 and ESL PUBG Masters 2021 Europe Spring(Super Rule Games Only).  
336 data used.  
50,000 epochs completed.  
  
'PGIS_W5_Prediction_Model.h5'의 확장 모델입니다.  
PGI.S, ESL PUBG Masters: Americas Phase 1, ESL PUBG Masters 2021 Europe Spring 경기 결과가 사용되었습니다(Super Rule 게임만).  
336개의 데이터가 사용되었습니다.  
50,000번 학습되었습니다.  
  
# Results  
  
PGI.S 2021 Week5  
|RANK|PREDICTION|RESULT|
|---|---|---|
|1|META|GEN|
|2|VP|META|
|3|GEN|IFTY|
|4|SQ|DA|
  
PGI.S 2021 Week6  
|RANK|PREDICTION|RESULT|
|---|---|---|
|1|STK|SQ|
|2|SQ|ZEN|
|3|FAZE|MCG|
|4|IFTY|4AM|
  
# Demo (Google Colab) 
  
You can make direct predictions using the Google Colab environment.  
  
Google Colab을 사용하여 직접 예측하실 수 있습니다.  
  
Link : [PUBG Super Rule Winner Prediction (Google Colab)](https://colab.research.google.com/drive/17Y2pWz-iTXwxVTYHqD-5v8V3-reOOaIh?usp=sharing) 
