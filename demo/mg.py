p1=input('Hg_mm=')
p1=float(p1)
t=input('T=')
t=float(t)
m1=input('m1 of mg=')
m1=float(m1)
m2=input('m2 of mg=')
m2=float(m2)
m3=input('m3 of mg=')
m3=float(m3)
n1=input('number_start=')
n1=float(n1)
n2=input('number_end=')
n2=float(n2)
n3=input('number_start=')
n3=float(n3)
n4=input('number_end=')
n4=float(n4)
n5=input('number_start=')
n5=float(n5)
n6=input('number_end=')
n6=float(n6)
p=((p1*10)/76)*101.325
d1=n2-n1
d2=n4-n3
d3=n6-n5
p_h=p-1.683
nh1=(p_h*d1)/((t+273.15)*8.314)
nh2=(p_h*d2)/((t+273.15)*8.314)
nh3=(p_h*d3)/((t+273.15)*8.314)
M1=m1/nh1
M2=m2/nh2
M3=m3/nh3
M_r=(M1+M2+M3)/3
e=(M_r-24.305)/24.305
print(M1,M2,M3)
print('Mg的相对分子质量是：',M_r)
print('相对误差为：',e)

