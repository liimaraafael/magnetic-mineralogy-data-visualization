from constants import list_his, list_irm, list_name
from functions import plot

for his, irm, name in zip(list_his, list_irm, list_name):
    plot(his, irm, name)
