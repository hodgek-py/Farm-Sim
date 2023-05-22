from hmac import new
import random

class Farm_Sim:
    def __init__(self, time, period = 'D',counter = 0):
        self.period = period
        self.time = time
        self.counter = counter

    def simulation(self):
        sim = Sim_Var(2,1,50,2)
        print(sim.spread)
        while self.time > self.counter:
            print(self.counter)
            self.counter += 1

class Sim_Var:
    def __init__(self,crop,rain,size,fertilizer,ratio = (1/3)):
        self.crop = crop
        self.rain = rain
        self.size = size
        self.fertilizer = fertilizer
        self.ratio = ratio
        self.spread = self.ratio * self.size

    def rain_day(self):
        pass

    def disease(self):
        pass


mister = Farm_Sim(15)
print(mister.simulation())