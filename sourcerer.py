import Start as st
import Source as s
import json
import os

start = st.Start()
start.render()
sources = []

running = True
while(running):
    command = input('> ').lower()

    #adds a source
    if(command.lower() == 'add'):
        sources.append(s.Source())
        sources[len(sources)-1].create(sources)

    #shows all sources
    if(command == 'show'):
        for source in sources:
            print(source.key+": "+source.title)
    
    #saves all sources as a JSON file
    if(command == 's' or command == 'save' ):
        tree = {}
        for source in sources:
            tree[source.key] = source.dict()
        js = json.dumps(tree)
        name = input('Save file as: ')
        f = open(os.path.join("sources", name+".json"), "x")
        f.write(js)
        f.close()

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
                sources[len(sources)-1].generate(key, data['title'], data['authors'])
        else:
            print('This file doesn\'t exist')

    #quits the script
    if(command == "q" or command == "quit"):
        running = False