'''
Created on Dec 24, 2014

@author: JA
'''
# Pour permettre <aparition des evenements

       
    
##########################################################
#
##########################################################                                                        
class EventMenu(gui.Dialog):  
    def __init__(self, island):
        title = gui.Label("Resources Management")
        self.island = island
        self.ZoneSrc = gui.Select(value=Island.LANDING_REGION_NAME , width=160, height=20)
        self.ZoneDst = gui.Select(value="RegionB" , width=160, height=20)        
        t = gui.Table()
        self.value = gui.Form()
        self.widgetList = []
        
        # Origin and destination zone
        t.tr()
        for item in sorted(Island.secteurDef):
            if(item != Island.OVERVIEW_ZONE_NAME):
                self.ZoneSrc.add(item, item)
                self.ZoneDst.add(item, item)
        self.ZoneSrc.connect(gui.CHANGE, self.action_ChangeZone, "src")
        self.ZoneDst.connect(gui.CHANGE, self.action_ChangeZone, "dst")        
        t.td(self.ZoneSrc)
        t.td(gui.Label("Origine"))
        t.td(gui.Label(""))   
        t.td(gui.Label("Destination"))
        t.td(self.ZoneDst)
        
        # Population
        t.tr()
        t.td(gui.Label("Population"))
        t.td(CustomWidget.DemographieLabel(self.island, self.ZoneSrc, "PopulationActive"))
        s = PopulationSlider(self.island, self.ZoneSrc, self.ZoneDst)
        self.widgetList.append(s)
        t.td(s)
        t.td(CustomWidget.DemographieLabel(self.island, self.ZoneDst, "PopulationActive"))     

        
        # Resources
        for item in sorted(resources.resourceDef):         
            t.tr()
            t.td(gui.Label(item))
            t.td(CustomWidget.StockLabel(self.island, self.ZoneSrc, item))
            s = ResourcesSlider(self.island, self.ZoneSrc, self.ZoneDst, item)
            self.widgetList.append(s)
            t.td(s)
            t.td(CustomWidget.StockLabel(self.island, self.ZoneDst, item))     

        gui.Dialog.__init__(self,title,t)

    def action_TransferPopulation(self, slider):
        slider.populationToMove
        self.island.secteur[self.ZoneSrc.value].population.current -=  slider.populationToMove
        self.island.secteur[self.ZoneDst.value].population.current +=  slider.populationToMove
    
    def action_ChangeZone(self, origin):
        if(self.ZoneSrc.value == self.ZoneDst.value):
            zoneCtl = self.ZoneDst if(origin == "src") else self.ZoneSrc  
            i =  zoneCtl.values.index(zoneCtl.top_selected.value)
            i = 0 if(i+1 >= len(zoneCtl.values)) else (i+1)
            zoneCtl.value =  zoneCtl.values[i].value 
        for w in self.widgetList:
            w.Refresh()    