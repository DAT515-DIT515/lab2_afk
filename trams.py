
#for now we have the file here, but I think they want us to read it from another folder, so we might need to rename the repos.
import json
import sys
TRAM_FILE = 'tramnetwork.json'

def readTramNetwork(tramfile=TRAM_FILE):
    
    with open(tramfile, 'r') as file:
        TramNetwork = json.load(file)
        return TramNetwork
    
print(readTramNetwork())




class TramNetwork:
    
    def __init__(start):
        pass
    
class TramLine:
    
    def __init__(num,stops):
        pass

class TramStop:
    
    def __init__(name, lines, lan, lon):
        pass