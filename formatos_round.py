# A partir del listado de números que tienes 
# a continuación, imprimirlos ordenados por 
# el punto decimal y con dos decimales.
 
# ORIGINAL    formatos
# 23.453        23.45
# 2.324         2.32
# 154           154.00
# 23142.253     23142.25
# 53.0000343    53.00

a=23.453
b=2.324
c=154
d=23142.253
e=53.0000343

f=round(a,2)
g=round(b,2)
h=round(c,2)
i=round(d,2)
j=round(e,2)

print("\n")
print("ORIGINAL".ljust(20),"formatos\n",a,"".rjust(15, " "),f,"\n",b,"".ljust(17, " "),g,"\n",c,"".ljust(20, " "),h,"\n",d,"".ljust(9, " "),i,"\n",e,"".ljust(12, " "),j,"\n")