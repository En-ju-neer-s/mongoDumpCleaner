import json
import re
import os

directoryName = 'test'
nameCleanedFoler = 'cleanedJson'

directory = os.fsencode(directoryName)
# loop through all the files
for file in os.listdir(directory):
    filename = os.fsdecode(file)  # get files name
    if filename.endswith(".json"):
        print(filename)  # see preogress
        # go to file name
        with open('./' + directoryName + "/" + filename, "r", encoding="utf8") as data_in:

            cleanedStringJson = ''  # starting string
            # REGEX
            for line in data_in:

                cleanedBindata = re.sub(r'BinData\S\d\S\s(\S+)\)',
                                        r'\1',
                                        line)

                # convert the TenGen JSON to Strict JSON
                jsondataString = re.sub(r'\:\s*\S+\s*\(\s*(\S+)\s*\)',
                                        r':\1',
                                        cleanedBindata)

                cleanedStringJson = cleanedStringJson + jsondataString
            print(len(cleanedStringJson))
            # cleanedStringJson = cleanedStringJson + ']'

        if os.path.exists(nameCleanedFoler) == False:  # check if this folder exist other wise make one
            os.mkdir(nameCleanedFoler)
        # Write data to a will
        with open('./' + nameCleanedFoler + '/' + os.path.splitext(filename)[0] + 'Cleaned.json', 'w') as json_file:
            json_file.write(cleanedStringJson)
    else:
        print("NOT JSON")
        continue
