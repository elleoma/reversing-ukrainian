---
{}
---

__Placeholder_9__ Частина 35 - Оператор Sizeof

Для повного змісту всіх уроків, будь ласка, натисніть нижче, оскільки він дасть короткий короткий урок на додаток до тем, які він висвітлює. & NBSP; __ Ploadholder_8__

Наступний етап нашої подорожі - це оператор Sizeof. & NBSP;

Давайте розглянемо наш код.

__Placeholder_0 __#включає & lt; iostream & gt;

& nbsp;

__Placeholder_11__ main (void) {

& nbsp; & nbsp; & nbsp; & nbsp; & nbsp; & nbsp; & nbsp; & nbsp; & nbsp; & nbsp; & nbsp; __Placeholder_12__ mynumber = 16;

& nbsp; & nbsp; & nbsp; & nbsp; & nbsp; & nbsp; & nbsp; & nbsp; & nbsp; & nbsp; & nbsp; __Placeholder_13__ mynumbersize = sizeof (mynumber);

& nbsp;

& nbsp; & nbsp; & nbsp; & nbsp; & nbsp; & nbsp; & nbsp; & nbsp; & nbsp; & nbsp; & nbsp; std :: cout & lt; & lt; mynumbersize & lt; & lt; std :: endl;

& nbsp;

& nbsp; & nbsp; & nbsp; & nbsp; & nbsp; & nbsp; & nbsp; & nbsp; & nbsp; & nbsp; & nbsp; повернення 0;

}
__Placeholder_1__

__Placeholder_2____placeholder_3____placeholder_4__

Щоб скласти це, ми просто вводимо:

g ++ example8__placeholder_10__ -o example8

./example8

__Placeholder_5____Placeholder_6____Placeholder_7__

Ми бачимо 4 надруковані на екрані.

Давайте розберемо його:

Ми створюємо змінну __mynumber = 16__, на яку ми створюємо іншу змінну __mynumbersize__, яка містить значення розміру __mymumber __. & NBSP; ми бачимо, що коли ми виконуємо наш код, він показує 4, тому ми бачимо, що оператор розміру вказує на ціле число 4 байти.

Наступного тижня ми зануримось у налагодження оператора Sizeof.