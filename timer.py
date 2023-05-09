import time

def start():
    startTime = time.time()
    return startTime

def stop(startTime):
    stopTime = time.time()
    totalTime = stopTime - startTime
    return totalTime
