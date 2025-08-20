---
{}
---

__Placeholder_18__ Частина 36 - Налагодження Оператора Sizeof

Для повного змісту всіх уроків, будь ласка, натисніть нижче, оскільки він дасть короткий короткий урок на додаток до тем, які він висвітлює. & NBSP; __ Ploadholder_17__

Давайте переглянемо наш код.

__Placeholder_0 __#включає & lt; iostream & gt;

& nbsp;

__Placeholder_222__ main (void) {

& nbsp; & nbsp; & nbsp; & nbsp; & nbsp; & nbsp; & nbsp; & nbsp; & nbsp; & nbsp; & nbsp; __Placeholder_23__ mynumber = 16;

& nbsp; & nbsp; & nbsp; & nbsp; & nbsp; & nbsp; & nbsp; & nbsp; & nbsp; & nbsp; & nbsp; __Placeholder_24__ mynumbersize = sizeof (mynumber);

& nbsp;

& nbsp; & nbsp; & nbsp; & nbsp; & nbsp; & nbsp; & nbsp; & nbsp; & nbsp; & nbsp; & nbsp; std :: cout & lt; & lt; mynumbersize & lt; & lt; std :: endl;

& nbsp;

& nbsp; & nbsp; & nbsp; & nbsp; & nbsp; & nbsp; & nbsp; & nbsp; & nbsp; & nbsp; & nbsp; повернення 0;

}
__Placeholder_1__

__Placeholder_2____placeholder_3____placeholder_4__

Пам'ятайте, що ми створюємо змінну __mynumber = 16__, до якої ми створюємо ще одну змінну __mynumbersize__, яка містить значення розміру __mynumber __. & NBSP; ми бачимо, що коли ми виконуємо наш код, він показує 4, тому ми бачимо, що оператор розмірівофів вказує на ціле чисельність, має 4 байт.

Давайте налагоджуємо __placeholder_25__ перерва на головному.

__Placeholder_5____Placeholder_6____Placeholder_7__

Давайте розірвемося на __main+20__, як ми бачимо, що значення __4__ переміщується в __r3__.

__Placeholder_8____Placeholder_9____Placeholder_10__

Давайте розглянемо, що відбувається в __main+16__, оскільки ми бачимо, що ми зберігаємо вартість __ $ __ ploadholder_19 __- 8__ того, що існує в __r3__, що в нашому випадку __16 __. Всередині __ $ __ Ploadholder_20 __- 8__.

__Placeholder_11____Placeholder_12____Placeholder_13__________________

Як ми бачимо вище значення всередині __ $ __ ploadholder_21 __- 12__ IS__ 4__, оскільки це представляє значення, яке __SizeOf__ повертається як ціле число __16 __, насправді 4 байти широко.

__Placeholder_14____Placeholder_15____Placeholder_16__

Нарешті, коли ми продовжуємо виконання, ми насправді бачимо значення __4__ перегукується з терміналом.

На наступному тижні ми зануримось у оператор Hacking Sizeof.