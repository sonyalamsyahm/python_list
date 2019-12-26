
# Metode Pada List Di Python
### Definisi
>__*List*__ adalah struktur data dalam python yang merupakan urutan element yang dapat diubah atau dimodifikasi atau __mutable__. Setiap element yang ada dalam list tersebut disebut dengan __item__. Ciri-ciri atau tanda suatu data sebagai List adalah List didefinisikan diantara tanda kurung `[]` . Contohnya list `hewan = ['Ayam', 'Angsa', 'Marmut']`

>__Indexing__  pada List:  Pada List, terdapat yang namanya ___index___, dimana index merupakan angka yang menunjukkan ruang atau urutan yang dipakai untuk menentukkan posisi dari suatu item pada list yang dimulai dari angka 0. Contoh pada `list hewan` diatas, index ke-0 menunjuk terhadap `'Ayam'`.  Untuk mengakses item pada list kita bisa menggunakan cara berikut: `NamaList[index ke-n]`, contohnya `print(hewan[1])`akan mencetak `'Angsa'`.

## Daftar Metode Pada List

 - `append()`
 - `extend()`
 - `insert()`
 - `remove()`
 - `index()`
 - `Count()`
 - `pop()`
 - `reverse()`
 - `sort()`
 - `copy()`
 - `clear()`
 - `any()`
 - `all()`
 - `ascii()`
 - `bool()`
 - `enumerate()`
 - `filter()`
 - `iter()`
 - `list() Function`
 - `len()`
 - `max()`
 - `min()`
 - `map()`
 - `reversed()`
 - `slice()`
 - `sorted()`
 - `sum()`
 - `zip()`
 
## `Append()`
Metode `append()` merupakan salah satu metode yang digunakan untuk menambahkan item ke daftar list. Metode ini biasa digunakan dalam pengolahan data yang memerlukan list sebagai struktur data. Contohnya pengolahan matriks dimensi 2 dst.
> *The append() method adds an item to the end of the list.*

__*Syntax	:*__
```
list.append('new item')
```

__contoh	:__

*Script:*
```
daftar_hari = ['Senin', 'Selasa', 'Rabu']
daftar_hari.append('Kamis')
print('Daftar hari:', daftar_hari)
```
*output:*
```
Daftar hari: ['Senin', 'Selasa', 'Rabu', 'Kamis']
```

## `Extend()`
Sama halnya dengan `append()` yaitu menambahkan data ke akhir list, tetapi data yang ditambahkan bukan *single data* tetapi __list__ data. Metode ini lebih *Powerful* dibandingkan dengan metode sebelumnya, karena data yang bisa ditambahkan dapat berupa *list, set, ataupun tuple*.

>   *The extend() extends the list by adding all items of a list (passed as an argument) to the end.*

___Syntax___
```
list1.extend(list2)
```

__contoh:__

*Script:*
```
Bahasa = ['Inggris','Francis','Spanyol']
Bahasa.extend(['Rusia','Indonesia'])
print('List bahasa:', Bahasa)
```
*output:*
```
List Bahasa: ['Inggris', 'Francis', 'Spanyol', 'Rusia', 'Indonesia']
```

## `Insert()`
Metode insert merupakan metode untuk menambahkan *item atau list* pada ___main list___ dengan posisi item atau list yang akan ditambahkan dapat diatur.
Metode ini memerlukan dua buah argumen atau parameter yaitu `index` dan `element` yang akan ditambahkan.
>  *The insert() method inserts an element to the list at a given index.*

___syntax	:___
```
list.insert(index, element)
```
__contoh	:__

*Script:*
```
vokal = ['a', 'i', 'u', 'o']
vokal.insert(3, 'e')
print('List huruf vokal:', vokal)
```
*output:*
```
List huruf vokal: ['a', 'i', 'u', 'e', 'o']
```
*Script:*
```
konsonan = ['b','c','d','h']
konsonan.insert(3, ['f', 'g'])
print('List huruf konsonan:', konsonan)
```
*output:*
```
List huruf konsonan: ['b','c','d',['f', 'g'],'h']
```


## `Remove()`
Metode ini merupakan metode untuk menghapus item pada list. Cara untuk menghapusnya adalah dengan memasukkan nilai atau item yang akan dihapus pada argumen.
> *The remove() method removes the first matching element (which is passed as an argument) from the list.*

___syntax	:___
```
list.remove('item')
```
___contoh	:___

