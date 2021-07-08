# fonksiyonumuzun çıktıları bu listede toplanıyor. 
flattenList = []

def flatten(sample):
    for item in sample:
        if type(item) != type([]): #verilen input'un elemanlarında gezip, elemanların liste olup olmadığını kontrol ediliyor. bu sorgulamaya set, dictionary, tuple gibi non-scalar yapılar da eklenebilirdi. 
            flattenList.append(item) # eğer eleman liste değilse ya da bir başka deyişle scalar yapıdaysa listemize ekliyoruz.
        else:
            flatten(item) #recursive fonksiyon yardımıyla elemanların tamamı scalar yapıya gelene kadar bu işlemi tekrarlıyoruz. 

patika_list = [[1,'a',['cat'],2],[[[3]],'dog'],4,5,]
flatten(patika_list)
print(flattenList)
