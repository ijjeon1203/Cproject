'''

방법 1
0,1 데이터를 가지고 학습하기 

총 8303765625 개의 데이터 필요 

방법 2 

1인 데이터 있으니 0인 데이터 만들어서 사용 

0인 데이터 만들기
랜덤함수로 파일 만들고 비교해서 찾기 

'''

cnt=0
fn = 0
name = 'total'
fname = name + str(fn)
f = open(fname + '.txt', mode='wt', encoding='utf-8')
for a in range(1,45) :
    for b in range(1,45) :
        for c in range(1,45):
            for d in range(1, 45):
                for e in range(1, 45):
                    for f1 in range(1, 45):
                        #list=[a,b,c,d,e,f1]
                        data = "%d %d %d %d %d %d\n" % (a,b,c,d,e,f1)
                        f.write(data)
                        #cnt=cnt+1
                        #if(cnt == 7000):
                        #    f.close()
f.close()



from random import *
import keras
import numpy as np
import pandas as pd

#import tensorflow as tf

data= pd.read_table("./lotto.txt")
#print(data.head())

train_data=data.to_numpy()
print(len(train_data))
test_data=np.random.randint(1,45,6)
print(test_data)
test_data=np.random.randint(1,45,6)
print(len(test_data))

# 모델 생성
model = keras.Sequential([keras.layers.Dense(units=1, input_shape=[6])])
model.compile(loss='mean_squared_error', optimizer='sgd')

# 모델학습
model.fit(train_data, train_data, epochs=100)

# 모델 검증
pred = model.predict(test_data)
print(pred)

"""

"""
# 입력
x = np.array(datalist).reshape(-1,1)
y = x * 2 + 1

# 모델 구성
X = tf.keras.layers.Input(shape=[6]) #피쳐의 개수 넣어줌
H = tf.keras.layers.Dense(10, activation='swish')(X)
y = tf.keras.layers.Dense(1)(H)
model = tf.keras.models.Model(X,y)
model.compile(loss='mse')

# epoch 세대, verbose 학습 진행 사항 표시 여부(0 표시 않함)
model.fit(feature,target,epochs=1000,verbose=0)

# 출력 결과 확인
model.predict(feature)
"""