*Script:*
```
hewan = ['anoa', 'rusa', 'beruang', 'gajah', 'gajah']
hewan.remove('beruang')
print('List Hewan yang baru:', hewan)
```
*output:*
```
>>> List Hewan yang baru: ['anoa', 'rusa', 'gajah', 'gajah']
```

Jika ada duplikat :

*Script:*
```
angka = [1, 2, 3, 4, 4, 5, 4]
angka.remove(4)
print('Angka Sekarang:', angka)
```
*output:*
```
Angka Sekarang: [1, 2, 3, 4, 5, 4]
```

note:
>Jika ada duplikat data, maka data yang akan dihapus hanyalah data yang pertamakali ditemukan dihitung dari index ke - 0 sampai index terakhir

contoh lain:

*Script:*
```
organ = ['Jantung', 'Hati', 'Empedu', 'Lambung']
organ.remove('Usus')
```
Jika item yang akan dihapus tidak ada dalam list, maka ketika kita menginput `organ.remove('Usus')` akan mendapatkan error seperti berikut:

*output:*
```
Traceback (most recent call last):
  File ".. .. ..", line 5, in <module>
    animal.remove('fish')
ValueError: list.remove(x): x not in list
```

untuk menghindari terhentinya program ketika adanya error, maka kita bisa menggunakan metode `try - except` seperti berikut:

*Script:*

```
a = [1, 2, 3]

try:
	a.remove(4)
except ValueError as e:
	print(e)
	pass
```
maka program tidak akan berhenti dan akan dilanjutkan apabila ada program lain dibawahnya.


## `Index()`
Metode ini digunakan untuk mengetahui index dari item yang ada pada list. Cara mencarinya adalah dengan mengisi argumen pada `index(argumen)` dengan item yang ingin dicari indexnya.
___syntax	:___
```
list.index('ítem')
```
__contoh	:__

*Script:*
```
motor = ['Revo', 'Mio', 'Beat', 'Ninja']
index_ke = motor.index('Revo')
print('Revo berada pada index ke-',index_ke)
```
*output:*
```
Revo berada pada index ke- 0
```

Apabila item yang ingin dicari tidak ada dalam list, maka akan menghasilkan error seperti berikut:

*Script:*
```
gaya_rambut = ['Keriting', 'Cepak', 'Bergelombang']
index_ke = gaya_rambut.index('Jocong')
```
*output:*
```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: 'Jocong' is not in list
```
Mencari index list didalam list:

*Script:*
```
sekolah_favorite = ['SMA 1',['SMA 2', 'SMA 3'], 'SMA 4']
index_ke = sekolah_favorite.index(['SMA 2', 'SMA 3'])
print('SMA2 dan SMA3 berada pada index ke-'index_ke)
```
*output:*
```
SMA2 dan SMA3 berada pada index ke- 1
```

## `Count()`
Metode `count()`digunakan untuk mencari berapa banyak item atau element yang sama muncul atau terdapat pada list. Dengan metode ini kita juga dapat mengetahui apakah elemet itu ada atau tidak, serta dapat mengetahui berapa banyak duplikasi pada list.
>*The count() method returns the number of occurrences of an element in a list.*

___syntax	:___
```
list.count(element)
```
__contoh	:__

*Script:*
```
nilai_mahasiswa = [8,8,7,6,7,9,10,6,7]
count = nilai_mahasiswa.count(8)
print('Jumlah nilai dengan angka 8 adalah:', count)
```
*output:*
```
Jumlah nilai dengan angka 8 adalah: 2
```
Contoh lain, apabila element yang kita hitung tidak ada pada list maka akan menghasilkan keluaran berikut:

*Script*
```
warna_favorit = ['Merah','Kuning','Hijau','Biru','Jingga']
warna = warna_favorit.count('Hitam')
print('Jumlah favorit warna hitam adalah:', warna)
```
*output:*
```
Jumlah favorit warna hitam adalah: 0
```
Apabila element yang dicari berupa list ataupun tupple pada list:
*Script:*
```
SMA_Favorit = ['SMA2', ('SMA5', 'SMA3'), 'SMA 1']
sma_fav = SMA_Favorit.count(('SMA5','SMA3'))
print('banyak yang memfavoritkan SMA5 dan SMA3 adalah:', sma_fav)
```
*output:*
```
banyak yang memfavoritkan SMA5 dan SMA3 adalah: 1
```

