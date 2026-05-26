from decimal import Decimal,ROUND_HALF_UP
scores=[78,92,85,64,99,88,73,82,91,60,57,100]
re1=0
for i in range(len(scores)):
        re1+=scores[i]
print(re1)
def averages_decimal(value,n):
        value=value/12
        xs="0."+"0"*n
        re2=Decimal(str(value)).quantize(Decimal(xs),rounding=ROUND_HALF_UP)
        return re2
print(f"平均分:{averages_decimal(re1,1)}")
print(f"总分为:{re1}")
mx=scores[0]
for i in range(len(scores)):
        if scores[i]>mx:
                mx=scores[i]
print(f"最高分:{mx}")
mn=scores[0]
for i in range(len(scores)):
        if scores[i]<mn:
                mn=scores[i]
print(f"最低分:{mn}")
a,b,c,d,e=0,0,0,0,0
for j in scores:
        if 90<j<=100:
                a+=1
        if 80<j<=90:
                b+=1
        if 70<j<=80:
                c+=1
        if 60<j<=70:
                d+=1
        if 50<j<=60:
                e+=1
print(f"90到100分段人数为:{a}")
print(f"80到90分段人数为:{b}")
print(f"70到80分段人数为:{c}")
print(f"60到70分段人数为:{d}")
print(f"50到60分段人数为:{e}")
list_new=[y for y in scores if y>=60]
z=len(list_new)
lv=averages_decimal(z,2)
print(f"百分率:{lv}")
print(sorted(scores,reverse=True))
for i in range(len(scores)):
        if scores[i]<60:
                print(f"不及格成绩:{scores[i]}")
        else:
                continue
                
                        




        