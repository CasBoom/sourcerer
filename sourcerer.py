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
    if(command.lower() == 'add'):
        sources.append(s.Source())

    if(command == 'show'):
        for source in sources:
            print(source.key+": "+source.title)
    
    if(command == 's' or command == 'save' ):
        tree = []
        for source in sources:
            tree.append(source.dict())
        js = json.dumps(tree)
        name = input('Save file as: ')
        f = open(os.path.join("sources", name+".json"), "x")
        f.write(js)
        f.close()

    if(command == "q" or command == "quit"):
        running = False