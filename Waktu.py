print ("K0ENVERSI WAKTU") //Andri alfiandi
print ("masukkan pilihan anda =")
print ("1. DETIK KE MENIT")
print ("2. DETIK KE JAM")
print ("3. MENIT KE DETIK")
print ("4. MENIT KE JAM")
print ("5. JAM KE DETIK")
print ("6. JAM KE MENIT")
pil = input("masukkan pilihan anda =")
if pil == '1' :
    detik = input("masukkan jumlah angka detik =")
    menit = float(detik)/60
    print ("jadi",float(detik),"detik",float(menit),"menit")
elif pil == '2' :
    detik = input("masukkan jumlah angka detik =")
    jam = float(detik)/3600
    print ("jadi",float(detik),"detik",float(jam),"jam")
elif pil == '3' :
    menit = input("masukkan jumlah angka menit =")
    detik = float(menit)*60
    print ("jadi",float(menit),"menit",float(detik),"detik")
elif pil == '4' :
    menit = input("masukkan jumlah angka menit =")
    jam = float(menit)/60
    print ("jadi",float(menit),"menit",float(jam),"jam")
elif pil == '5' :
    jam = input("masukkan jumlah angka jam =")
    menit = float(jam)*60
    print ("jadi",float(jam),"jam",float(menit),"menit")
elif pil == '6' :
    jam = input("masukkan jumlah angka jam =")
    detik = float(jam)*3600
    print ("jadi",float(jam),"jam",float(detik),"detik")
else :
    print ("salah input ki kodong")