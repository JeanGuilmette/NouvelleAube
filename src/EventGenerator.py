import random
import EventDef


class GenerateEvents(object):
    def __init__(self):
        pass
    
    def Generate(self):
        a = random.random()
        print("random: %f", a)
        if(a < 0.005):
            EventDef.evt_epidemie.regions = ["RegionA"]
            EventDef.evt_epidemie.effects = ["population=-100", "panic=12"]
            return EventDef.evt_epidemie
        
        if(a > 0.999):
            EventDef.evt_seisme.regions = ["RegionA", "RegionB", "RegionC", "RegionF"]
            EventDef.evt_seisme.effects = ["population=-100", "panic=50"]
            return EventDef.evt_seisme
        return False