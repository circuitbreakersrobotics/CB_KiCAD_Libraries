import shutil
import os

print(" packMan V 5.0 ")

searchWord = "CB_"
addWord = "PCM_"
#outputDitectory = "RemovedBackup/output/"
#outputDitectory = "../RemovedBackup/output/"
outputDitectory = "pcm/symbols/"
symbolDir       = "pcm/symbols"


srcFootprint     = "footprints"
srcSymbols       = "symbols"
srcModels        = "3dmodels"
srcResources     = "resources"
srcJson          = "metadata.json"


destFootprint    = "pcm/footprints"
destSymbols      = "pcm/symbols"
destModels       = "pcm/3dmodels"
destResources    = "pcm/resources"
destJson         = "pcm/metadata.json"



def changeLibParthToPCM():
    #..\Landuse
    sWordLen = len(searchWord)


    #listFile = open("pythonscripts/LibList.txt", "r")
    listFile = []

    for symFilse in os.listdir("symbols/"):
        if symFilse.endswith(".kicad_sym"):
            #print(symFilse)
            listFile.append(symFilse)

    print(listFile)
    count = 0


    for x in listFile:
        #fileName = "CB_Resistors.kicad_sym"
        #fileName = x[0:-1]
        fileName = x
        if x[0] == "#":
            continue
        
        #print("Opening File - ",  fileName)
        print(" -------------  ",fileName,"  ----------- ")
        file = open("symbols/"+fileName, "r") #Opening file
        fileData = file.read()
        fileDataLength = len(fileData)
        print(fileDataLength)
            
        #searchWord = "Arduino_Pro"
        lnCount = 1
        errorFlag_1 = True
        file.seek(0,0)
        for i in range(fileDataLength):
            #print(fileData[i])
            #print("******************")
            
            if fileData[i:i+sWordLen] == searchWord:
                count = count + 1
                for j in range(i , fileDataLength):
                    errorFlag_1 = False
                    if fileData[j] == '"':
                        print(count, "- ",lnCount, " ",fileData[i-1:j+1])
                        break

            if fileData[i] == "\n":
                lnCount = lnCount +1
                    
        file.close()
            
        if errorFlag_1:
            print("ERROE-01 - No need of changers") 
        print("Count need to change = ", count)
        print("")



    ###############################################################################################
    #//////////////////////////////////////////////////////////////////////////////////////////////
    ###############################################################################################



    UserInput = input("Accept changes (y -yes / n -No to Discard) = ") 

    if(UserInput == 'y'):
        print("OK **************** ")
        os.mkdir(symbolDir)
        #listFile.seek(0)
        for x in listFile:
            #fileName = "CB_Resistors.kicad_sym"
            #fileName = x[0:-1]
            fileName = x
            if x[0] == "#":
                continue
            
            #print("Opening File - ",  fileName)
            print(" -------------  ",fileName,"  ----------- ")
            file = open("symbols/"+fileName, "r") #Opening file
            fileData = file.read()
            fileDataLength = len(fileData)
            #newFileData = []
            newFileData = ""
            print(fileDataLength)
                
            #searchWord = "Arduino_Pro"
            lnCount = 1
            errorFlag_1 = True
            file.seek(0,0)
            for i in range(fileDataLength):
                #print(fileData[i])
                #print("******************")
                
                if fileData[i:i+sWordLen] == searchWord:
                    count = count + 1
                    #newFileData.append(addWord)
                    #newFileData.append(fileData[i])
                    newFileData = newFileData + addWord +fileData[i]
                    for j in range(i , fileDataLength):
                        errorFlag_1 = False
                        if fileData[j] == '"':
                            print(count, "- ",lnCount, " ",fileData[i-1:j+1])
                            break
                else:
                    #newFileData.append(fileData[i])
                    newFileData = newFileData + fileData[i]

                if fileData[i] == "\n":
                    lnCount = lnCount +1
            #print(newFileData)
            fileName = outputDitectory + fileName  
            outputFile = open(fileName, "w") #Opening file
            outputFile.write(newFileData)
            outputFile.close()

            file.close()
                
            if errorFlag_1:
                print("ERROE-01 - No changers") 
            print("Count changed = ", count)
            print("")



    elif(UserInput == 'n'):
        print("Discarded **************** ")
    else:
        print("Discarded **************** ")
    print("")

    UserInput = input("Do you want to copy other files which need to create a PCM package (y / n) = ") 

    if(UserInput == 'y'):

        print("")
        print("")
        print("Copying Footprint files ........................................")
        destination = shutil.copytree(srcFootprint, destFootprint) 

        print("")
        print("Copying 3D Model files ......{ this might take some time }......")
        destination = shutil.copytree(srcModels, destModels) 

        print("")
        print("Copying metadata and resources .................................")
        destination = shutil.copytree(srcResources, destResources) 

        #outputFile = open(destJson, "w") #Opening file
        #outputFile.write(newFileData)
        #outputFile.close()

        destination = shutil.copyfile(srcJson, destJson) 

        print("")

    else:
        print("Discarded **************** ")
    print("")


    UserInput = input("Enter anything to Exit the programe :) = ") 

def Update3DLinks():

    
    

