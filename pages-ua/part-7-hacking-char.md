---
{}
---

__Placeholder_27__ Частина 7 - Хакерський шар

Сьогодні ми зламаємо просту програму CHAR.

Давайте розглянемо наш код.

__Placeholder_0 __#включити & lt; stdio__placeholder_45 __ & gt;
__Placeholder_28__ включити "pico/stdlib__placeholder_46__"

__Placeholder_43__ main () & nbsp;
{
& nbsp; stdio_init_all ();

& nbsp; в той час як (1) & nbsp;
& nbsp; {
& nbsp; & nbsp; char x = 'x';
& nbsp; & nbsp; & nbsp; & nbsp; & nbsp;
& nbsp; & nbsp; __Placeholder_52 __ ("%c \ n", x);

& nbsp; & nbsp; Sleep_ms (1000);
& nbsp; }
& nbsp; & nbsp; & nbsp; & nbsp; & nbsp;
& nbsp; повернення 0;
}
__Placeholder_1__

Давайте розберемо наш налагоджувач.

__Placeholder_2__radare2 -w __placeholder_53__ -b 16 0x03_char .__ ploadholder_29__
__Placeholder_3__

Давайте автоматично проаналізуємо.

__Placeholder_4__aaaa
__Placeholder_5__

Давайте прагнемо до головного.

__Placeholder_6__s main
__Placeholder_7__

Давайте перейдемо у візуальний режим, ввівши & nbsp; __ v __ & nbsp; __ ploadholder_48__ тоді & nbsp; __ p __ & nbsp; двічі, щоб дістатися до хорошого подання налагоджувача.

__Placeholder_8____Placeholder_9____Placeholder_10__

На нашому останньому уроці ми зламали кожен рядок. Тут ми, очевидно, зацікавлені у зламанні значення 0x78 __placeholder_49__, змінюючи це на все, що ми хочемо. Спробуємо 0x79. Цей простий хак перетворить char _'x'_ в _'y'_.

__Placeholder_11 __: & gt; wa movs __placeholder_32__, 0x79 @ 0x00000328
Написано 2 байти (и) (Movs __placeholder_33__, 0x79) = WX 7921
__Placeholder_12__

Давайте перевіримо зміни.

__Placeholder_13 __: & gt; PD 1 @ 0x00000328
│ & nbsp; & nbsp; & nbsp; & nbsp; & nbsp; ; Код XREF від Main @ 0x338
│ & nbsp; & nbsp; & nbsp; & nbsp; & nbsp; 0x00000328 & NBSP; & nbsp; & nbsp; 7921 & NBSP; & nbsp; & nbsp; & nbsp; & nbsp; movs __placeholder_34__, 0x79 & nbsp; & nbsp; & nbsp; & nbsp; & nbsp; & nbsp; & nbsp; ; 'y'; arg1
__Placeholder_14__

У цьому випадку наш налагоджувач навіть говорить нам, що це насправді _'y'_, крім того, зараз ми переміщуємо значення шестигранного ASCII в 0x79 в _R1_.

Давайте також зламаємо час сну до 2000 MS __placeholder_35__ 2 секунди.

__Placeholder_15 __: & gt; wa lsls __placeholder_37__, __placeholder_38__, 3 @ 0x00000332
Написано 2 байти (и) (lsls __placeholder_39__, __placeholder_40__, 3) = WX C000
__Placeholder_16__

Тут ми просто логічний зсув ліворуч 3 рази, тому 250 x 2 = 500, 500 x 2 = 1000, 1000 x 2 = 2000.

Давайте перевіримо.

__Placeholder_17 __: & gt; PD 1 @ 0x00000332
│ & nbsp; & nbsp; & nbsp; & nbsp; & nbsp; 0x00000332 & NBSP; & nbsp; & nbsp; C000 & NBSP; & nbsp; & nbsp; & nbsp; & nbsp; lsls __placeholder_41__, __placeholder_42__, 3
__Placeholder_18__

Все, що нам потрібно зробити зараз, - це вихід __placeholder_50__ перетворити наш & nbsp; __.__ ploadholder_30 __ & nbsp; __ до & nbsp; __. Uf2__!

__Placeholder_19__./elf2uf2/elf2uf2 0x03_char .__ ploadholder_31__ 0x03_char.uf2
__Placeholder_20__

Підключіть Pico __placeholder_51__ Переконайтеся, що ви тримаєте завантаження __placeholder_36__ Використовуйте налаштування, яку я надав у частині 2.

__Placeholder_21__cp 0x03_char.uf2 /volumes /rpi-rp2
__Placeholder_22__

Давайте екранимо це!

__Placeholder_23__screen /__placeholder_47__/tty.usbmodem00000000001
__Placeholder_24__

Ага так!

__Placeholder_25__y
у
у
у
у
у
__Placeholder_26__

Ми бачимо, як "Y" надруковано кожні 2 секунди!

На нашому наступному уроці ми обговоримо тип даних __placeholder_44__.