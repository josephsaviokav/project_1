import random
from tqdm import tqdm
def pi(samples):
    inside_circle=0
    x,y=0,0
    for _ in tqdm(range(samples)):
        x=random.random()
        y=random.random()
        if x**2+y**2<=1:
            inside_circle+=1
    pie=(inside_circle/samples)*4
    return pie


print(pi(100000000))
