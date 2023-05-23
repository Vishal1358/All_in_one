def get_earliest(date1,date2):
    day1, month1, year1 = map(int, date1.split("/"))
    day2, month2, year2 = map(int, date2.split("/"))
    
    if year1 > year2:
        return date1
    elif year2 < year2:
        return date2
    else:
        if month1 >= 1 and month1 < 31 and month2 >= 1 and month2 <= 31:
             
            if month1 > month2:
                return date1
            elif month1 < month2:
                return date2
        
            else:
                if day1 > day2:
                    return date1
                else:
                    return date2
            
print(get_earliest("25/12/2029","03/12/2029"))