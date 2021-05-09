# ML-BASED PUBG 'SUPER RULE' PREDICTION PROJECT  

This project aims to predict the final winner of PUBG Series.  
It was created based on 'Super Rule'.  
Users can use this Machine Learning Model to compare the overall power of PUBG team.  
('WWCD Rule' Games are also possible)  
This Machine Learning Model can also be used for Pick'em Challange's Top 4 prediction event.  
  
이 프로젝트는 PUBG 시리즈의 최종 승자를 예측하는 것을 목표로 합니다.  
'Super Rule'을 기반으로 제작되었습니다.  
본 머신러닝 모델로 여러 팀의 전반적인 전력을 비교할 수 있습니다.  
('WWCD 규칙' 경기에도 사용 가능합니다)  
본 머신러닝 모델은 Pick'em Challange의 Top4 예측 이벤트에 사용할 수 있습니다.  
  
# Required Environment  
- Python 3.6.13
- Tensorflow 2.0.0
- Keras 2.3.1
  
# Data  
'The average of Place Points' and 'The average of Kill Points' by team before the final battle were used as training data. 
  
최종 경기 전까지의 팀별 Place Point 평균과 Kill Point 평균을 훈련 데이터로 사용했습니다.  
  
Type (순위 데이터 형태)   
|TEAM INFO|X1|X2|Y|
|---|---|---|---|
|TEAM NAME|MEAN VALUE OF PLACE POINTS|MEAN VALUE OF KILL POINTS|RANK|
|팀명|평균 PLACE POINT|평균 KILL POINT|순위|
  
Example Rank Data (순위 데이터 예시)    
|TEAM|MEAN VALUE OF PLACE POINTS|MEAN VALUE OF KILL POINTS|RANK|
|---|---|---|---|
|GEN|3.1|4.5|1|
|META|2.7|4.6|2|
|IFTY|2|5|3|
|DA|2.8|4.1|4|
  
For more information about data, refer to 'Sheet' & 'Train_Data' folders.  
  
데이터에 대한 자세한 내용은 'Sheet' 및 'Train_Data' 폴더를 참조하십시오.  
  
# Model Design  
- Sequential Model
- Activation function : sigmoid, relu, softmax

### PGIS_Prediction_Model_W5.h5
This model aimed to predict the winner of the PGI.S Weekly Final Week6.  
It was created based on the results until PGI.S Week5.  
Rank Decision, Bottom 16, Weekly Final data used('Super Rule' games Only).  
272 Rank Data used.  
30,000 epochs completed.  
  
이 모델은 Weekly Final 6주 차의 최종 승자를 예측하는 것을 목표로 합니다.  
PGI.S 5주 차까지의 경기 데이터를 기반으로 제작되었습니다.  
Rank Decision, Bottom 16, Weekly Final 경기 데이터가 사용되었습니다(Super Rule 게임만).  
272개의 순위 데이터가 사용되었습니다.  
30,000번 학습되었습니다.  
  
### PGIS_ESL_Prediction_Model.h5
Extended model of PGIS_prediction_Model_W5.h5  
It was created based on the results of PGI.S, ESL PUBG Masters: Americas Phase 1 and ESL PUBG Masters 2021 Europe Spring(Super Rule Games Only).  
336 Rank Data used.  
40,000 epochs completed.  
  
PGIS_prediction_Model_W5.h5의 확장 모델입니다.  
PGI.S, ESL PUBG Masters: Americas Phase 1, ESL PUBG Masters 2021 Europe Spring 경기 결과가 사용되었습니다(Super Rule 게임만).  
336개의 순위 데이터가 사용되었습니다.  
40,000번 학습되었습니다.  
  
# Results  
  
PGI.S Week5  
|RANK|PREDICTION|RESULT|
|---|---|---|
|1|META|GEN|
|2|VP|META|
|3|GEN|IFTY|
|4|SQ|DA|
  
PGI.S Week6  
|RANK|PREDICTION|RESULT|
|---|---|---|
|1|STK|SQ|
|2|SQ|ZEN|
|3|FAZE|MCG|
|4|IFTY|4AM|
  
# Demo (Google Colab) 
