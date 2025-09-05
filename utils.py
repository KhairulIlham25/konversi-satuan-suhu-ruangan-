def konversi_suhu(nilai, dari, ke):
    #normalisasi satuan agar tidak case sensiitive
    dari = dari.lower()
    ke = ke.lower()
    
    #validasi satuan
    if dari not in ["c", "f", "k"] or ke not in ["c", "f", "k"]:
        return "Satuan tidak valid. Gunakan 'C', 'F', atau 'K'."
    
    #validasi nilai kelvin tidak boleh negatif
    if dari == "k" and nilai < 0:
        return "Nilai suhu dalam Kelvin tidak boleh negatif."
    
    #konversii awal ke celcius sebagai dasar
    if dari == "c":
        celcius = nilai
    elif dari == "f":
        celcius = (nilai - 32) * 5/9
    elif dari == "k":
        celcius = nilai - 273.15

    #konversi dari celcius ke satuan tujuan
    if ke == "c":
        hasil = celcius
    elif ke == "f":
        hasil = (celcius * 9/5) + 32
    elif ke == "k":
        hasil = celcius + 273.15

    #valiidasi hasil kelvin tidak boleh negatif
    if ke == "k" and hasil < 0:
        return "Hasil konversi dalam Kelvin tidak boleh negatif."
    
    return hasil