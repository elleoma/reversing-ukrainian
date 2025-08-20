---
{}
---

__Placeholder_39__ Частина 4 - Закрання Hello World

На останньому уроці ми розглянули, як правильно налагодити наш дуже простий бінар у __radare2__. Сьогодні ми збираємося зламати цей статичний __.__ ploadholder_41__ __binary __placeholder_62__ перетворити його на __. UF2__ формат __placeholder_63__ спалахує до нашого Pico __placeholder_64__ Див. Давайте ще раз розглянемо нашу дуже просту програму. __Placeholder_0 __#включити & lt; stdio__placeholder_59 __ & gt;
__Placeholder_40__ включити "pico/stdlib__placeholder_60__"

__Placeholder_58__ main () & nbsp;
{	
& nbsp; stdio_init_all ();

& nbsp; в той час як (1) & nbsp;
& nbsp; {
& nbsp;   __Placeholder_72 __ ("Привіт світ! \ N");

& nbsp; & nbsp; Sleep_ms (1000);
& nbsp; }
    
  повернення 0;
}
__Placeholder_1__

Давайте завантажимо наш двійковий. __Placeholder_2__radare2 -w __placeholder_73__ -b 16 0x02_hello_world .__ ploadholder_42__
__Placeholder_3__

Давайте автоматично проаналізуємо. __Placeholder_4__aaaa
__Placeholder_5__

Давайте прагнемо до головного. __Placeholder_6__s main
__Placeholder_7__

Давайте використовуємо Visual Mode __placeholder_65__ натисніть P двічі, щоб отримати наш улюблений вигляд налагоджувача. __Placeholder_8__v
__Placeholder_9__

Давайте розглянемо просту збірку ARM32. __Placeholder_10____Placeholder_11________Solder_12__

Я б зламав цей двійковий двома способами. Як ми обговорювали на останньому уроці, ми бачимо вміст всередині місця пам'яті _0x00000338_, що містить значення нашого рядка. Давайте натиснемо на товсту кишку: __placeholder_66__ натисніть Enter. __Placeholder_13 __: & gt; PSZ @ [0x00000338]
Привіт світ! __Placeholder_14__

Давайте розглянемо наш __placeholder_56__. Я хочу, щоб ви звернули увагу на "привіт світ!" як ви побачите дві адреси. Ліворуч - це фізична адреса __placeholder_67__, що безпосередньо праворуч - віртуальна адреса. Ми будемо стурбовані віртуальною адресою. Щоб краще зрозуміти, давайте зробимо наступне. __Placeholder_15 __: & gt; iz ~ | менше
__Placeholder_16__

