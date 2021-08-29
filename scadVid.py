import os 

def isComment(line):
    if( "//" in line ):
        return True
    else:
        return False

def getNumberFromComment(line):
    dat = line.split("//")
    dat = dat[len(dat)-1]
    dat = int(dat)
    return dat

def takePicOfScad(name, num, scadOutputFile):
    openScadDir = "%s%s" % (os.getcwd(), '/')
    #print( openScadDir )
    outDir = 'pics/'
    outputPicture = '%s%s%s%s%s' % (outDir, name, '_', num, '.png')
    #print( outputPicture )
    command = '%s%s%s%s%s%s' % ('sudo ', 'openscad', ' --o ', outputPicture, ' --render --camera 0,0,0,45,0,135,40  --imgsize 1920,1080 --view axes ', scadOutputFile)
    #print( command )
    os.system(command)


inputFile = 'cube.scad'
scadFile = open( inputFile, 'r' )

outputDir = 'outputData/'

i=0
for i in range(6):
    results = list()
    #print (i)
    scadFile.seek(0)
    for line in scadFile:
        if ( isComment( line ) ):
            if( getNumberFromComment( line ) <= i ):
                results.append(line)
    
    outputFileName = '%s%s%s%s%s%s' % (outputDir, inputFile.split('.')[0], '_', i, ".", inputFile.split('.')[1] )
    outputFile = open(outputFileName, "w")
    #print( "/-->", outputFileName )
    for elem in results:
        outputFile.write(elem)
    outputFile.close()

    takePicOfScad(inputFile.split('.')[0], i, outputFileName)