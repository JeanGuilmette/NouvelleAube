import Island
import Events

class EventImpact(object):
    def __init__(self, island):
        self.island = island


    def Apply(self, evt):
        if(len(evt.regions) > 0 and len(evt.effects) > 0):
            for s in evt.regions:
                for item in evt.effects: 
                    self.Analyze(evt.name, s, item)          
    
    def Analyze(self, evtName, secteur, effect):
        t = effect.split('=')
        token = t[0]
        value = t[1]
        
        if(token == "population"):
            self.island.ModifyPopulation(secteur, value)
            print("%s modify %s population by %s" % (evtName, secteur, value))
        elif(token == "panic"):
            self.island.ModifyPanic(secteur, value)
            print("%s modify %s panic by %s" % (evtName, secteur, value) )               
