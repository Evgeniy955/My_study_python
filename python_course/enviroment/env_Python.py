import os


os.environ['VarHello'] = "874587"

env = os.getenv("VarHello")
print(env)