#Шахов Кирилл
#ИВТ 2 курс 
def zip2(keys,values):
    res = {}
    it = iter(values)
    nullValue = False
    for key in keys:
        try:            
            res[key] = it.next() if not nullValue else None
        except StopIteration:
            nullValue = True
            res[key] = None
    return res

print( zip2([],[]) == {})
print( zip2([1,2,3],[4,5,6]) == {1:4,2:5,3:6} )
print( zip2([1,2],[4,5,6]) == {1:4,2:5} )
print( zip2([1,2,3],[4,5]) == {1:4,2:5,3:None} )
