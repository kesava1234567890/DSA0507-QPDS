import pandas as pd
employees=pd.read_csv(r"C:/Users/leela/OneDrive/Desktop/QPDS/jobs.csv")
result=employees.groupby(["emp_id"])
print(result.filter(lambda x:len(x)>1).groupby("emp_id").size().sort_values(ascending=False))
