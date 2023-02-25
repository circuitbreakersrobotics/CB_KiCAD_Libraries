import shutil
import os
import json

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



def Update3DLinks():
    # Define the directory to search for .kicad_mod files in
    #dir_to_search = "pcm/footprints"
    dir_to_search = destFootprint
    

    # Walk through the directory and its subdirectories
    for root, dirs, files in os.walk(dir_to_search):
        # Loop through all files in the current directory
        for file_name in files:
            # Check if the file is a .kicad_mod file
            if file_name.endswith(".kicad_mod"):
                # Construct the full path to the file
                file_path = os.path.join(root, file_name)

                # Open the file in read mode
                with open(file_path, "r") as file:
                    # Read the file contents into a string variable
                    file_contents = file.read()

                # Replace all occurrences of "{KICAD6_3RD_PARTY}" with "{KICAD7_3RD_PARTY}"
                new_contents = file_contents.replace("{KICAD6_3RD_PARTY}", "{KICAD7_3RD_PARTY}")

                # Open the file in write mode and write the new contents to it
                with open(file_path, "w") as file:
                    file.write(new_contents)

#***********************************************************************************************



def updatePackageVersion(version):

    # Open the JSON file in read mode
    with open(srcJson, "r") as file:
        # Load the JSON data into a Python dictionary
        data = json.load(file)

    # Update the value of the "version" key
    data["versions"][0]["version"] = version


    url = data["versions"][0]["download_url"] 

    # Change downlode URL.

    #url = "https://github.com/circuitbreakersrobotics/CB_KiCAD_Libraries/releases/download/v0.0.2/CB_KiCAD_Libraries_v0.0.2.zip"

    # Split the URL string by "/"
    url_parts = url.split("/")
    # Split the CB_KiCAD_Libraries_v0.0.2. string by "_"
    file_name = url_parts[8].split("_")


    # Replace the text between the 7th and 8th "/" characters
    url_parts[7] = "v" + version

    file_name[3] =  "v" + version + ".zip"

    # Join the file name back into a single string
    url_parts[8] = "_".join(file_name)

    # Join the URL parts back into a single string
    new_url = "/".join(url_parts)

    print(new_url)


    data["versions"][0]["download_url"]  = new_url


    # Open the JSON file in write mode
    with open(srcJson, "w") as file:
        # Write the updated JSON data to the file
        file.write(json.dumps(data, indent=1))
        #json.dump(data, file)

#***********************************************************************************************



def updateKiCADVersionInMetadata(kicad_version):

        # Open the JSON file in read mode
    with open(destJson, "r") as file:
        # Load the JSON data into a Python dictionary
        data = json.load(file)

    # Update the value of the "version" key
    data["versions"][0]["kicad_version"] = kicad_version

    # Open the JSON file in write mode
    with open(destJson, "w") as file:
        # Write the updated JSON data to the file
        file.write(json.dumps(data, indent=1))
        #json.dump(data, file)

#***********************************************************************************************



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

       
        pack_version = "0.1"
        pack_version = input("Enter the version number (In to JSON file) = ")
        updatePackageVersion(pack_version)
        destination = shutil.copyfile(srcJson, destJson) 

        kicad_version_in = "7"
        kicad_version_in = input("Enter the version number (In to JSON file) = ")
        updateKiCADVersionInMetadata(kicad_version_in)


        print("")

    else:
        print("Discarded **************** ")
    print("")



    UserInput = input("Do you want to Change the 3D model pathes (y / n) = ") 
    if(UserInput == 'y'):
        Update3DLinks()
    else:
        print("Discarded **************** ")
    print("")



    UserInput = input("Enter anything to Exit the programe :) = ") 





