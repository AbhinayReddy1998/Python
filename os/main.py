import os
if(not os.path.exists("data")):
 os.mkdir("Data")
for i in range (0,101):
      #os.mkdir(f"data/Data{i+1}")
      os.rename(f"data/Tutorial{i+1}",f"data/Tutorial {i+1}")