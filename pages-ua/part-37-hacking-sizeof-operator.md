---
{}
---

__Placeholder_36__ Частина 37 - Злом оператора Sizeof

Для повного змісту всіх уроків, будь ласка, натисніть нижче, оскільки він дасть короткий короткий урок на додаток до тем, які він висвітлює. & NBSP; __ Ploadholder_35__

Давайте переглянемо наш код.

__Placeholder_0 __#включає & lt; iostream & gt;

& nbsp;

__Placeholder_40__ main (void) {

& nbsp; & nbsp; & nbsp; & nbsp; & nbsp; & nbsp; & nbsp; & nbsp; & nbsp; & nbsp; & nbsp; __Placeholder_41__ mynumber = 16;

& nbsp; & nbsp; & nbsp; & nbsp; & nbsp; & nbsp; & nbsp; & nbsp; & nbsp; & nbsp; & nbsp; __Placeholder_42__ mynumbersize = sizeof (mynumber);

& nbsp;

& nbsp; & nbsp; & nbsp; & nbsp; & nbsp; & nbsp; & nbsp; & nbsp; & nbsp; & nbsp; & nbsp; std :: cout & lt; & lt; mynumbersize & lt; & lt; std :: endl;

& nbsp;

& nbsp; & nbsp; & nbsp; & nbsp; & nbsp; & nbsp; & nbsp; & nbsp; & nbsp; & nbsp; & nbsp; повернення 0;

}
__Placeholder_1__

__Placeholder_2____placeholder_3____placeholder_4__

Пам'ятайте, що ми створюємо змінну __mynumber = 16__, до якої ми створюємо ще одну змінну __mynumbersize__, яка містить значення розміру __mynumber __. & NBSP; ми бачимо, що коли ми виконуємо наш код, він показує 4, тому ми бачимо, що оператор розмірівофів вказує на ціле чисельність, має 4 байт.

Давайте переглянемо код минулого тижня, коли ми починаємо з налагодження __placeholder_43__, що розбивається на Main.

__Placeholder_5____Placeholder_6____Placeholder_7__

Давайте розірвемося на __main+20__, як ми бачимо, що значення __4__ переміщується в __r3__.

__Placeholder_8____Placeholder_9____Placeholder_10__

Давайте розглянемо, що відбувається в __main+16__, оскільки ми можемо побачити, що ми зберігаємо вартість __ $ __ procesholder_37 __- 8__, що існує в __r3__, що в нашому випадку __16 __. Всередині __ $ __ Ploadholder_38 __- 8__.

__Placeholder_11____Placeholder_12____Placeholder_13__________________

Як ми бачимо вище значення всередині __ $ __ procesholder_39 __- 12__ IS__ 4__, оскільки це являє собою значення, яке __SizeOf__ повертається як ціле число __16 __, насправді 4 байти широко.

__Placeholder_14____Placeholder_15____Placeholder_16__

Нарешті, коли ми продовжуємо виконання, ми насправді бачимо значення __4__ перегукується з терміналом.

Давайте хакемо!

__Placeholder_17____Placeholder_18____Placeholder_19__

Ми запускаємо __placeholder_44__ перерва на __main+28__.

__Placeholder_20____Placeholder_21____Placeholder_22______

Ми бачимо, що цінність у __R3__ - __4__, що очікується.

__Placeholder_23____placeholder_24____placeholder_25__

Ми ламаємося на __main+36__.

__Placeholder_26____Placeholder_27____Placeholder_28__

Ми бачимо, що значення в __R1__ є __4__, що повинно мати логічний сенс, оскільки значення зберігалося з __R3__ в __R11-12__ __placeholder_45__, а потім назад до __R1__.

__Placeholder_29____Placeholder_30____Placeholder_31__

Давайте зламаємо значення в __R1__!

__Placeholder_32____Placeholder_33____Placeholder_34__

Успіх! & Nbsp; ми зламали машину!

Наступного тижня ми зануримося в оператор попереднього інкрементації.