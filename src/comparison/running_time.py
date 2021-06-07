from time import monotonic
from datetime import timedelta as td

def determine_running_time(alg):
    start_time = monotonic()
    model = alg()
    end_time = monotonic()
    duration = td(seconds=end_time - start_time)
    return (model, duration)