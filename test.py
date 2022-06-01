from collections import OrderedDict

temps = [('2000', -4.4), ('2001', -2.5), ('2002', -4.4), ('2003', -9.5),
        ('2004', -8.2), ('2005', -1.6), ('2006', -5.9), ('2007', -2.4),
        ('2008', -1.7), ('2009', -3.5), ('2010', -12.1), ('2011', -5.8),
        ('2012', -4.9), ('2013', -6.1), ('2014', -6.9), ('2015', -2.7),
        ('2016', -11.2), ('2017', -3.9), ('2018', -2.9), ('2019', -6.5),
        ('2020', 1.5)]
         
# Напечатайте словарь из температур, отсортированный по уменьшению температуры

a = 0
b = 0
only_temps = list()
for i in temps:
    only_temps.append(i[1])

sort_temps = list()

while len(only_temps) > 0:
    a = only_temps.index(max(only_temps))
    sort_temps.append(only_temps[a])
    only_temps.pop(a)

dict1 = OrderedDict()

while True:
    if b == 1:
        break
    for i in temps:
        if i[1] == sort_temps[0]:
            dict1[i[0]] = sort_temps[0]
            sort_temps.pop(0)
            if len(sort_temps) == 0:
                b = 1
                break
            

print(dict1)
    
    
        

    
    
    
