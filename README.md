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

```
>>> daftar_hari = ['Senin', 'Selasa', 'Rabu']
>>> daftar_hari.append('Kamis')
>>> print(daftar_hari)
```
`>>> ['Senin', 'Selasa', 'Rabu', 'Kamis']`

## `Extend()`
Sama halnya dengan `append()` yaitu menambahkan data ke akhir list, tetapi data yang ditambahkan bukan *single data* tetapi __list__ data. Metode ini lebih *Powerful* dibandingkan dengan metode sebelumnya, karena data yang bisa ditambahkan dapat berupa *list, set, ataupun tuple*.

>   *The extend() extends the list by adding all items of a list (passed as an argument) to the end.*

___Syntax___
```
list1.extend(list2)
```

__contoh:__
```
>>> Bahasa = ['Inggris','Francis','Spanyol']
>>> Bahasa.extend(['Rusia','Indonesia'])
>>> print(Bahasa)
```
`>>> ['Inggris', 'Francis', 'Spanyol', 'Rusia', 'Indonesia']`

## `Insert()`
Metode insert merupakan metode untuk menambahkan *item atau list* pada ___main list___ dengan posisi item atau list yang akan ditambahkan dapat diatur.
Metode ini memerlukan dua buah argumen atau parameter yaitu `index` dan `element` yang akan ditambahkan.
>  *The insert() method inserts an element to the list at a given index.*

___syntax	:___
```
list.insert(index, element)
```
__contoh	:__
```
>>> vokal = ['a', 'i', 'u', 'o']
>>> vokal.insert(3, 'e')
>>> print(vokal)
```
`>>> ['a', 'i', 'u', 'e', 'o']`

```
>>> konsonan = ['b','c','d','h']
>>>	konsonan.insert(3, ['f', 'g'])
>>> print(konsonan)
```
`>>> ['b','c','d',['f', 'g'],'h']`


## `Remove()`
Metode ini merupakan metode untuk menghapus item pada list. Cara untuk menghapusnya adalah dengan memasukkan nilai atau item yang akan dihapus pada argumen.
> *The remove() method removes the first matching element (which is passed as an argument) from the list.*

___syntax	:___
```
list.remove('item')
```
___contoh	:___
```
>>> hewan = ['anoa', 'rusa', 'beruang', 'gajah', 'gajah']
>>> hewan.remove('beruang')
>>> print(hewan)
```
`>>> ['anoa', 'rusa', 'gajah', 'gajah']`

Jika ada duplikat :
```
>>> angka = [1, 2, 3, 4, 4, 5, 4]
>>> angka.remove(4)
>>> print(angka)
```
`>>> [1, 2, 3, 4, 5, 4]`

note:
>Jika ada duplikat data, maka data yang akan dihapus hanyalah data yang pertamakali ditemukan dihitung dari index ke - 0 sampai index terakhir

contoh lain:
```
>>>	organ = ['Jantung', 'Hati', 'Empedu', 'Lambung']
>>> organ.remove('Usus')
```
Jika item yang akan dihapus tidak ada dalam list, maka ketika kita menginput `organ.remove('Usus')` akan mendapatkan error seperti berikut:
```
Traceback (most recent call last):
  File ".. .. ..", line 5, in <module>
    animal.remove('fish')
ValueError: list.remove(x): x not in list
```

untuk menghindari terhentinya program ketika adanya error, maka kita bisa menggunakan metode `try - except` seperti berikut:
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
```
>>>	motor = ['Revo', 'Mio', 'Beat', 'Ninja']
>>>	index_ke = motor.index('Revo')
>>> print(index_ke)
```
`>>> 0`

Apabila item yang ingin dicari tidak ada dalam list, maka akan menghasilkan error seperti berikut:
```
>>> gaya_rambut = ['Keriting', 'Cepak', 'Bergelombang']
>>> index_ke = gaya_rambut.index('Jocong')
```
```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: 'Jocong' is not in list
```
Mencari index list didalam list:
```
>>> sekolah_favorite = ['SMA 1',['SMA 2', 'SMA 3'], 'SMA 4']
>>> index_ke = sekolah_favorite.index(['SMA 2', 'SMA 3'])
>>> print(index_ke)
```

`>>> 1`