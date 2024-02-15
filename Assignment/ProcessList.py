# import wmi

# p = wmi.WMI()
#cant instantiate  WMI class directly

import csv
import psutil
dict = {}


        

processes = psutil.process_iter()
for process in processes:
    
    if process.name() in dict:
        dict[process.name()] += 1   #process.name vs process.name()
    else:
        dict[process.name()] = 1
    print(process)

for name, count in dict.items():
        print(f"{name}: {count}")

with open("C:\js\python\Assignment\Processes.csv", 'w', newline="") as file:
    writer = csv.DictWriter(file, fieldnames= ['Name','Count'])

    writer.writerow( {'Name': 'Process Name', 'Count': "Count"})
    for name, count in dict.items():
        writer.writerow( {'Name': name ,'Count': count})
# print(dict)