from memory_profiler import memory_usage

def determine_memory_usage(f):
    (mem_usage, ret_val) = memory_usage(f, interval=0.0001, retval=True)
    return (ret_val, max(mem_usage) - min(mem_usage))