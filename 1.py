import pandas as pd
emp=pd.read_csv("C:/Users/leela/OneDrive/Desktop/QPDS/employees.csv")
print("distinct department id:")
print(emp.DEPARTMENT_ID.unique())

