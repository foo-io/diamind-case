#!/usr/bin/env python
# coding: utf-8
import time
start_time = time.time()

import pandas as pd
import seaborn as sns

import matplotlib.pyplot as plt
import numpy as np

import xlrd

from k_means_constrained import KMeansConstrained

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.cluster import KMeans

# Перманентно поменял настройки вывода графиков
from matplotlib import pylab
from pylab import *


# In[2]:


df = pd.read_excel("static/uploads/case.xlsm", sheet_name="Таблица")
df.info()


# In[3]:


df = df.rename(
    columns={
        "Номер": "id",
        "Форма": "form",
        "Цвет": "color",
        "form": "",
        "Размер": "size",
        "Флуоресценция": "light",
        "Вес": "weight",
        "Стоимость": "cost",
    }
)
del df["id"]
df.head(10)


# In[4]:


### Отсортировали значения по средней стоимости от меньшего к большему
def declare_cost(col):
    print(df.groupby(col)["cost"].mean().sort_values())


declare_cost("form")
declare_cost("color")
declare_cost("size")
declare_cost("light")


# Самый дорогой - круглый, зеленый, большой, светящийся камень<br>
# Самый дешевый - треугольный, красный, малый, не светящийся камень

# In[5]:


def count_of(col):
    hist = (
        df.groupby(col)
        .agg({col: "count", "cost": "sum"})
        .rename(columns={col: "count"})
    )
    return hist


# In[6]:


"""Самая частая форма"""
count_of("form")["count"].sort_values().tail(1)
"""Самый частый цвет"""
count_of("color")["count"].sort_values().tail(1)
"""Самый частый размер"""
count_of("size")["count"].sort_values().tail(1)
"""Самая частая флуоресценция"""
count_of("light")["count"].sort_values().tail(1)


# <a id='step_2'></a>
# ## 2. Исследовательский анализ данных:

# <a id='step_21'></a>
# ### 2.1 Сортировка признаков по стоимости,  средние значения и стандартные отклонения:

# In[7]:


main_dict = {}


def text_to_int(x):
    return d.get(x)


"""Заменил названия на числовые значения по словарю:"""
for col_name in df.select_dtypes(include=["object"]).columns.tolist():
    d = {}
    n = 0
    for col_dict in df.groupby(col_name)["cost"].mean().sort_values().index:
        d.update({col_dict: n})
        n += 1
    main_dict.update({col_name: d})
    df[col_name] = df[col_name].apply(lambda x: text_to_int(x))

main_dict
df.head(10)


# In[8]:


df.describe()


# In[9]:


df["weight"].to_frame().boxplot()


# In[10]:


df["cost"].to_frame().boxplot()


# Выводы:
# * Средняя стоимость камней 3.65
# * Средний вес 333.69
# * В основном вес камней от 197 до 333. Камни больше весом больше 800, считаются редкостью
# * Самый маленький камень весом 2, самый большой - 992.

# <a id='step_24'></a>
# ### 2.2 Матрица корелляций:

# In[11]:


cm = df.corr()
plt.figure(figsize=(14, 10))
sns.heatmap(cm, annot=True, fmt="0.2f", linewidths=0.5)
plt.show()


# ### Вывод

# На стоимость в первую очередь влияет размер/вес. В меньше степени форма, цвет и флуоресценция.

# <a id='step_4'></a>
# ## 3. Кластеризация камней:

# In[12]:


# Провел стандартизацию всех параметров
df_sс = df.drop(["cost", "weight"], axis=1)
df_columns_list = df_sс.columns

# Преобразовал набор данных
df_sс = StandardScaler().fit_transform(df_sс)
df_sс = pd.DataFrame(df_sс, columns=df_columns_list).astype("float64")

"""Веса параметров"""
df_sс

# Сформировал таблицу связок
linked = linkage(df_sс, method="ward")

km = KMeansConstrained(
    init="k-means++", n_clusters=10, size_min=100, size_max=100, random_state=0
)
labels = km.fit_predict(df_sс)
df["cluster"] = labels

"""Количество камней в каждом кластере"""
df.cluster.value_counts()

"""Средние значения по кластерам"""
df.groupby("cluster").mean().T


# In[13]:


df_final = df

reverse_dict = {}

for item in main_dict:
    temp_dict = {v: k for k, v in main_dict[item].items()}
    reverse_dict.update({item: temp_dict})

reverse_dict

for col_name in reverse_dict.keys():
    df_final[col_name] = df_final[col_name].map(reverse_dict[col_name])

df_final.head(10)


# ### Результат

# In[19]:


def data_mart(col_name):
    grouped = (
        df_final.groupby(["cluster", col_name])
        .agg({col_name: "count", "weight": "sum", "cost": "sum"})
        .rename(columns={col_name: "count"})
    )
    grouped_perc = (
        df_final.groupby(["cluster", col_name])
        .agg({col_name: "count"})
        .rename(columns={col_name: "percent"})
        .groupby(level=0)
        .apply(lambda x: 100 * x / float(x.sum()))
    )
    grouped["percent"] = grouped_perc["percent"]
    #
    return grouped


# In[52]:


df_final.set_index(["cluster"]).sort_values(by="cluster")


# In[195]:


data = {"clusters": {}}
data["clusters"]["id"] = {}
data


# In[248]:


data_mart("form").head(1)


# In[271]:


# In[265]:


final_parameters = pd.DataFrame(columns=["cluster", "items"])

for parameter in reverse_dict:
    temp = (
        data_mart(parameter)
        .reset_index()
        .groupby(["cluster", parameter])
        .apply(
            lambda x: x[[parameter, "count", "weight", "cost", "percent"]].to_dict(
                "records"
            )
        )
        .reset_index()
        .rename(columns={0: "items"})
    )
    #     temp['']
    final_parameters = final_parameters.append(temp)

with open("static/results/parameters.json", "w", encoding="utf-8") as file:
    final_parameters.sort_values(by="cluster").to_json(
        file, orient="records", force_ascii=False
    )


# In[267]:


final_parameters


# In[278]:


df_final


# In[277]:


data_mart("form").reset_index().sort_values(by="cluster")


# In[279]:


d = (
    data_mart("form")
    .reset_index()
    .sort_values(by="cluster")
    .groupby(["cluster"])
    .apply(lambda x: x[["form", "percent"]].to_dict("records"))
    .reset_index()
    .rename(columns={0: "items"})
)
d


# In[234]:


j = (
    df_final.groupby(["cluster"])
    .apply(
        lambda x: x[["form", "color", "size", "light", "weight", "cost"]].to_dict(
            "records"
        )
    )
    .reset_index()
    .rename(columns={0: "items"})
)
with open("static/results/rs.json", "w", encoding="utf-8") as file:
    j.to_json(file, orient="records", force_ascii=False)


# In[272]:
print(j.to_json(orient='records', force_ascii=False))
print("Время выполнения скрипта: %s seconds" % (time.time() - start_time))