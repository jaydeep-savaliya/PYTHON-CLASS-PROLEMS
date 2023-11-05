import pandas as pd
with open('iris.data') as f:
    data = f.read()
# print(data)
newdata = []
for line in data:
    # print(line)
    newdata.append(line.split(","))
df = pd.DataFrame(newdata,columns=['c1','c2'])
df.to_csv("py.csv")
print(df)