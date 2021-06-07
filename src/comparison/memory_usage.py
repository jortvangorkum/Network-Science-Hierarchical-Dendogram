from memory_profiler import memory_usage

def determine_memory_usage(f):
    (mem_usage, ret_val) = memory_usage(f, retval=True)
    return (ret_val, max(mem_usage))