#!/home/angus/bin/python3.4

import sys, os, os.path, shutil

inDir = sys.argv[1]
outDir = sys.argv[2]

def lcFirst (inStr):
    if (inStr.isupper()):
        return inStr.lower()
    else:
        return inStr[0].lower() + inStr[1:]

def lcDir(inStr):
    item = inStr.split('/')
    loweritem = []
    for (k) in item:
        loweritem.append(lcFirst(k))
    return '/'.join(loweritem)

def lcPack (inStr):
    item = inStr.split('.')
    loweritem = []
    for (k) in item:
        loweritem.append(lcFirst(k))
    return 'edu.nyu.' + '.'.join(loweritem)

def lcImport (inStr):
    item = inStr.split('.')
    loweritem = []
    for (k) in item:
        if (';' == k[-2]):
            loweritem.append(k)
        else:
            loweritem.append(lcFirst(k))
    return 'edu.nyu.' + '.'.join(loweritem)


for root, subdirs, files in os.walk(inDir):
    for subdir in subdirs:
        print(subdir)
        if ('AceJet' == subdir):
            newsubdir = os.path.join(outDir, 'edu/nyu/jet/', os.path.relpath(lcDir(root), inDir), lcFirst(subdir))
        else:
            newsubdir = os.path.join(outDir, 'edu/nyu/', os.path.relpath(lcDir(root), inDir), lcFirst(subdir))
        try:
            os.mkdir(newsubdir)
        except IOError:
            print("Can't create directory " + newsubdir)
    for filename in files:
        filepath = os.path.join(root, filename)
        print (filepath)
        if ('AceJet' == os.path.basename(root)):
            newfilepath = os.path.join(outDir, 'edu/nyu/jet/', os.path.relpath(lcDir(root), inDir), filename)
        else:
            newfilepath = os.path.join(outDir, 'edu/nyu/', os.path.relpath(lcDir(root), inDir), filename)
        
        if ('.java' != filepath[-5:]):
            # just copy the file
            print ('  copy ' + newfilepath)
            try:
                shutil.copy2(filepath, newfilepath)
            except IOError:
                print("Can't copy to " + newfilepath)
        else:
            f = open(filepath, "r")
            t = "nonempty"
            hasPack = False
            ft = ''
            while (t != ""):
                t = f.readline()
                if ('package Jet' == t[0:11]):
                    hasPack = True;
#                    print('lcPack(' + t[8:] + ')')
                    newPack = 'package ' + lcPack(t[8:])
                    ft += newPack
                    print ('newPack = ' + newPack)
                elif ('package AceJet' == t[0:14]):
                    hasPack = True;
#                    print('lcPack(Jet.' + t[8:] + ')')
                    newPack = 'package ' + lcPack('Jet.' + t[8:])
                    ft += newPack
                    print ('newPack = ' + newPack)
                elif ('import Jet' == t[:10]):
                    newImp = 'import ' + lcImport(t[7:])
                    ft += newImp
                    print('newImp = ' + newImp)
                elif ('import AceJet' == t[:13]):
#                    print('lcImport(Jet.' + t[7:] + ')')
                    newImp = 'import ' + lcImport('Jet.' + t[7:])
                    ft += newImp
                    print('newImp = ' + newImp)
                elif ('package ' == t[:8]):
                    print ('unknown ' + t)
                else:
                    ft += t
            f.close
            foh = open(newfilepath, 'w')
            foh.write(ft)
            foh.close
            '''
            if (not hasPack):
                print ('ALERT: No package found!')
            '''
