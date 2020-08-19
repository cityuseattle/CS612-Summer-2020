# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import pandas as pd


# %%
df1 = pd.DataFrame({'employee': ['Gary', 'Stu', 'Mary', 'Sue'], 'group': ['Accounting', 'Marketing', 'Marketing', 'HR']})
df1


# %%
df2 = pd.DataFrame({'employee': ['Mary', 'Stu', 'Gary', 'Sue'], 'hire_date': [2008, 2012, 2017, 2018]})
df2


# %%
df_combined = pd.merge(df1, df2)
df_combined


# %%
df3 = pd.DataFrame({'group': ['Accounting', 'Marketing', 'HR'], 'supervisor': ['Carlos', 'Giada', 'Stephanie']})
df3


# %%
pd.merge(df_combined, df3, on='group')


# %%
df4 = pd.DataFrame({'group': ['Accounting', 'Accounting', 'Marketing', 'Marketing', 'HR', 'HR'], 'core_skills': ['math', 'spreadsheets', 'writing', 'communication', 'spreadsheets', 'organization']})
df4


# %%
df1


# %%
pd.merge(df1, df4, on='group')


# %%
left = pd.DataFrame({
    'id':[1,2,3,4,5],
    'Name':['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
    'subject_id':['sub1', 'sub2', 'sub4', 'sub6', 'sub5']})
left


# %%
right = pd.DataFrame({
    'id':[1,2,3,4,5],
    'Name':['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
    'subject_id':['sub2', 'sub4', 'sub3', 'sub6', 'sub5']})
right


# %%
pd.merge(left, right, on='subject_id', how='left')


# %%
pd.merge(left, right, on='subject_id', how='inner')


# %%
df5 = pd.DataFrame({'name':['Gary', 'Stu', 'Mary', 'Sue'], 'salary': [70000, 80000, 120000, 90000]})
df5


# %%
pd.merge(df1, df5, left_on="employee", right_on="name")


# %%
serie1 = pd.Series(['a', 'b', 'c'], index=[1, 2, 3])
serie1


# %%
serie2 = pd.Series(['d', 'e', 'f'], index=[4, 5, 6])
serie2


# %%
pd.concat([serie1, serie2])


# %%
one = pd.DataFrame({'A': ['a', 'c'], 'B': ['b', 'd']})
one


# %%
two = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
two


# %%
pd.concat([one, two], ignore_index=True, axis=1)


# %%
three = pd.DataFrame({'A': ['a', 'd'], 'B': ['b', 'e'], 'C': ['c', 'f']})
three


# %%
four = pd.DataFrame({'B': ['u', 'x'], 'C': ['v', 'y'], 'D': ['w', 'z']})
four


# %%
pd.concat([three, four])


# %%
pd.concat([three, four], join='inner')


# %%



