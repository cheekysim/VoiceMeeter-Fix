import psutil

process = psutil.Process(4116) # Get audiodg.exe process
process.cpu_affinity(cpus=[2]) # Set CPU Affinity to CPU 2
process.nice(psutil.HIGH_PRIORITY_CLASS) # Set CPU Proiroty to High
