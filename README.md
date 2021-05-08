# ML-BASED PUBG SUPER RULE PREDICTION PROJECT  

This project aims to predict the final winner of PUBG Series.  
Designed based on 'Super Rule', but the user can use this Machine Learning Model to compare the overall power of PUBG teams ('WWCD Rule' Games included).    
  
이 프로젝트는 PUBG 시리즈의 최종 승자를 예측하는 것을 목표로 합니다.
'Super Rule'을 기반으로 제작되었지만, 본 머신러닝 모델로 여러 팀의 전반적인 전력을 비교할 수 있습니다 ('WWCD 규칙' 경기 포함).  

# Required Environment  
- Python 3.6.13
- Tensorflow 2.0.0
- Keras 2.3.1
  
# Data Type  
The average Place Points and the average Kill Points by the team before the final match were used as train data.  

최종 경기 전까지의 팀별 평균 Place Points와 평균 Kill Points를 훈련 데이터로 사용했습니다.  
  
EXAMPLE
|TEAM|MEAN VALUE OF PLACE POINTS|MEAN VALUE OF KILL POINTS|RANK|
|---|---|---|---|
|GEN|3.1|4.5|1|
|META|2.7|4.6|2|
|IFTY|2|5|3|
|DA|2.8|4.1|4|
  
# Model Design  
- Sequential Model
- Activation function : sigmoid, relu, softmax
- For more information, refer to 'information.txt' in Introduction folder
