---
{}
---

__Placeholder_31__ Частина 10 - Злом __placeholder_46__

Сьогодні ми зламаємо нашу просту програму __placeholder_47__. Давайте розглянемо код.

__0x04 \ _int.c__

__Placeholder_0 __#включає & lt; stdio__placeholder_51 __ & gt;
__Placeholder_32__ включити "pico/stdlib__placeholder_52__"

__Placeholder_48__ main () & nbsp;
{
& nbsp; stdio_init_all ();

& nbsp; в той час як (1) & nbsp;
& nbsp; {
& nbsp; & nbsp; __Placeholder_49__ x = 40; & nbsp;

& nbsp; & nbsp; __Placeholder_61 __ ("%d \ n", x); & nbsp;

& nbsp; & nbsp; Sleep_ms (1000);
& nbsp; }

& nbsp; повернення 0;
}
__Placeholder_1__

Давайте розберемося в нашому налагоджувачі.

__Placeholder_2__radare2 -w __placeholder_63__ -b 16 0x04_int .__ ploadholder_33__
__Placeholder_3__

Давайте автоматично проаналізуємо.

__Placeholder_4__aaaa
__Placeholder_5__

Давайте прагнемо до головного.

__Placeholder_6__s main
__Placeholder_7__

Перейдемо у візуальний режим, ввівши & nbsp; __ v __ & nbsp; __ ploadholder_54__ тоді & nbsp; __ p __ & nbsp; двічі, щоб дістатися до хорошого подання налагоджувача.

__Placeholder_8____Placeholder_9____Placeholder_10__

Ми збираємось спочатку зламати значення __placeholder_50__, яке ми знаємо, це _40_ десятковий __placeholder_38__ _28_ hex.

__Placeholder_11 __: & gt; wa movs __placeholder_36__, 0x30 @ 0x00000328
Написано 2 байти (S) (MOVS __placeholder_37__, 0x30) = WX 3021
__Placeholder_12__

Тут ми бачимо _0x30_ IS _48_ десятковий.

__Placeholder_13 __: & gt; ? 0x30
int32 & nbsp; 48
UINT32 & NBSP; 48
Hex & nbsp; & nbsp; 0x30
восьминог; 060
одиниця & nbsp; & nbsp; 48
Сегмент 0000: 0030
рядок & nbsp; "0"
Fvalue: 48.0
Float: & nbsp; 0,000000f
Подвійний: 0,000000
Бінарне & nbsp; 0B00110000
Тринар 0T1210
__Placeholder_14__

Ми також бачимо, що _0xfa_, який ми знаємо, це _250_ десятковий - це наша 1/4 мілісекундна затримка, що, коли зміщена ліворуч, множиться, __placeholder_55__ стає _1000_ десяткове протягом 1 секунди затримки.

__Placeholder_15 __: & gt; ? 0xfa
int32 & nbsp; 250
UINT32 & NBSP; 250
Hex & nbsp; & nbsp; 0xfa
восьминог; 0372
одиниця & nbsp; & nbsp; 250
сегмент 0000: 00FA
рядок & nbsp; "\ xfa"
FVALUE: 250.0
Float: & nbsp; 0,000000f
Подвійний: 0,000000
Бінарне & nbsp; 0B11111010
Тринарі 0T100021
__Placeholder_16__

Давайте зламаємо це на _50_ десятковий.

__Placeholder_17 __: & gt; wa movs __placeholder_40__, 0x32 @ 0x00000330
Написано 2 байти (и) (MOVS __placeholder_41__, 0x32) = WX 3220
__Placeholder_18__

Ми можемо бачити, що це насправді _50_ десятковий.

__Placeholder_19 __: & gt; ? 0x32
int32 & nbsp; 50
UINT32 & NBSP; 50
Hex & nbsp; & nbsp; 0x32
восьминог; 062
одиниця & nbsp; & nbsp; 50
сегмент 0000: 0032
рядок & nbsp; "2"
fvalue: 50.0
Float: & nbsp; 0,000000f
Подвійний: 0,000000
Бінарне & nbsp; 0B00110010
Тринарі 0T1212
__Placeholder_20__

Давайте також змінимо його лише один раз таким, що він знадобиться _50_ десятковий __placeholder_56__, перетворивши його на _100_, коли він зміщує ліворуч лише один раз.

__Placeholder_21 __: & gt; wa lsls __placeholder_42__, __placeholder_43__, 1 @ 0x00000332
Написано 2 байти (lsls __placeholder_44__, __placeholder_45__, 1) = WX 4000
__Placeholder_22__

Все, що нам потрібно зробити зараз, - це вихід __placeholder_57__ перетворіть нашу & nbsp; __.__ ploadholder_34 __ & nbsp; __ до & nbsp; __. Uf2__!

__Placeholder_23__./elf2uf2/elf2uf2 0x04_int .__ ploadholder_35__ 0x04_int.uf2
__Placeholder_24__

Підключіть Pico __placeholder_58__ Переконайтесь, що ви тримаєте завантаження __placeholder_39__ Використовуйте налаштування, яку я надав у частині 2.

__Placeholder_25__cp 0x04_int.uf2 /томи /rpi-rp2
__Placeholder_26__

Давайте екранимо це!

__Placeholder_27__screen /__placeholder_53__/tty.usbmodem00000000001
__Placeholder_28__

Ага так!

__Placeholder_29__48
48
48
48
48
48
48
48
48
48
48
48
48
48
48
48
48
48
48
48
__Placeholder_30__

Тут ми бачимо, що ми зламали його до 48 десяткових __placeholder_59__ Він друкує кожні 100 мілісекунд!

На нашому наступному уроці ми будемо мати справу з поплавками __placeholder_60__ унікальний спосіб, яким Піко обробляє їх, як це робить __placeholder_62__, має співпроцесор.