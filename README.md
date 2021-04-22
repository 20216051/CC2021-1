# CC2021-1
Azure Machine learning studio에서 Iris 데이터셋을 학습하고 테스트한 결과입니다


<br/><br/><br/>
실험
데이터셋의 클래스가 3개이므로 Multiclass logistic regression을 사용하였습니다
<br/><br/><br/>
![모델링](https://user-images.githubusercontent.com/83013439/115728318-61cf7900-a3bf-11eb-938d-9c25fd8e1857.PNG)
<br/><br/><br/>

<br/><br/><br/>
데이터셋 (출처 : https://archive.ics.uci.edu/ml/datasets/iris)
<br/><br/><br/>
![데이터셋](https://user-images.githubusercontent.com/83013439/115728386-70b62b80-a3bf-11eb-8a94-8a8c1074029f.PNG)
<br/><br/><br/>

<br/><br/><br/>
결과
전체적인 정확도는 92%
정확도의 평균은 94.66%
개별 precision의 평균은 92%
전체 precision의 평균은 90.96%
개별 recall 92%
전체 recall 90.43% 입니다.
<br/><br/><br/>
recall은 실제 TRUE인것중에 TRUE라고 예측한것의 비율, precision은 TRUE로 예측한것중에 실제 TRUE인것과 TRUE가 아닌것 중에서 실제 TRUE인것의 비율입니다
<br/><br/><br/>
![recall precision](https://user-images.githubusercontent.com/83013439/115731474-24201f80-a3c2-11eb-85ee-af14117882ba.png)
<br/><br/><br/>
![결과1](https://user-images.githubusercontent.com/83013439/115727686-cd651680-a3be-11eb-9a54-0b47bea96b8d.PNG)
<br/><br/><br/>
setosa를 setosa라고 예측한것은 32개 versicolor라고 예측한것은 0개, virginica라고 예측한것은 0개, 평균 손실율은 0.378899, precision, recall 둘다 1 입니다
versicolor를 setosa라고 예측한것은 0개, versicolor라고 예측한것은 16개, virginica라고 예측한것 4개, 평균 손실율은 0.648152, precision은 88.88%, recall은 80%입니다
virginica를 setosa라고 예측한것은 0개, versicolor라고 예측한것은 2개, virginica라고 예측한것은 21개, 평균 손실율은 0.592734, precision은 84%, recall은 91.3%입니다
<br/><br/><br/>
![결과2](https://user-images.githubusercontent.com/83013439/115727737-d950d880-a3be-11eb-875b-899d46098422.PNG)
<br/><br/><br/>
