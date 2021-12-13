from sklearn.metrics import recall_score, confusion_matrix

y_true = [0, 1, 2, 0, 1, 2]
y_pred = [0, 2, 1, 0, 0, 1]

print(confusion_matrix(y_true, y_pred))
#라벨 별 각 평균
print(recall_score(y_true, y_pred, average=None))
#전체평균
print(recall_score(y_true, y_pred, average='micro'))
#라벨 별 각 합의 평균
print(recall_score(y_true, y_pred, average='macro'))