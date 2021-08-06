from collections import namedtuple


class CarBrands:
    def __init__(self):
        """named tuple for the parking ticket informations"""
        self.park_tk = namedtuple('park_tk','Summons_Number Plate_ID Registration_State Plate_Type Issue_Date Violation_Code Vehicle_Body_Type Vehicle_Make Violation_Description')
        self.violations_brand = {}
    
    def brands(self,f_name):
        """lazy iterator to iterate parking ticket informations"""
        with open(f_name, encoding='utf8', errors='ignore') as f:
            for line in f:
                yield line.strip('\n')
    
    def find_violations(self):
        """find the violations made by the car brands"""
        info = namedtuple('park_tk', ['tickets'])
        files = "nyc_parking_tickets_extract-1.csv"
        i=0
        for brand in self.brands(files):
            tickets = brand.split(",")
            if(i==0):
                pass
            elif(i==1):
                s=self.park_tk(tickets[0],tickets[1],tickets[2],tickets[3],tickets[4],tickets[5],tickets[6],tickets[7],tickets[8])
                t = info(s)
            else:
                s=self.park_tk(tickets[0],tickets[1],tickets[2],tickets[3],tickets[4],tickets[5],tickets[6],tickets[7],tickets[8])
                t += info(s)
            i+=1

        for prof in t:
            bg = prof.Vehicle_Make
            if bg not in self.violations_brand:
                self.violations_brand[bg]=0
            else:
                self.violations_brand[bg]+=1
        
        
        for i in self.violations_brand:
            print(i,self.violations_brand[i])
            
    def most_violated(self):
        """most violated car brand"""
        prev_count = 0
        for i in self.violations_brand:
            count = self.violations_brand[i]
            if count>prev_count:
                prev_count = count
                most_violated_brand = i
        print("\nmost violated car brand:",most_violated_brand)


c = CarBrands()

c.find_violations()
c.most_violated()
