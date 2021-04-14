import csv
from operator import itemgetter
from random import randint
import random
with open('hutang.csv') as csvfile:
    reader = csv.reader(csvfile)
    line_count = 0
    allIncome = []
    allDebt = []
    lowestIncome = 1000
    highestIncome = 0
    highestDebt = 0
    lowestDebt = 1000
    arrIncome = []
    arrDebt = []

    #Pencarian hutang terbesar & terkecil, pendapatan terbesar & terkecil
    for row in reader:
        if line_count == 0:
            line_count += 1
        else:
            a = float(row[1])
            b = float(row[2])
            if lowestIncome > a:
                lowestIncome = a
            if highestIncome < a:
                highestIncome = a
            if highestDebt < b:
                highestDebt = b
            if lowestDebt > b:
                lowestDebt = b   
            arrIncome.append(a)
            arrDebt.append(b)   

    #Design Membership Function

    #Perhitungan persentase titik pendapatan/hutang tiap kepala keluarga
    #arrHiIncome berisi poin pendapatan tinggi
    arrHiIncome = []
    #arrMidIncome berisi poin pendapatan menengah
    arrMidIncome = []
    #arrLoIncome berisi poin pendapatan menengah
    arrLoIncome = []
    #arrHiDebt berisi poin hutang besar
    arrHiDebt = []
    #arrMidDebt berisi poin hutang lumayan
    arrMidDebt = []
    #arrLoDebt berisi poin hutang kecil
    arrLoDebt = []
    #Poin pada setiap array di atas merupakan poin setiap kepala keluarga
    #Persentase tiap titik pendapatan
    arrGap = [0.25,0.35,0.25,0.4,0.6,0.75,0.65,0.75]
    #Persentase tiap titik hutang
    arrGap2 = [0.15,0.25,0.2,0.3,0.6,0.7,0.65,0.75]
    
    #Perhitungan persentase titik
    for a in arrIncome:
        mark = 0
        if(a>=(((highestIncome-lowestIncome)*arrGap[7])+lowestIncome)):
            mark = 1
        elif(a<(((highestIncome-lowestIncome)*arrGap[6])+lowestIncome)):
            mark = 0
        else:
            mark = (a-(((highestIncome-lowestIncome)*arrGap[6])+lowestIncome))/((((highestIncome-lowestIncome)*arrGap[7])+lowestIncome)-(((highestIncome-lowestIncome)*arrGap[6])+lowestIncome))
        arrHiIncome.append(mark)
        if(a<(((highestIncome-lowestIncome)*arrGap[2])+lowestIncome) or a>(((highestIncome-lowestIncome)*arrGap[5])+lowestIncome)):
            mark = 0
        elif(a<=(((highestIncome-lowestIncome)*arrGap[4])+lowestIncome) and a>=(((highestIncome-lowestIncome)*arrGap[3])+lowestIncome)):
            mark = 1
        elif(a>(((highestIncome-lowestIncome)*arrGap[4])+lowestIncome) and a<=(((highestIncome-lowestIncome)*arrGap[5])+lowestIncome)):
            mark = ((((highestIncome-lowestIncome)*arrGap[5])+lowestIncome)-a)/((((highestIncome-lowestIncome)*arrGap[5])+lowestIncome)-(((highestIncome-lowestIncome)*arrGap[4])+lowestIncome))
        else:
            mark = (a-(((highestIncome-lowestIncome)*arrGap[2])+lowestIncome))/((((highestIncome-lowestIncome)*arrGap[3])+lowestIncome)-(((highestIncome-lowestIncome)*arrGap[2])+lowestIncome))
        arrMidIncome.append(mark)
        if(a<=(((highestIncome-lowestIncome)*arrGap[0])+lowestIncome)):
            mark = 1
        elif(a>(((highestIncome-lowestIncome)*arrGap[1])+lowestIncome)):
            mark = 0
        else:
            mark = ((((highestIncome-lowestIncome)*arrGap[1])+lowestIncome)-a)/((((highestIncome-lowestIncome)*arrGap[1])+lowestIncome)-(((highestIncome-lowestIncome)*arrGap[0])+lowestIncome))
        arrLoIncome.append(mark)
    for b in arrDebt:
        mark = 0
        if(b>=(((highestDebt-lowestDebt)*arrGap2[7])+lowestDebt)):
            mark = 1
        elif(b<(((highestDebt-lowestDebt)*arrGap2[6])+lowestDebt)):
            mark = 0
        else:
            mark = (b-(((highestDebt-lowestDebt)*arrGap2[6])+lowestDebt))/((((highestDebt-lowestDebt)*arrGap2[7])+lowestDebt)-(((highestDebt-lowestDebt)*arrGap2[6])+lowestDebt))
        arrHiDebt.append(mark)
        if(b>=(((highestDebt-lowestDebt)*arrGap2[3])+lowestDebt) and b<=(((highestDebt-lowestDebt)*arrGap2[4])+lowestDebt)):
            mark = 1
        elif(b>((highestDebt-lowestDebt)*arrGap2[5])+lowestDebt or b<(((highestDebt-lowestDebt)*arrGap2[2])+lowestDebt)):
            mark = 0
        elif(b>(((highestDebt-lowestDebt)*arrGap2[4])+lowestDebt) and b<=(((highestDebt-lowestDebt)*arrGap2[5])+lowestDebt)):
            mark = ((((highestDebt-lowestDebt)*arrGap2[5])+lowestDebt)-b)/((((highestDebt-lowestDebt)*arrGap2[5])+lowestDebt)-(((highestDebt-lowestDebt)*arrGap2[4])+lowestDebt))
        else:
            mark = (b-(((highestDebt-lowestDebt)*arrGap2[2])+lowestDebt))/((((highestDebt-lowestDebt)*arrGap2[3])+lowestDebt)-(((highestDebt-lowestDebt)*arrGap2[2])+lowestDebt))
        arrMidDebt.append(mark)
        if(b<=(((highestDebt-lowestDebt)*arrGap2[0])+lowestDebt)):
            mark = 1
        elif(b>(((highestDebt-lowestDebt)*arrGap2[1])+lowestDebt)):
            mark = 0
        else:
            mark = ((((highestDebt-lowestDebt)*arrGap2[1])+lowestDebt)-b)/((((highestDebt-lowestDebt)*arrGap2[1])+lowestDebt)-(((highestDebt-lowestDebt)*arrGap2[0])+lowestDebt))
        arrLoDebt.append(mark)
    
    #Penggabungan semua titik Pendapatan (Tinggi, Menengah, Rendah)
    allIncome.append(arrHiIncome)
    allIncome.append(arrMidIncome)
    allIncome.append(arrLoIncome)
    #Penggabungan semua titik Hutang (Besar, Lumayan, Sedikit)
    allDebt.append(arrHiDebt)
    allDebt.append(arrMidDebt)
    allDebt.append(arrLoDebt)

    #Fuzzy Rules

    #1 = ya
    #2 = mungkin
    #3 = tidak
    arrPotention1 = []
    arrPotention2 = []
    arrPotention3 = []
    x = 0
    a = 0
    b = 0
    mark1 = 0
    mark2 = 0
    mark3 = 0
    mark4 = 0
    while(x<100):
        note = []
        for a in range(3):
            for b in range(3):
                if(a == 1 and b == 0):
                    if(allDebt[b][x]>allIncome[b][x]):
                        mark1 = allIncome[a][x]
                    else:
                        mark1 = allDebt[b][x]
                    note.append(mark1)
                if(a == 2 and b == 0):
                    if(allDebt[b][x]>allIncome[a][x]):
                        mark2 = allIncome[a][x]
                    else:
                        mark2 = allDebt[b][x]
                    note.append(mark2)
                if(a == 2 and b == 1):
                    if(allDebt[b][x]>allIncome[a][x]):
                        mark3 = allIncome[a][x]
                    else:
                        mark3 = allDebt[b][x]
                    note.append(mark3)
        arrPotention1.append(max(note))
        note = []
        for a in range(3):
            for b in range(3):   
                if(a == 0 and b == 0):
                    if(allDebt[b][x]>allIncome[a][x]):
                        mark1 = allIncome[a][x]
                    else:
                        mark1 = allDebt[b][x]
                    note.append(mark1)
                if(a == 1 and b == 1):
                    if(allDebt[b][x]>allIncome[a][x]):
                        mark2 = allIncome[a][x]
                    else:
                        mark2 = allDebt[b][x]
                    note.append(mark2)
                if(a == 2 and b == 2):
                    if(allDebt[b][x]>allIncome[a][x]):
                        mark3 = allIncome[a][x]
                    else:
                        mark3 = allDebt[b][x]
                    note.append(mark3)
        arrPotention2.append(max(note))
        note = []
        for a in range(3):
            for b in range(3):            
                if(a == 0 and b == 1):
                    if(allDebt[b][x]>allIncome[a][x]):
                        mark1 = allIncome[a][x]
                    else:
                        mark1 = allDebt[b][x]
                    note.append(mark1)
                if(a == 0 and b == 2):
                    if(allDebt[b][x]>allIncome[a][x]):
                        mark2 = allIncome[a][x]
                    else:
                        mark2 = allDebt[b][x]
                    note.append(mark2)
                if(a == 1 and b == 2):
                    if(allDebt[b][x]>allIncome[a][x]):
                        mark3 = allIncome[a][x]
                    else:
                        mark3 = allDebt[b][x]
                    note.append(mark3)
        arrPotention3.append(max(note))
        x+=1
    arrPotention = []
    arrPotention.append(arrPotention1)
    arrPotention.append(arrPotention2)
    arrPotention.append(arrPotention3)

    #Defuzzification

    #arrZ adalah array yang digunakan untuk menampung nilai Sugeno
    arrZ = []
    i = 0
    arrFinish = []
    while(i<100):
        j = 0
        x = ((arrPotention1[i]*100)+(arrPotention2[i]*70)+(arrPotention3[i]*50))
        y = (arrPotention1[i]+arrPotention2[i]+arrPotention3[i])
        arrZ.append(x/y)
        i+=1  
    arrTemp = []
    i=1
    while(i<=100):
        arrTemp.append([i, arrZ[i-1]])
        i+=1
    
    #Digunakan untuk sort berdasarkan nilai sugeno
    arrTemp.sort(key=lambda x: x[1])
    arrTemp.reverse()
    #Digunakan untuk memotong array, hanya 20 data tertinggi yang diambil
    arrFinish = arrTemp[:-80]
    
    #Output program, variabel j digunakan untuk memastikan jumlah data yang dikeluarkan
    j = 0
    for i in arrFinish:
        print(i)
        j+=1
    print(j)

    #Digunakan untuk menulis data nomor kepala keluarga ke file keluarga
    with open('hutang.csv','w') as file:
        for i in range(20):
            file.write('%d' % arrFinish[i][0])
            file.write('\n')