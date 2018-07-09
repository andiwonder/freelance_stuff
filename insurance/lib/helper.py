def getBaseRate(Ann_Revenue_Norm):
  if Ann_Revenue_Norm <= 100 :
    return [100]
  elif Ann_Revenue_Norm > 100 and Ann_Revenue_Norm < 250 :
    return [100, 250]
  elif Ann_Revenue_Norm == 250 :
    return [250]
  elif 250 < Ann_Revenue_Norm < 500 :
    return [250, 500]
  elif Ann_Revenue_Norm == 500 :
    return [500]
  elif 500 < Ann_Revenue_Norm < 750 :
    return [500, 750]
  elif Ann_Revenue_Norm == 750 :
    return [750]
  elif 750 < Ann_Revenue_Norm < 1000 :
    return [750, 1000]
  elif Ann_Revenue_Norm == 1000 :
    return [1000]
  elif 1000 < Ann_Revenue_Norm < 1500 :
    return [1000, 1500]
  elif Ann_Revenue_Norm == 1500 :
    return [1500]
  elif 1500 < Ann_Revenue_Norm < 2000 :
    return [1500, 2000]
  elif Ann_Revenue_Norm == 2000 :
    return [2000]
  elif 2000 < Ann_Revenue_Norm < 3000 :
    return [2000, 3000]
  elif Ann_Revenue_Norm == 3000 :
    return [3000]
  elif 3000 < Ann_Revenue_Norm < 4000 :
    return [3000, 4000]
  elif Ann_Revenue_Norm == 4000:
    return [4000]
  elif 4000 < Ann_Revenue_Norm < 5000:
    return [4000, 5000]
  elif Ann_Revenue_Norm == 5000:
    return [5000]
  elif 5000 < Ann_Revenue_Norm < 6000 :
    return [5000, 6000]
  elif Ann_Revenue_Norm == 6000:
    return [6000]