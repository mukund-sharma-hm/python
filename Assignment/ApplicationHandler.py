# from AppOpener import open, close
# import psutil
# dict = {}

# processes = psutil.process_iter()
# for process in processes:
    
#     if process.name() in dict:
#         dict[process.name()] += 1   #process.name vs process.name()
#     else:
#         dict[process.name()] = 1
#     # print(process)


# print("To open app try :'open <app name>' ")

# while True:
#     command = input("Enter the name of the App you want to open: -> ").lower()

#     if 'open' in command:

#         app_name = command.replace("open", "",).lstrip()
        
#         #to do

#         open(app_name, match_closest=True)

#     if 'close' in command:
#         app_name = command.replace('close', "").lstrip()

#         close(app_name, match_closest=True)

#     elif 'exit' == command or 'quit' == command:
#         break



import psutil

instance = []
def monitor_app(process_name, max_instnace):
    for process in psutil.process_iter(['pid','name']):
        if process.info['name'] == process_name:
            instance.append(p)

    if len(instance) > max_instnace:
        print(f"Killing {process_name} (more than {max_instnace})")
        instance[0].kill()
        print("killed process")
    else:
        print(f"Number of instances of {process_name}: {len(instance)}")
monitor_app('notepad.exe', 2)

        

        

