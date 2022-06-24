import pandas as pd

print("Hello world")

x = pd.read_excel(r"C:\Users\mathe\AutomatizarPlanilha\excel\PyEx.xlsx", engine='openpyxl')

print(x)