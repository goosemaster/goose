#!/usr/bin/env python


import random


def honkGen():
        "generate random honks"

        honks = ['HOOONK', 'HONK', 'HooOoOoOonk', 'HOOONK', 'HoOoOonK', 'HOOOOOOOONK', 'HONK', 'HOOONK' , 'HOOOOOOONK' , 'HOOOONK' , 'HONK' ]

        RH = random.randint(5,12)
        randmessage = ' '.join(random.choice(honks) for _ in range(RH))
        message = "" + randmessage
        print message



honkGen()
