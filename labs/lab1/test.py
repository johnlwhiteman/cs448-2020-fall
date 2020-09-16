import json
import os
import re
import subprocess
import sys
from  pprint import pprint

class Result:
    def __init__(self):
        self.ret = None
        self.out = None
        self.err = None
        self.cmd = None

class Test:
    def __init__(self, test):
        self.c = test["c"]
        self.k = test["k"]
        self.p = test["p"]
        self.kpath = "k.txt"
        self.cpath = "c.txt"
        self.ppath = "p.txt"

def read(path):
    try:
        with open(path, "r",  encoding="utf-8") as fd:
            content = fd.read()
            return content.strip()
    except IOError as e:
        print("Read Failed: {0}".format(e))
        sys.exit(1)

def run(args):
    r = Result()
    r.cmd = "./vigenere {0}".format(args)
    print(r.cmd)
    p = subprocess.Popen(r.cmd,
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE,
        shell=True)
    stdout, stderr = p.communicate()
    r.out = stdout.decode("utf8").strip()
    r.err = stderr.decode("utf8").strip()
    r.ret = p.returncode
    if r.ret or re.search("Vigenère is a ", r.out):
        print(r.out)
        print(r.err)
        sys.exit(1)
    return r

def write(path, content):
    try:
        with open(path, "w", encoding="utf-8") as fd:
            fd.write(content)
    except IOError as e:
        print("Write Failed: {0}".format(e))
        sys.exit(1)

def testEncryption(t):
    r = run("-e -k '{0}' -i '{1}'".format(t.k, t.p))
    if r.out != t.c:
        print("Encryption Failed: {0}".format(r.cmd))
        print("{0} != {1}".format(r.out, t.c))
        sys.exit(1)
    print("Encryption Passed")

def testDecryption(t):
    r = run("-d -k '{0}' -i '{1}'".format(t.k, t.c))
    if r.out != t.p:
        print("Decryption Failed: {0}".format(r.cmd))
        print("{0} != {1}".format(r.out, t.p))
        sys.exit(1)
    print("Decryption Passed")

def testEncryptionFile(t):
    write(t.kpath, t.k)
    write(t.ppath, t.p)
    #write(t.cpath, t.c)
    r = run("-E -k '{0}' -i '{1}' -o '{2}'".format(
            t.kpath, t.ppath, t.cpath))
    os.unlink(t.kpath)
    os.unlink(t.ppath)
    if not os.path.exists(t.cpath):
        print("Encryption File Failed: No {0}".format(
            t.cpath))
        sys.exit(1)
    c = read(t.cpath)
    os.unlink(t.cpath)
    if t.c != c:
        print("Encryption File Failed: {0}".format(r.cmd))
        print("{0} != {1}".format(t.c, c))
        sys.exit(1)
    print("Encryption File Passed")

def testDecryptionFile(t):
    write(t.kpath, t.k)
    #write(t.ppath, t.p)
    write(t.cpath, t.c)
    r = run("-D -k '{0}' -i '{1}' -o '{2}'".format(
            t.kpath, t.cpath, t.ppath))
    os.unlink(t.kpath)
    os.unlink(t.cpath)
    if not os.path.exists(t.ppath):
        print("Decryption File Failed: No {0}".format(
            t.ppath))
        sys.exit(1)
    p = read(t.ppath)
    os.unlink(t.ppath)
    if t.p != p:
        print("Decryption File Failed: {0}".format(r.cmd))
        print("{0} != {1}".format(t.p, p))
        sys.exit(1)
    print("Decryption File Passed")

if __name__ == "__main__":
    try:
        with open("tests.json", "r",
                  encoding="utf-8") as fd:
            tests = json.load(fd)
            for test in tests:
                t = Test(test)
                testEncryption(t)
                testDecryption(t)
                testEncryptionFile(t)
                testDecryptionFile(t)
    except IOError as e:
        print("Abort: {0}".format(e))
        sys.exit(1)
