import requests 
import random 
from itertools import count 


for i in count(0):
    try:
         x_rand = random.randrange(20,30)
         y_rand = random.randrange(20,30)
         z_rand = random.randrange(20,30) 
         data_swarm = {"kornbot380@hotmail.com":{"Smart_bots":{"motion_data":[x_rand,y_rand,z_rand,90,45,90]}}}
         res = requests.post("https://roboreactor.com/Navigation_mesh_input",json=data_swarm) 
         res.json() 
    except:
         print("Error post request server")



