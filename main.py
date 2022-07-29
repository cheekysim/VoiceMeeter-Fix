import psutil

pid = [proc.pid for proc in psutil.process_iter() if "audiodg" in proc.name()]
process = psutil.Process(pid[0]) # Get audiodg.exe process
process.cpu_affinity(cpus=[2]) # Set CPU Affinity to CPU 2
process.nice(psutil.HIGH_PRIORITY_CLASS) # Set CPU Proiroty to High