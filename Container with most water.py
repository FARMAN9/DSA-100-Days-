def max_area(array):
    area=0
    length = len(array)
    if length==0 or length==1:
        return  area
    for i in range(length):
        for j in range(i+1,length):
            hight=min(array[i],array[j])
            wight=(j-i)
            area=max(area,wight*hight)
    return area





print("Max area",max_area([1,2,1]))