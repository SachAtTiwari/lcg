import math
import time

class Random():

   def __init__(self, seed = time.time(), a = 1103515245, c = 12345 , mod = math.pow(2, 31)):
      '''
        intialize required variable for LCG(linear congruential genrator)
      '''
      self.seed = seed 
      self.a = a
      self.c = c
      self.mod = mod

 
   def __randInt(self):
     '''
       main function to genrate seed for random variable
     '''
     self.seed = int((self.a * self.seed + self.c)) % self.mod
     yield self.seed

   def __getLcg(self): 
     '''
       get seed value and return division 
     '''
     retval = 0
     for i in self.__randInt():
        retval = i / self.mod 
     return retval
 
   def __randRange(self, min, max):
     '''
       calculate random number in b/w the given range using LCG 
     '''
     lcg = self.__getLcg()
     retval = min + lcg * (max - min) 
     return retval

   def randIntRange(self, min, max):
     '''
       main function to get random value in range 
     '''
     return int(abs(self.__randRange(min, max)))
  

if __name__ == "__main__":
   '''
     Test function to get add biasing in random number 
   '''
   test = Random()
   #Create variable to count greater and small
   great, small = 0, 0
   #Create list store random numbers
   randList = []

   #high = (73 * max)/100
   #Assuming max 100 and range from 0 to 10
   high = (73 * 100)/100

   ##Add higher biased number in randList
   while len(randList) != high:

      #73% times val should be > max/2
      val = test.randIntRange(5, 10)
      randList.append(val) 
      great += 1
      #print "greater", val, great
      continue
     

   ##Add lower biased number in randList
   while len(randList) != 100:

      val = test.randIntRange(0, 5)
      randList.append(val) 
      small += 1
      #print "smaller", val, small
      continue

   ##Desired output
   print randList #, len(randList)

