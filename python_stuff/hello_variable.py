#!/usr/bin/python3

hvar = "Hello World!"

print(hvar)

print("Non-format method: " + hvar)

print("Other non-format method: %s" % (hvar))

print("Format method: {0}".format(hvar))

print("{:.4}".format(hvar))

print("{:.6}".format( 14/3))

print("{:.7f}".format( 14/3))
