import pandas
import numpy
numpy.random.seed(27)
biaoge=pandas.DataFrame({
    "姓名":[f"学生{i}" for i in range(1,101)],
    "班级":numpy.random.choice(["一班","二班","三班"],100),
    "语文":numpy.random.randint(70,125,100),
    "数学":numpy.random.randint(40,135,100),
    "英语":numpy.random.randint(60,130,100),
    })
biaoge.loc[20:30,"数学"]=numpy.nan
biaoge.to_csv(r"D:\PY\学生成绩表.csv",encoding="utf-8-sig",index=False)
print("success")