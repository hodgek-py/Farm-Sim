from hmac import new
import random

class Farm_Sim:
    def __init__(self, time, period = 'D',counter = 0):
        self.period = period
        self.time = time
        self.counter = counter

    def simulation(self):
        while self.time > self.counter:
            print(self.counter)
            self.counter += 1

class Sim_Var:
    def __init__(self,amount,crop,ratio,rain,size,fertilizer):
        self.amount = amount
        self.crop = crop
        self.rain = rain
        self.size = size
        self.fertilizer = fertilizer
        self.ratio = ratio

    def dispersion(self):
        pass

    def rain_day(self):
        pass

    def disease(self):
        pass


mister = Farm_Sim(15)
print(mister.simulation())