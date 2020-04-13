import Start as st
import Source as s
import json
import os

start = st.Start()
start.render()
sources = []

print("Write \"help\" in order to view all commands")

running = True
while(running):
    command = input('> ').lower()

    #shows all commands
    if(command == 'help' or command == 'h'):
        print("""..:::COMMANDS:::..
add  / a : adds a source
view / v : shows all keys + title pairs
save / s : saves all sources as a JSON file
load / l : loads soures from a JSON file
quit / q : closes the script""")

    #adds a source
    if(command == 'add' or command == 'a'):
        sources.append(s.Source())
        sources[len(sources)-1].create(sources)

    #shows all sources
    if(command == 'view' or command == 'v'):
        for source in sources:
            print(source.key+": "+source.title)
    
    #saves all sources as a JSON file
    if(command == 's' or command == 'save' ):
        files = os.listdir(os.path.join("sources"))
        name = input('Save file as: ')
        if(name+".json" not in files):    
            tree = {}
            for source in sources:
                tree[source.key] = source.dict()
            js = json.dumps(tree)
            
            f = open(os.path.join("sources", name+".json"), "x")
            f.write(js)
            f.close()
        else:
            print("Sorry, a file with this name already exists")

    #loads soures from a JSON file
    if(command == 'l' or command == 'load' ):
        print('All available source files are: ')
        files = os.listdir(os.path.join("sources"))
        for file in files:
            print(file.strip('.json')) 
        file_to_load = input('Which file would you like to load?: ')
        if(file_to_load+".json" in files):
            f = open(os.path.join("sources", file_to_load+".json"), 'r')
            source_list = json.load(f)
            for key, data in source_list.items():
                sources.append(s.Source())
                sources[len(sources)-1].generate(key, data['title'], data['authors'], data['date'], data['viewing_date'], data['url'])
        else:
            print('This file doesn\'t exist')

    #quits the script
    if(command == "q" or command == "quit"):
        running = False