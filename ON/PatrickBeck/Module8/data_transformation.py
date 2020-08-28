# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import numpy as np
import pandas as pd


# %%
trans = pd.DataFrame({"A":[12, 4, 5, None, 1],
                    "B":[7, 2, 54, 3, None],
                    "C":[20, 16, 11, 3, 8],
                    "D":[14, 3, None, 2, 6]},
                    index=['Row_1', 'Row_2', 'Row_3', 'Row_4', 'Row_5'])
trans


# %%
result = trans.transform(lambda x : x + 10)
result


# %%
result2 = trans.transform([np.sqrt, np.exp])
result2


# %%
x = np.random.randint(10, 200, size=10)
x


# %%
np.digitize(x,bins=[50])


# %%
np.digitize(x, bins=[50, 100])


# %%
df = pd.DataFrame({"height": x})
df


# %%
df['binned'] = pd.cut(x=df['height'], bins=[0, 25, 50, 100, 200])
df


# %%
df['bin_label'] = pd.cut(x = df['height'],
                        bins = [0, 25, 50, 100, 200],
                        labels = [1, 2, 3, 4])
df


# %%
pd.qcut(df['height'], q=5)


# %%
degrees = ["none", "cum laude", "magna cum laude", "summa cum laude"]
student_results = [3.93, 3.24, 2.80, 2.83, 3.91, 3.698, 3.731, 3.25, 3.24, 3.82, 3.22]
student_results.sort(reverse=True)

student_results_degrees = pd.cut(student_results, [0, 3.6, 3.8, 3.9, 4.0], labels=degrees)
honor = pd.DataFrame({'grades': student_results,
                    'honors': student_results_degrees})
honor


# %%
pd.value_counts(student_results_degrees).plot.bar()


# %%



