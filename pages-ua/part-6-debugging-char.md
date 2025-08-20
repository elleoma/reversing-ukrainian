---
{}
---

__Placeholder_34__ Частина 6 - Налагодження Чар

Сьогодні ми налагоджуємо програму CHAR. Давайте розглянемо код.

__Placeholder_0 __#включити & lt; stdio__placeholder_52 __ & gt;
__Placeholder_35__ включають "pico/stdlib__placeholder_53__"

__Placeholder_51__ main () & nbsp;
{
& nbsp; stdio_init_all ();

& nbsp; в той час як (1) & nbsp;
& nbsp; {
& nbsp; & nbsp; char x = 'x';
& nbsp; & nbsp; & nbsp; & nbsp; & nbsp;
& nbsp; & nbsp; __Placeholder_56 __ ("%c \ n", x);

& nbsp; & nbsp; Sleep_ms (1000);
& nbsp; }
& nbsp; & nbsp; & nbsp; & nbsp; & nbsp;
& nbsp; повернення 0;
}
__Placeholder_1__

Давайте розберемо наш налагоджувач.

__Placeholder_2__radare2 -w __placeholder_58__ -b 16 0x03_char .__ ploadholder_36__
__Placeholder_3__

Давайте автоматично проаналізуємо.

__Placeholder_4__aaaa
__Placeholder_5__

Давайте прагнемо до головного.

__Placeholder_6__s main
__Placeholder_7__

Перейдемо у візуальний режим, ввівши & nbsp; __ v __ & nbsp; __ ploadholder_54__ тоді & nbsp; __ p __ & nbsp; двічі, щоб дістатися до хорошого подання налагоджувача.

__Placeholder_8____Placeholder_9____Placeholder_10__

Ми починаємо з налаштування нашого основного значення повернення.

__Placeholder_11__push {__placeholder_48__, __placeholder_40__}
__Placeholder_12__

Ми __placeholder_45__ стандартний I/O INIT.

__Placeholder_13__bl sym.stdio_init_all
__Placeholder_14__

Потім ми завантажуємо наш модифікатор формату %C в _R4_.

__Placeholder_15__ldr __placeholder_49__, [0x0000033c]
__Placeholder_16__

Ми можемо це довести.

__Placeholder_17 __: & gt; PSZ @ [0x0000033c]
%c
__Placeholder_18__

Потім ми завантажуємо наш char _'x'_ в _r1_.

__Placeholder_19__movs __placeholder_37__, 0x78
__Placeholder_20__

__Placeholder_33__

Ви можете перевірити вище, що 0x78 Hex - _'x'_.

Потім ми переміщуємо модифікатор формату в _R0_.

__Placeholder_21__movs __placeholder_41__, __placeholder_50 __ & nbsp;
__Placeholder_22__

Потім ми розгалужуємось довго до __placeholder_57__ обгортка __placeholder_55__ __placeholder_46__ it.

__Placeholder_23__bl sym .__ wrap_printf

__Placeholder_24__

Потім ми переміщуємо 250 десятків __placeholder_38__ 0xfa HEX в _R0_.

__Placeholder_25__movs __placeholder_42__, 0xfa
__Placeholder_26__

Потім ми переміщуємо 250 десяткових знаків, що ми знаємо, коли логічний зсув двічі буде 1000 десятків __placeholder_39__ 0xfa Hex в _R0_.

__Placeholder_27__lsls __placeholder_43__, __placeholder_44__, 2
__Placeholder_28__

Тоді ми __placeholder_47__ Функція Sleep \ _MS.

__Placeholder_29__bl sym.sleep_ms
__Placeholder_30__

Потім ми продовжуємо весь петлю нескінченно.

__Placeholder_31__b 0x328
__Placeholder_32__

На нашому наступному уроці ми зламаємо тип даних CHAR.