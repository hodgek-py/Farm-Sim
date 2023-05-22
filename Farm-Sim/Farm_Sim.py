from hmac import new
import random

class Farm_Sim:
    def __init__(self, time, period = 'D',counter = 0):
        self.period = period
        self.time = time
        self.counter = counter

    def simulation(self):
        sim = Sim_Var(2,1,3,2)
        print(sim.final_output())
        while self.time > self.counter:
            print(self.counter)
            self.counter += 1

class Sim_Var:
    def __init__(self,crop,rain,size,fertilizer,ratio = (1/3),output = 0):
        self.crop = crop
        self.rain = rain
        self.size = size
        self.fertilizer = fertilizer
        self.ratio = ratio
        self.seeds = (self.ratio * (self.size * 12)) * (self.ratio * (self.size * 12))
        self.output = output

    def final_output(self):
        for x in range(0,int(self.seeds)):
            self.output += random.randint(20,25)

        self.output = self.output - self.seeds
        return self.output

    def rain_day(self):
        pass

    def disease(self):
        pass


mister = Farm_Sim(15)
print(mister.simulation())