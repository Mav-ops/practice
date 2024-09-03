class HotelRoomCalc(object):
    'Hotel room rate calculator'

    def __init__(self,rt,sales=0.085,rm=0.1):
        """ HotelRoomCalc default arguments:
            sales tax==8.5% and room tax==10%"""
        self.salesTax=sales
        self.roomTax=rm
        self.roomRate=rt

    def calcTotal(self,days=1):
        'Calculate total;default to daily rate'
        daily=round((self.roomRate*(1+self.roomTax+self.salesTax)),2)
        return float(days)*daily

sfo=HotelRoomCalc(299)
print('SFO ',sfo.calcTotal())
print('SFO ',sfo.calcTotal(2))

sea=HotelRoomCalc(189,0.086,0.058)
print('SEA ',sea.calcTotal())
print('SEA ',sea.calcTotal(4))

wasWkDay=HotelRoomCalc(169,0.045,0.02)
wasWkEnd=HotelRoomCalc(119,0.045,0.02)
print('WAS 7days ',wasWkEnd.calcTotal()+wasWkDay.calcTotal(5))