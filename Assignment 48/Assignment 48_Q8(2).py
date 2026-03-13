from sklearn.metrics import confusion_matrix

actual_value = [1,1,1,1,0,0,0,0]
predicted_value = [1,1,0,1,0,1,0,0]

Confusion_Mat = confusion_matrix(actual_value,predicted_value)

TN,FP,FN,TP = Confusion_Mat.ravel()

print("True Positive: ",TP)
print("True Negative: ",TN)
print("False Positive: ",FP)
print("False Negative: ",FN)
