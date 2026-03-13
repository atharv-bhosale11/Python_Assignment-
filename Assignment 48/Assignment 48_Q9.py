from sklearn.metrics import classification_report

actual_value = [1,1,1,1,0,0,0,0]
predicted_value = [1,1,0,1,0,1,0,0]

Report = classification_report(actual_value,predicted_value)

print("Classification Report are: ")
print(Report)
