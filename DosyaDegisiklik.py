with open("ogrenci.txt", "r+") as dosya:
    """data=dosya.read()
    dosya.seek(0)
    data="Prof.Dr:Mehmet Akbaba\n"+data
    dosya.write(data)"""
    data = dosya.readlines()
    data.insert(3, "Bilimtey Kulubu\n")
    dosya.seek(0)
    dosya.writelines(data)
