

#s =[('SEV TAMATAR',), ('MOONG DAL HALWA',), ('KADAHI PANEER',), ('PANEER TIKKA MASALA',), ('DAL TADKA',), ('PLAIN PARATHA',), ('LACHCHA PARATHA',), ('TAWA ROTI',), ('MIX VEG',), ('PINDI CHOLE',), ('JEERA RICE',), ('ALOO KI SABZI',), ('BUTTER KHICHADI',), ('BIRYANI',), ('IDLI SAMBHAR',), ('MASALA DOSA',), ('POHA',), ('BUTTER SANDWICH',), ('AALOO PARATHA ',), ('FRIED IDLI',), ('GULAB JAMUN',), ('RASGULLA',), ('FRUIT CUSTARD',), ('AAM RAS',)]
class rep():

    def __init__(self, s):
        self.s = s
        populate(self.s)

    def populate(s):
        l=[]
        for ei in s:
            e = str(ei)
            new = e.replace("(\'", "")
            new = new.replace("\',)", "")
            l.append(new)
        return print(l)
 
    def show_s(s):
        print(s)
