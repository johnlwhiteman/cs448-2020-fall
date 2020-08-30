#!/usr/bin/env python3
import json
import os
import pprint
import subprocess
import sys

# http://www.bluetulip.org/2014/programs/primitive.html
# http://www.irongeek.com/diffie-hellman.php?

# g, p, a, b
tests = [
        ["5", "23", "4", "3", 18],
        ["3", "11", "4", "7", 5],
        ["7", "23", "4", "3", 16],
        ["5", "17", "2", "6", 4],
        ["13", "19", "8", "7", 17],
        ["7", "13", "2", "7", 10],
        ["3", "7", "2", "7", 2],
        ["14", "29", "4", "3", 25],
        ["8", "29", "5", "5", 26],
        ["11", "13", "5", "8", 3]]
results = []
exePath = "./dh"
logPath = "./results.json"

if os.path.isfile(logPath):
    os.unlink(logPath)

if os.system("make"):
    print("Abort: Make failed")
    sys.exit(1)

if not os.path.isfile(exePath):
    print("Abort: Can't find {0}".format(exePath))
    sys.exit(1)

failedCnt = 0
for t in tests:
    cmd = ["./dh", t[0], t[1], t[2], t[3]]
    print("Test:   {0}".format(t))
    proc = subprocess.run(cmd, 
                          stdout=subprocess.PIPE, 
                          stderr=subprocess.PIPE)
    tOutput = proc.stdout.decode("utf-8").strip()
    if 0 != proc.returncode:
        print("Result: {0}".format(tOutput))
        print("Test aborted!")
        sys.exit(1)
    jOutput = json.loads(tOutput) 
    jOutput["score"] = "Passed"
    jOutput["expectedSK"] = t[4] 
    if jOutput["aSK"] != jOutput["bSK"]:
        jOutput["score"] = "Failed: Secret keys don't match"
    elif jOutput["aSK"] != t[4]:
        jOutput["score"] = \
        "Failed: {0} != {1}".format(jOutput["aSK"], t[4])
        failedCnt += 1
        print("Failed: {0}".format(t))
    results.append(jOutput)
with open(logPath, "w", encoding="utf-8") as fd:
    json.dump(results, fd, indent=4, sort_keys=True) 
testsCnt = len(tests)
print("Tests {0}, Passed: {1}, Failed: {2}".format(
      testsCnt, testsCnt - failedCnt, failedCnt))
print("Script completed. See {0} for results".format(logPath))
