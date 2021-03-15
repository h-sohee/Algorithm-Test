from sklearn import svm, metrics
from sklearn.model_selection import train_test_split
import pandas as pd

tbl = pd.read_csv("engels.csv")

label = tbl["label"]
f = tbl["food"] / 800       # 최대 800
e = tbl["expenses"] / 3000  # 최대 3000
x = pd.concat([f, e], axis=1)

# 데이터 분리
data_train, data_test, label_train, label_test = train_test_split(x, label)

# 학습하기
clf = svm.SVC()
clf.fit(data_train, label_train)

# 예측하기
predict = clf.predict(data_test)

# 결과값 출력하기
ac_score = metrics.accuracy_score(label_test, predict)
cl_report = metrics.classification_report(label_test, predict)
print("정답률 =", ac_score)
print("리포트 =\n", cl_report)