## `Pop()`
Metode `pop()` digunakan untuk menghapus item atau element dari list, dan akan mengembalikan nilai yang dihapus.
Ada beberapa aturan dalam metode ini, yaitu:
* Metode ini hanya mengambil 1 argumen, yaitu index pada list
* Argumen pada metode ini bersifat opsional. Jika tidak diisi, maka secara otomatis element yang dihapus adalah element pada index ke **-1**
* Apabila argumen yang dimasukkan kedalam metode merupakan nilai index diluar jangkauan index listnya, maka akan menghasilkan error: ___**IndexError: pop index out of range** exception___

> *The pop() method removes the item at the given index from the list and returns the removed item.*

___syntax	:___
```
list.pop(index)
```
__contoh	:__

*Script:*
```
bahasa_pemrograman = ['Python','JavaScript','Java','Indonesia','C++']
bahasa = bahasa_pemrograman.pop(3)
print('Bahasa yang dihapus adalah:',bahasa)
print('Bahasa yang masih ada:',bahasa_pemrograman )
```
*output:*
```
Bahasa yang dihapus adalah: Indonesia
Bahasa yang masih ada: ['Python', 'JavaScript', 'Java', 'C++']
```
Apabila kita tidak memasukkan argumen, maka keluarannya akan seperti berikut:

*Script:*
```
asean = ['Indonesia','Singapura','Malaysia','Yunani']
bukan_asean = asean.pop()
print('Negara yang dihapus dari asean:',bukan_asean)
print('Sisa negara asean:',asean)
```
*output:*
```
Negara yang dihapus dari asean: Yunani
Sisa negara asean: ['Indonesia', 'Singapura', 'Malaysia']
```
Dari contoh diatas, ketika kita tidak memasukkan argumen apapun kedalam metode, maka item yang dihapus adalah item ke __-1__ atau item dengan nilai index paling akhir.
Contoh berikutnya adalah ketika kita memasukkan argumen diluar jangkauan index listnya:
*Script:*
```
merk_handphone = ['Samsung','Xiaomi','Vivo','Opo','Sony']
hapus_merk = merk_handphone.pop(10)
```
Akan menghasilkan error sebagai berikut:
*output:*
```
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    hapus_merk = merk_handphone.pop(10)
IndexError: pop index out of range
```

## `Reverse()`
Reverse berfungsi untuk membalikkan element pada list.
> *The reverse() method reverses the elements of a given list.*

___syntax	:___
```
list.reverse()
```
__contoh	:__

*Script:*
```
angka = [1,2,3,4,5]
angka.reverse()
print(angka)
```
*output:*
```
>>> [5,4,3,2,1]
```
Ada cara lain untuk membalikkan list, yaitu dengan menggunakan *Slicing operator*. Berikut merupakkan contoh menggunakan *Slicing operator*:

*Script:*
```
os = ['Windows', 'macOS', 'Linux']
reversed_list = os[::-1] # Syntax: reversed_list = os[start:stop:step]
print('Update list:',os)
```
*output:*
```
Update list: ['Linux', 'macOS', 'Windows']
```
Selain itu, kita juga dapat menggunakan metode `reversed()`
Contoh:

*Script:*
```
os = ['Windows', 'macOS', 'Linux']
for o in reversed(os):
	print(o)
```
*output:*
```
Linux
macOS
Windows
```
## `Sort()`
Metode `sort()` berfungsi untuk mensortir item atau element pada list. Metode ini dapat mengurutkan nilai baik dari yang terkecil ke yang terbesar atau *(Ascending)*, maupun sebaliknya *(Descending)*

___syntax	:___
*syntax* dengan metode `sort()`
```
list.sort(key=..., reverse=...)
```
cara alternativenya yaitu dengan menggunakan `sorted()`
```
sorted(list, key=..., reverse=...)
```
**Note:** Perbedaan `sort()` dan `sorted()` adalah `sort()` tidak mengebalikkan nilai apapun, sedangkan `sorted()` mengembalikkan daftar iterable

__Parameter	:__
Secara default, sort tidak memerlukan parameter apapun. Tetapi, ada dua opsi parameter yaitu:
* reverse - Jika `true`, maka hasil sorting akan dibalikkan *(Descending)*
* key - fungsi yang berfungsi sebagai kunci untuk perbandingan nilai yang disortir

__contoh	:__

*Script:*
```
angka = [3,2,5,4,1]
angka.sort()
print('Hasil sorting:',angka)
```
*output:*
```
Hasil sorting: [1, 2, 3, 4, 5]
```