---
{}
---

__Placeholder_21__ Частина 39-Налагодження оператора попереднього інкрементації

Для повного змісту всіх уроків, будь ласка, натисніть нижче, оскільки він дасть короткий короткий урок на додаток до тем, які він висвітлює. & NBSP; __ Ploadholder_20__

Давайте переглянемо наш код.

__Placeholder_0 __#включає & lt; iostream & gt;

& nbsp;

__Placeholder_23__ main (void) {

& nbsp; & nbsp; & nbsp; & nbsp; & nbsp; & nbsp; & nbsp; & nbsp; & nbsp; & nbsp; & nbsp; __Placeholder_24__ mynumber = 16;

& nbsp; & nbsp; & nbsp; & nbsp; & nbsp; & nbsp; & nbsp; & nbsp; & nbsp; & nbsp; & nbsp; __Placeholder_25__ mynewnumber = ++ mynumber;

& nbsp;

& nbsp; & nbsp; & nbsp; & nbsp; & nbsp; & nbsp; & nbsp; & nbsp; & nbsp; & nbsp; & nbsp; std :: cout & lt; & lt; mynewnumber & lt; & lt; std :: endl;

& nbsp;

& nbsp; & nbsp; & nbsp; & nbsp; & nbsp; & nbsp; & nbsp; & nbsp; & nbsp; & nbsp; & nbsp; повернення 0;

}
__Placeholder_1__

__Placeholder_2____placeholder_3____placeholder_4__

Щоб скласти це, ми просто вводимо:

g ++ example9__placeholder_22__ -o example9

./example9

__Placeholder_5____Placeholder_6____Placeholder_7__

Ми бачимо 17 надрукованих на екран.

Давайте розберемо його:

Ми створюємо змінну __mynumber = 16__, до якої ми створюємо іншу змінну __mynewnumber__, що попередньо запроваджує значення __mynumber __. & Nbsp; ми бачимо це, коли виконуємо наш код, він показує 17.

Коли ми заздалегідь запроваджуємо, значення змінної збільшується перед тим, як призначити її іншій змінній. & NBSP; наприклад, __Mynumber__ є __16__, тому вона збільшується, перш ніж бути призначеним до __mynewnumbum__, тому ми отримуємо __17__.

Давайте налагоджуємо.

__Placeholder_8____Placeholder_9____Placeholder_10__

Ми проводимо звичайний старт у __placeholder_28__ __placeholder_26__ Break on Main. & Nbsp; взяти до уваги __main+24__ Ми переміщуємо значення __1__ в __r3 __.

__Placeholder_11____Placeholder_12____Placeholder_13__________________

Коли ми оцінюємо значення в __R3__ на цьому етапі, ми бачимо __17 __.

__Placeholder_14____Placeholder_15____Placeholder_16__

Ми бачимо, що коли ми продовжуємо код, значення __17__ успішно перегукується до терміналу, як очікувалося.

__Placeholder_17____Placeholder_18____Placeholder_19__

Наступного тижня ми зануримося в зламу налагодження оператора попереднього інтекції.