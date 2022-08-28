# AI-Powered PUBG Winner Prediction 

This project aims to predict the final top 4 teams of [PUBG](https://www.pubgesports.com/) e-sports game using Machine Learning Technology.  
It was created based on Super Rule.  
You can use this Machine learning Model to compare the overall power of participating teams.  
This project can be used for Pick'em Challange's Top 4 Prediction event.  
  
이 프로젝트는 머신러닝 기술을 사용하여 PUBG 이스포츠의 최종 상위 4팀을 예측합니다.  
Super Rule을 기반으로 제작되었습니다.   
본 머신러닝 모델로 참가 팀의 전반적인 전력을 비교할 수 있습니다.  
이 프로젝트는 Pick'em Challange의 Top 4 예측 이벤트에 사용될 수 있습니다.  
  
# Required Environment  
- Python 3.8.13
- Tensorflow 2.9.0 macos
- Keras 2.7.0
  
# Data  
'Mean value of Place Points & Standardization', 'Mean value of Kill Points & Standardization' and 'Rank' were used as training data. 
  
팀별 'Place Point 평균 & 표준화', 'Kill Point 평균 & 표준화' 그리고 '순위'를 훈련 데이터로 사용했습니다.  
  
Type (형태)   
||X1|X2|Y|
|---|---|---|---|
|TEAM|MEAN VALUE OF PLACE POINTS & STANDARDIZATION|MEAN VALUE OF KILL POINTS & STANDARDIZATION|RANK|
|팀명|PLACE POINT 평균 & 표준화|KILL POINT 평균 & 표준화|순위|

  
Example (예시)    
|TEAM|MEAN VALUE OF PLACE POINTS & STANDARDIZATION|MEAN VALUE OF KILL POINTS & STANDARDIZATION|RANK|
|---|---|---|---|
|NH|2.06|1.97|1|
|HERO|2.25|1.54|2|
|VP|0.32|1.33|3|
|TSM|0.13|0.79|4|
  
For more information about data, refer to 'data' folders.  
  
데이터에 대한 자세한 내용은 'data' 폴더를 참조하십시오.  
  
# Model Design    
![image](model/model.png)  
  
### Model Info 
Data : PGC2019, PGI.S2021, PGC2021 (Super Rule Game Olny)  
1,040 data used.  
1,000 epochs completed.  (Validation Accuracy : 50.64%)    
  
데이터 : PGC2019, PGI.S2021, PGC2021 (수퍼룰 게임만)    
1,040 개의 데이터가 사용되었습니다.  
1,000 번 학습되었습니다. (Validation Accuracy : 50.64%)  
  
![image](Introduction/acc.png)    
  
# Results  
  
### PGI.S 2021 Week 6 Final (Initial Prediction Model)   
|RANK|PREDICTION|RESULT|
|---|---|---|
|1|STK|***SQ***|
|2|***SQ***|ZEN|
|3|FAZE|MCG|
|4|IFTY|4AM|   
  
### PGC 2021 Grand Final (Initial Prediction Model) 
|RANK|PREDICTION|RESULT|
|---|---|---|
|1|***NH***|***NH***|
|2|ENCE|HERO|
|3|TL|VP|
|4|GEN|TSM|  
 
### 2022 PWS : Phase 2 Grand Final : Day 4 (Latest Prediction Model) 
|RANK|PREDICTION|RESULT|
|---|---|---|
|1|***KDF***|***KDF***|
|2|***DNW***|***DNW***|
|3|***DK***|***DK***|
|4|***GEN***|***GEN***|   
 
### PGC 2022 Grand Final (Latest Prediction Model) 
|RANK|PREDICTION|RESULT|
|---|---|---|
|1|TBD|TBD|
|2|TBD|TBD|
|3|TBD|TBD|
|4|TBD|TBD|  

# Demo (Web App) 
  
You can predict the results using the Web App environment.  
  
웹 환경에서 직접 예측하실 수 있습니다.  
  
Web App Link : [AI-Powered PUBG Winner Prediction](https://hantaeha-pubg-super-winner-prediction-pubg-prediction-78zxuz.streamlitapp.com/)  
  
# Future Plan  
  
Creating Prediction Models by Maps (Miramar & Erangel)  
   
맵별 예측 모델 생성 (미라마 & 에란겔)  
