import random
from helpers import binomial_dist

"""
Suppose that the traffic light at the driveway leading 
into your school is red for 40% of its green-yellow-red cycle. 
During a 10-day period, what is the probability that
your school bus has to stop there on exactly 5 days?
"""

def simulate(prob_red, days):
    stops = list()
    for day in range(total_days):
        stop = 0
        if random.random() < prob_red:
            stop = 1
        else:
            stop = 0
        stops.append(stop)
    return stops


prob_red = 0.4
stopped_days = 5
total_days = 10
N = 1000000

stops_sim = 0
for i in range(N):
    stops = simulate(prob_red, total_days)
    # print(stops)
    if sum(stops) == stopped_days:
        stops_sim += 1

prob = stops_sim/float(N)
exact_prob = binomial_dist(prob_red, stopped_days, total_days)
print("Stopped {}, total days {}".format(stopped_days, total_days))
print("Simulated prob {} for N {}".format(prob, N))
print("Difference {}".format(abs(prob - exact_prob)))
