---
{}
---

__Placeholder_25__ Частина 16 - Злом подвійний

Давайте розглянемо & nbsp; __ 0x06 \ _double \ _mod.c __ & nbsp; наступним чином.

__Placeholder_0 __#включити & lt; stdio__placeholder_32 __ & gt;
__Placeholder_26__ включити "pico/stdlib__placeholder_33__"

__Placeholder_31__ main () & nbsp;
{
& nbsp; stdio_init_all ();

& nbsp; в той час як (1) & nbsp;
& nbsp; {
& nbsp; & nbsp; подвійний X = 40.555555555555555555555;

& nbsp; & nbsp; __Placeholder_38 __ ("%. 16f \ n", x) & nbsp;

& nbsp; & nbsp; Sleep_ms (1000);
& nbsp; }

& nbsp; повернення 0;
}
__Placeholder_1__

Давайте розберемося в нашому налагоджувачі.

__Placeholder_2__radare2 -w __placeholder_39__ -b 16 0x06_double .__ ploadholder_27__
__Placeholder_3__

Давайте автоматично проаналізуємо.

__Placeholder_4__aaaa
__Placeholder_5__

Давайте прагнемо до головного.

__Placeholder_6__s main
__Placeholder_7__

Давайте перейдемо у візуальний режим, ввівши & nbsp; __ v __ & nbsp; __ ploadholder_35__ тоді & nbsp; __ p __ & nbsp; двічі, щоб дістатися до хорошого подання налагоджувача.

__Placeholder_8____Placeholder_9____Placeholder_10__

Наш мікроконтролер - це маленька ендіанська архітектура, як ми говорили раніше, тому, якщо ми збираємось змінити наше 40.5555555560000000 на 1,0, нам потрібно поставити це значення у зворотному порядку байтів, тому ...

__Placeholder_11__0x3ff00000
__Placeholder_12__

Потрібно бути ...

__Placeholder_13__0x0000f03f
__Placeholder_14__

Тому нам потрібно змінити значення на наступному.

__Placeholder_15__wx 0x0000f03f @ 0x00000344
__Placeholder_16__

Все, що нам потрібно зробити зараз, - це вихід __placeholder_36__ Перетворіть наше & nbsp; __.__ ploadholder_28 __ & nbsp; __ до & nbsp; __. Uf2__!

__Placeholder_17__./elf2uf2/elf2uf2 0x06_double .__ ploadholder_29__ 0x06_double.uf2
__Placeholder_18__

Підключіть Pico __placeholder_37__ Переконайтесь, що ви тримаєте Bootsel __placeholder_30__ Використовуйте налаштування, яку я надав у частині 2.

__Placeholder_19__cp 0x06_double.uf2 /томи /rpi-rp2
__Placeholder_20__

Давайте екранимо це!

__Placeholder_21__screen /__placeholder_34__/tty.usbmodem00000000001
__Placeholder_22__

Ага так!

__Placeholder_23__1.0000002380000000
1.00002380000000
1.00002380000000
1.00002380000000
1.00002380000000
1.00002380000000
1.00002380000000
1.00002380000000
1.00002380000000
1.00002380000000
1.00002380000000
1.00002380000000
1.00002380000000
1.00002380000000
1.00002380000000
__Placeholder_24__

Тепер ми повинні добре розуміти типи даних всередині С, щоб переглянути деякі трохи більші поняття.

На нашому наступному уроці ми почнемо обговорювати вклад.