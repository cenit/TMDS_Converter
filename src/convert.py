#!/usr/bin/env python

from nptdms import TdmsFile

filename = "log1.tdms"
tdms_file = TdmsFile(filename)
print("Analysing", filename)
root_object = tdms_file.object()
# Iterate over all items in the root properties and print them
for name, value in root_object.properties.items():
    print("{0}: {1}".format(name, value))

df = tdms_file.as_dataframe()

df.columns = df.columns.str.replace('/', '')
df.columns = df.columns.str.replace('\'\'', '-')
df.columns = df.columns.str.replace('\'', '')

print(df.to_string())
