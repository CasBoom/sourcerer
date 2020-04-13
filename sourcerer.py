import Start as st
import Source as s

start = st.Start()
start.render()
sources = []

running = True
while(running):
    command = input('> ')
    if(command.lower() == 'add'):
        sources.append(s.Source())

    if(command.lower() == "q"):
        running = False