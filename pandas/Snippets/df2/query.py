import pandas as pd
  
# assign data
dataFrame = pd.DataFrame({'Name': [' RACHEL  ', ' MONICA  ', ' PHOEBE  ',
                                   '  ROSS    ', 'CHANDLER', ' JOEY    '],
                            
                          'Age': [30, 35, 37, 33, 34, 30],
                            
                          'Salary': [100000, 93000, 88000, 120000, 94000, 95000],
                            
                          'JOB': ['DESIGNER', 'CHEF', 'MASUS', 'PALENTOLOGY',
                                  'IT', 'ARTIST']})
  
# filter dataframe 
display(dataFrame.query('Salary  <= 100000 & Age < 40 & JOB.str.startswith("C").values'))