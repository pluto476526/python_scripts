import psutil

def check_ram_usage():
    # Get virtual memory statistics
    memory_info = psutil.virtual_memory()
    swap_info = psutil.swap_memory()

    # Calculate memory usage details
    total_memory = memory_info.total / (2**30)  # Convert bytes to GB
    used_memory = memory_info.used / (2**30)    # Convert bytes to GB
    free_memory = memory_info.available / (2**30)  # Convert bytes to GB
    percent_used = memory_info.percent

    # Calculate swap memory usage details
    total_swap = swap_info.total / (2**30)  # Convert bytes to GB
    used_swap = swap_info.used / (2**30)    # Convert bytes to GB
    free_swap = swap_info.free / (2**30)    # Convert bytes to GB
    percent_swap_used = swap_info.percent

    # Print RAM usage statistics
    print("RAM Usage Statistics:")
    print(f"Total Memory: {total_memory:.2f} GB")
    print(f"Used Memory: {used_memory:.2f} GB")
    print(f"Free Memory: {free_memory:.2f} GB")
    print(f"Memory Used Percentage: {percent_used:.2f}%")
    
    # Print Swap usage statistics
    print("\nSwap Memory Statistics:")
    print(f"Total Swap: {total_swap:.2f} GB")
    print(f"Used Swap: {used_swap:.2f} GB")
    print(f"Free Swap: {free_swap:.2f} GB")
    print(f"Swap Used Percentage: {percent_swap_used:.2f}%")

# Example usage
check_ram_usage()