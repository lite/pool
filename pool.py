#!/usr/bin/env python

import os, sys
import shlex, subprocess
import re
import zipfile

def do_unzip(zfname):
    zfile = zipfile.ZipFile( zfname, "r" )
    zfile.printdir()
    for info in zfile.infolist():
        fname = info.filename
        data = zfile.read(fname)
        fout = open(fname, "w")
        fout.write(data)
        fout.close()

# download from "http://www.pool.com/Downloads/PoolDeletingDomainsList.zip"
def lastest_pool():
    cmd = "wget http://www.pool.com/Downloads/PoolDeletingDomainsList.zip -O tmp.zip"
    args = shlex.split(cmd)
    p = subprocess.Popen(args)
    os.waitpid(p.pid,0)
    return "tmp.zip"

# search
def do_search(fname, pat):
    f = open(fname,'r')
    for line in f.readlines():
        m = re.match(pat, line)
        if m: 
            print m.group(0) 
	
    f.close()

if __name__ == '__main__':
    
    if len(sys.argv) > 2:
        pat = sys.argv[2]
    else:
        #pat = r"^([a-z]{1,1})([a|e|i|o|u]{1,1})([a-z]{1,4})\.com(.+)$"
        pat = r"^([0-9a-z]{1,3})(\1)*\.(com|me)(.+)$"
        #pat = r"^([a-z]{1,5})(\1)*\.(com|me)(.+)$"

    if len(sys.argv) > 1:
        fname = sys.argv[1]
    else:
        print "downloading..."    
        zfname = lastest_pool()
        print "unzipping..."
        do_unzip(zfname)
        fname = "PoolDeletingDomainsList.txt"
    
    print "searching..."
    do_search(fname, pat)
    			
