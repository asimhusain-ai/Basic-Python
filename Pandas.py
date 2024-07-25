import pandas as pd
dict = {
        'Name':['Asim','Hina','Ashi','Yahiya','Zeeshan','Arbaz','Salik'],
        'Age':[19,18,00,22,21,20,23],
        'Address':['Sirpura','Pakwada','Space','Amroha','Sambhal','Dhampur','Rampur']
}
arr = pd.DataFrame(dict)
print(arr)