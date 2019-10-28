import json
import re
import os

directoryName = 'data'
nameCleanedFoler = 'cleanedJson'

isArray = False

directory = os.fsencode(directoryName)
# loop through all the files
for file in os.listdir(directory):
    filename = os.fsdecode(file)  # get files name
    if filename.endswith(".json"):
        print(filename)  # see preogress
        # go to file name
        with open('./' + directoryName + "/" + filename, "r", encoding="utf8") as data_in:
            linesAmount = len(data_in.readlines())
            print('Total: ', end="")
            print(linesAmount)

        with open('./' + directoryName + "/" + filename, "r", encoding="utf8") as data_in:
            cleanedStringJson = ''  # starting string
            linesCount = 0
            # REGEX
            for line in data_in:
                newLine = ''  # starting string

                if '[' in line:
                    isArray = True

                if ']' in line:
                    line = ''
                    isArray = False

                if isArray:
                    newLine = ''

                else:
                    cleanedBindata = re.sub(r'BinData\S\d\S\s(\S+)\)',
                                            r'\1',
                                            line)
                    # convert the TenGen JSON to Strict JSON
                    jsondataString = re.sub(r'\:\s*\S+\s*\(\s*(\S+)\s*\)',
                                            r':\1',
                                            cleanedBindata)
                    # remove any /r or /n breaks
                    removeLinebreaks = re.sub(r'\\r\\n|\\r|\\n',
                                              r'',
                                              jsondataString)
                    newLine = removeLinebreaks

                cleanedStringJson = cleanedStringJson + newLine

                linesCount += 1
                progres = (linesCount/linesAmount) * 100
                print("Progres: "+str(round(progres))+"%  Lines: " +
                      str(linesCount), end="\r", flush=True)

            print(len(cleanedStringJson))
            # cleanedStringJson = cleanedStringJson + ']'

        # check if this folder exist other wise make one
        if os.path.exists(nameCleanedFoler) == False:
            os.mkdir(nameCleanedFoler)
        # Write data to a will
        with open('./' + nameCleanedFoler + '/' + os.path.splitext(filename)[0] + 'Cleaned.json', 'w') as json_file:
            json_file.write(cleanedStringJson)
    else:
        print("NOT JSON")
        continue
