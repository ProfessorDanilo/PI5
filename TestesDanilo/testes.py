import pandas as pd
import matplotlib.pyplot as plt


i=0
f = open("salvando.csv", "a")
i=i+1
f.write('\n')
f.write(str(i))
f.write(',')
f.write('nome')
f.write(',')
f.write('categoria')
f.write(',')
f.write('console')
f.close()
df = pd.read_csv("salvando.csv")
print(df.head())