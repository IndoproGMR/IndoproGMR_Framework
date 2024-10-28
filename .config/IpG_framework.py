# vim:fileencoding=utf-8:foldmethod=marker

# System {{{


import sys

argumentPass = sys.argv
argvLen = len(argumentPass)

# INFO tamplate
dataRouter = """
# userCode {{{
# Your Code Here
# }}}
"""

dataModel = """
# userCode {{{
# Your Code Here
# }}}
"""

dataView = """
# userCode {{{
# Your Code Here
# }}}
"""

command = """# command

# untuk memudahkan bisa menggunakan Gui
gui

# membuat file 
makeFile <type> "Nama File"

type: router
      model
      view

# update Framework
update

# force update
update --something-has-gone-wrong
"""

if argvLen < 2:
    print(command)
    exit()

if argumentPass[1] == "help":
    print(command)
    exit()

# swicth
if argvLen > 2:
    print("WIP")
    exit()


def makeFileTamplate():
    if argvLen < 4:
        print("setting belum dimasukan dengan benar")
        exit()


if argumentPass[1] == "makeFile":

    typeFile = argumentPass[2]
    namaFile = argumentPass[3]
    namaFile = f"{namaFile}.py"
    print(f"membuat file {typeFile} dengan nama {namaFile}")


# TODO 
# membuat makeFile
# Update
# gui
# zip untuk update


# membuat file untuk Router
# membuat file untuk Model
# membuat file untuk view


# membaca .FWsystem
# Zip dari .FWsystem
# download dari github
# unzip ke "tmp/.update"
# cek .FWsystem pada zip update dan .FWsystem original apakah perlu update
# membaca file system Code untuk di update
# lalu replace code yang di dalam system code

# }}}
