import aiml
import os
import sys
import gfortune
import subprocess
from subprocess import call


def scmd(command):


        testVar = "GGG"



        if command == "quit":
                return "HONK HONK HONK HONK HONK HONK HONK HONK"


        elif command == "fortune":
                output = gfortune.fortune()


        else:
                output = subprocess.check_output(command , shell =True)

        response = str(output)
        return response