Як ви бачите, наша рядок знаходиться вгорі. __Placeholder_17 __ [__ ploadholder_57__]
nth paddr & nbsp; & nbsp; & nbsp; VADDR & NBSP; & nbsp; & nbsp; Тип розділу LEN та NBSP; & nbsp; нитка
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - --―
0 & nbsp; & nbsp; 0x00014cf8 0x00004cf8 12 & nbsp; 13 & nbsp; & nbsp; .rodata ascii & nbsp; & nbsp; привіт світ! 1 & nbsp; & nbsp; 0x00014d08 0x00004d08 26 & nbsp; 27 & NBSP; & nbsp; .rodata ascii & nbsp; & nbsp; немає спіноків
2 & nbsp; & nbsp; 0x00014d24 0x00004d24 33 & nbsp; 34 & NBSP; & nbsp; .rodata ascii & nbsp; & nbsp; апаратна сигналізація %d вже заявлена
3 & nbsp; & nbsp; 0x00014d48 0x00004d48 15 & nbsp; 16 & nbsp; & nbsp; .rodata ascii & nbsp; & nbsp; \ n *** паніка *** \ n
4 & nbsp; & nbsp; 0x00014d5c 0x00004d5c 11 & nbsp; 12 & nbsp; & nbsp; .rodata ascii & nbsp; & nbsp; жорстка ствердження
5 & nbsp; & nbsp; 0x00014d68 0x00004d68 7 & nbsp; & nbsp; 8 & nbsp; & nbsp; .rodata ascii & nbsp; & nbsp;
6 & nbsp; & nbsp; 0x00014d70 0x00004d70 5 & nbsp; & nbsp; 6 & nbsp; & nbsp; .rodata ascii & nbsp; & nbsp; 1.0.0
7 & nbsp; & nbsp; 0x00014d78 0x00004d78 4 & nbsp; & nbsp; 5 & nbsp; & nbsp; .rodata ascii & nbsp; & nbsp; Pico
8 & nbsp; & nbsp; 0x00014d80 0x00004d80 16 & nbsp; 17 & nbsp; & nbsp; .rodata ascii & nbsp; & nbsp; 0x02_hello_world
9 & nbsp; & nbsp; 0x00014d94 0x00004d94 11 & nbsp; 12 & nbsp; & nbsp; .rodata ascii & nbsp; & nbsp; 21 березня 2021
10 & nbsp; 0x00014DB2 0x00004DB2 4 & NBSP; & nbsp; 5 & nbsp; & nbsp; .rodata ascii & nbsp; & nbsp; ubhm
11 & nbsp; 0x00014DBC 0x00004DBC 10 & NBSP; 11 & nbsp; & nbsp; .rodata ascii & nbsp; & nbsp; uart stdin
12 & nbsp; 0x00014DC8 0x00004DC8 11 & NBSP; 12 & nbsp; & nbsp; .rodata ascii & nbsp; & nbsp; uart stdout
13 & nbsp; 0x00014dd4 0x00004dd4 19 & nbsp; 20 & nbsp; & nbsp; .rodata ascii & nbsp; & nbsp; uart stdin / stdout
14 & nbsp; 0x00014DFC 0x00004DFC 18 & NBSP; 19 & NBSP; & nbsp; .rodata ascii & nbsp; & nbsp; usb stdin / stdout
15 & nbsp; 0x00014e1c 0x00004e1c 12 & nbsp; 13 & nbsp; & nbsp; .rodata ascii & nbsp; & nbsp; Raspberry pi
16 & nbsp; 0x00014e2c 0x00004e2c 4 & nbsp; & nbsp; 5 & nbsp; & nbsp; .rodata ascii & nbsp; & nbsp; Pico
17 & nbsp; 0x00014E34 0x00004E34 12 & NBSP; 13 & nbsp; & nbsp; .rodata ascii & nbsp; & NBSP; 0000000000
18 & NBSP; 0x00014E44 0x00004E44 9 & NBSP; & nbsp; 10 & nbsp; & nbsp; .rodata ascii & nbsp; & nbsp; плата CDC
19 & NBSP; 0x00014ec4 0x00004ec4 19 & nbsp; 20 & nbsp; & nbsp; .rodata ascii & nbsp; & nbsp; незбагнено IRQ 0x%x \ n
20 & nbsp; 0x00014ED8 0x00004ED8 39 & NBSP; 40 & NBSP; & nbsp; .rodata ascii & nbsp; & nbsp; ізохронний wmaxpacketsize %d занадто великий
21 & nbsp; 0x00014F00 0x00004F00 30 & NBSP; 31 & nbsp; & nbsp; .rodata ascii & nbsp; & nbsp; ep %d %s вже був доступний
22 & nbsp; 0x00014F20 0x00004F20 40 & NBSP; 41 & NBSP; & nbsp; .rodata ascii & nbsp; & nbsp; не може продовжувати xfer на неактивному EP %d %s
23 & nbsp; 0x00014F4C 0x00004F4C 35 & NBSP; 36 & NBSP; & nbsp; .rodata ascii & nbsp; & nbsp; передача більше даних, ніж очікувалося
0 & nbsp; & nbsp; 0x00020135 0x10000135 5 & nbsp; & nbsp; 6 & nbsp; & nbsp; .data & nbsp; & nbsp; ascii & nbsp; & nbsp; v \ n` \ eh
1 & nbsp; & nbsp; 0x0002018b 0x1000018b 5 & nbsp; & nbsp; 6 & nbsp; & nbsp; .data & nbsp; & nbsp; ascii & nbsp; & nbsp; & amp; cf \ eh
2 & nbsp; & nbsp; 0x000201a0 0x100001a0 4 & nbsp; & nbsp; 5 & nbsp; & nbsp; .data & nbsp; & nbsp; ascii & nbsp; & nbsp; cf \ ey
3 & nbsp; & nbsp; 0x000201a8 0x100001a8 4 & nbsp; & nbsp; 5 & nbsp; & nbsp; .data & nbsp; & nbsp; ascii & nbsp; & nbsp; cf \ eh
4 & nbsp; & nbsp; 0x000201d0 0x100001d0 4 & nbsp; & nbsp; 5 & nbsp; & nbsp; .data & nbsp; & nbsp; ascii & nbsp; & nbsp; \ thaq
5 & nbsp; & nbsp; 0x0002028d 0x1000028d 5 & nbsp; & nbsp; 6 & nbsp; & nbsp; .data & nbsp; & nbsp; ascii & nbsp; & nbsp; gpf \ t8
6 & nbsp; & nbsp; 0x00020805 0x10000805 5 & nbsp; & nbsp; 11 & nbsp; & nbsp; .data & nbsp; & nbsp; utf16le \ a \ b \ b
7 & nbsp; & nbsp; 0x00020905 0x10000905 5 & nbsp; & nbsp; 11 & nbsp; & nbsp; .data & nbsp; & nbsp; utf16le \ b \ t \ t
8 & nbsp; & NBSP; 0x00020A05 0x10000A05 5 & NBSP; & nbsp; 11 & nbsp; & nbsp; .data & nbsp; & nbsp; utf16le \ t \ n \ n
9 & nbsp; & nbsp; 0x00020b05 0x10000b05 5 & nbsp; & nbsp; 11 & nbsp; & nbsp; .data & nbsp; & nbsp; utf16le \ n \ v \ v
(Кінець)
__Placeholder_18__

Ви можете побачити значення _0x00004cf8_ тримає наш рядок, щоб довести, що ми можемо зробити наступне. __Placeholder_19 __: & gt; PSZ @ 0x00004CF8
Привіт світ! __Placeholder_20__

Давайте зламаємо це. __Placeholder_21 __: & gt; w Зламаний світ! @ [0x00000338]
__Placeholder_22__

Давайте перевіримо, що значення змінюється. __Placeholder_23 __: & gt; PSZ @ 0x00004CF8
Зламаний світ! __Placeholder_24__

Інша річ, яку я хотів би зламати, - це сон \ _ms, який наразі встановлений на 1000. Пам'ятайте, що він показує 250 десятків __placeholder_45__ 0xfa hex __placeholder_68__ Ми логічні зсуви ліворуч двічі, як ми обговорюємо на останньому уроці. Перший логічний зсув ліворуч помножиться на 2, що призведе до 500 __placeholder_69__ 2 -й логічний зсув ліворуч буде помножуватися на 2, що піднімає нас до 1000.
__Placeholder_26__

Давайте зламаємо це, змінивши 2 на 1. Це зробить затримку 500 мс __placeholder_46__ півсекунди. __Placeholder_27 __: & gt; wa lsls __placeholder_50__, __placeholder_51__, 1 @ 0x00000330
Написано 2 байти (и) (LSLS __placeholder_52__, __placeholder_53__, 1) = WX 4000
__Placeholder_28__

Давайте перевіримо. __Placeholder_29 __: & gt; PD 1 @ 0x00000330
│ & nbsp; & nbsp; & nbsp; & nbsp; & nbsp; 0x00000330 & NBSP; & nbsp; & nbsp; 4000 & NBSP; & nbsp; & nbsp; & nbsp; & nbsp; lsls __placeholder_54__, __placeholder_55__, 1
__Placeholder_30__

Ми чітко бачимо, що це змінилося. Все, що нам потрібно зробити зараз, - це вихід __placeholder_70__ перетворіть наш __.__ ploadholder_43__ __to __. Uf2__! __Placeholder_31__./elf2uf2/elf2uf2 0x02_hello_world .__ ploadholder_44__ 0x02_hello_world.uf2
__Placeholder_32__

Підключіть Pico __placeholder_71__ Переконайтесь, що ви тримаєте Bootsel __placeholder_47__ Використовуйте налаштування, яку я надав на останньому уроці. __Placeholder_33__cp 0x02_hello_world.uf2 /volumes /rpi-rp2
__Placeholder_34__

Давайте екранимо це! __Placeholder_35__screen /__placeholder_61__/tty.usbmodem00000000001
__Placeholder_36__

Ага так! __Placeholder_37__ у світ! Зламаний світ! Зламаний світ! Зламаний світ! Зламаний світ! Зламаний світ! Зламаний світ! Зламаний світ! Зламаний світ! Зламаний світ! Зламаний світ! Зламаний світ! Зламаний світ! Зламаний світ! Зламаний світ! Зламаний світ! Зламаний світ! Зламаний світ! Зламаний світ! Зламаний світ! Зламаний світ! Зламаний світ! Зламаний світ! Зламаний світ! Зламаний світ! __Placeholder_38__

Кожні півсекунди! Наступний урок ми обговоримо змінні.