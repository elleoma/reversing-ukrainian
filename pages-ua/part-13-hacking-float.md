---
{}
---

__Placeholder_29__ Частина 13 - Злом поплавця

Давайте розглянемо наш приклад. & Nbsp; __ 0x05 \ _float.c __ & nbsp; наступним чином.

__Placeholder_0 __#включити & lt; stdio__placeholder_36 __ & gt;
__Placeholder_30__ включити "pico/stdlib__placeholder_37__"

__Placeholder_35__ main () & nbsp;
{
& nbsp; stdio_init_all ();

& nbsp; в той час як (1) & nbsp;
& nbsp; {
& nbsp; & nbsp; float x = 40,5;

& nbsp; & nbsp; __Placeholder_43 __ ("%f \ n", x); & nbsp;

& nbsp; & nbsp; Sleep_ms (1000);
& nbsp; }

& nbsp; повернення 0;
}
__Placeholder_1__

Давайте розберемося в нашому налагоджувачі.

__Placeholder_2__radare2 -w __placeholder_46__ -b 16 0x05_float .__ ploadholder_31__
__Placeholder_3__

Давайте автоматично проаналізуємо.

__Placeholder_4__aaaa
__Placeholder_5__

Давайте прагнемо до головного.

__Placeholder_6__s main
__Placeholder_7__

Перейдемо у візуальний режим, ввівши & nbsp; __ v __ & nbsp; __ ploadholder_39__ тоді & nbsp; __ p __ & nbsp; двічі, щоб дістатися до хорошого подання налагоджувача.

__Placeholder_8____Placeholder_9____Placeholder_10__

Поплавок AT & nbsp; _ \ [0x00000340 \] _.

__Placeholder_11 __: & gt; pff @ [0x00000340]
0x00004000 = 9.32830524E-09
__Placeholder_12__

Як ми обговорювали на останньому уроці, зробіть __placeholder_45__ хвилюйтеся, що поплавок є неточним, оскільки ця машина __placeholder_44__. Що важливо побачити значення & nbsp; _0x00004000_.

На нашому останньому уроці ми також пояснили те, як Піко обробляє плавання. Давайте розглянемо деякі основи.

__Placeholder_13__0x3ff00000 = 1.000000
0x3ff00001 = 1,000001
0x3ff00002 = 1,000002
...
0x3ff0000f = 1.000015
0x3ff00010 = 1.000016
0x3ff00011 = 1.000017
тощо ...
__Placeholder_14__

Давайте зламаємо до 1.000000 наступним чином.

Наш мікроконтролер - це маленька ендіанська архітектура, тому, якщо ми збираємось змінити наше 40,5 до 1,0, нам потрібно поставити це значення у зворотному порядку байтів ...

__Placeholder_15__0x3ff00000
__Placeholder_16__

Потрібно бути ...

__Placeholder_17__0x0000f03f
__Placeholder_18__

Тому нам потрібно змінити значення на наступному.

__Placeholder_19__wx 0x0000f03f @ 0x00000340
__Placeholder_20__

Все, що нам потрібно зробити зараз, - це вихід __placeholder_40__ перетворіть нашу & nbsp; __.__ ploadholder_32 __ & nbsp; __ до & nbsp; __. Uf2__!

__Placeholder_21__./elf2uf2/elf2uf2 0x05_float .__ ploadholder_33__ 0x05_float.uf2
__Placeholder_22__

Підключіть Pico __placeholder_41__ Переконайтесь, що ви тримаєте завантаження __placeholder_34__ Використовуйте налаштування, яку я надав у частині 2.

__Placeholder_23__cp 0x05_float.uf2 /томи /rpi-rp2
__Placeholder_24__

Давайте екранимо це!

__Placeholder_25__screen /__placeholder_38__/tty.usbmodem00000000001
__Placeholder_26__

Ага так!

__Placeholder_27__1.000000
1.000000
1.000000
1.000000
1.000000
1.000000
1.000000
1.000000
1.000000
1.000000
1.000000
1.000000
__Placeholder_28__

Тут ми зламали цінність до 1.000000 __placeholder_42__, ми дозволили зберегти 1 секунду.

На нашому наступному уроці ми обговоримо подвійний тип даних.