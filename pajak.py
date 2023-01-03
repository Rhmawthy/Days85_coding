'''program yang dapat mengetahui berapa uang bersih yang 
didapatkan dari hasil penjualan tanah setelah dipotong pajak 
dengan ketentuan:
1. Harga Jual Permeter adalah Rp 300.000
2. Jika total harga jual 50 jt keatas maka dikenakan pajak 3%
3. Jika Total harga jual 100 jt keatas maka dikenakan pajak 5%
4. Dibawah 50jt maka dikenakan pajak 1%.
5. Luas tanah diinput menggunakan fungsi input pada python'''

jumlah = int(input("jumlah permeter tanah : "))

total = jumlah * 300000

if total >= 100000000:
	persen_pertama = total * 5 / 100 
	pajak1 = total - persen_pertama
	print ("anda di kenakan pajak 5 %, total pembayaran",pajak1)

elif total >= 50000000:
	persen_kedua = total * 3 / 100 
	pajak2 = total - persen_pertama
	print ("anda di kenakan pajak 3%, total pembayaran",pajak2)


elif total <= 50000000:
	persen_ketiga= total * 1/ 100 
	pajak3 = total - persen_ketiga
	print ("anda di kenakan pajak 1%, total pembayaran",pajak3)
	