---
{}
---

__Placeholder_35__ Частина 9 - Налагодження __placeholder_52__

Сьогодні ми збираємось налагодити нашу дуже просту програму __placeholder_53__. Давайте розглянемо код.

__0x04 \ _int.c__

__Placeholder_0 __#включити & lt; stdio__placeholder_57 __ & gt;
__Placeholder_36__ включити "pico/stdlib__placeholder_58__"

__Placeholder_54__ main () & nbsp;
{
& nbsp; stdio_init_all ();

& nbsp; в той час як (1) & nbsp;
& nbsp; {
& nbsp; & nbsp; __Placeholder_55__ x = 40; & nbsp;

& nbsp; & nbsp; __Placeholder_61 __ ("%d \ n", x); & nbsp;

& nbsp; & nbsp; Sleep_ms (1000);
& nbsp; }

& nbsp; повернення 0;
}
__Placeholder_1__

Давайте розберемося в нашому налагоджувачі.

__Placeholder_2__radare2 -w __placeholder_63__ -b 16 0x04_int .__ ploadholder_37__
__Placeholder_3__

Давайте автоматично проаналізуємо.

__Placeholder_4__aaaa
__Placeholder_5__

Давайте прагнемо до головного.

__Placeholder_6__s main
__Placeholder_7__

Перейдемо у візуальний режим, ввівши & nbsp; __ v __ & nbsp; __ ploadholder_59__ тоді & nbsp; __ p __ & nbsp; двічі, щоб дістатися до хорошого подання налагоджувача.

__Placeholder_8____Placeholder_9____Placeholder_10__

Ми починаємо з налаштування нашого основного значення повернення.

__Placeholder_11__push {__placeholder_49__, __placeholder_41__}
__Placeholder_12__

Ми __placeholder_46__ стандартний I/O INIT.

__Placeholder_13__bl sym.stdio_init_all
__Placeholder_14__

Потім ми завантажуємо наш модифікатор формату %d в & nbsp; _r4_.

__Placeholder_15__ldr __placeholder_50__, [0x0000033c]
__Placeholder_16__

Ми можемо це довести.

__Placeholder_17 __: & gt; PSZ @ [0x0000033c]
%D
__Placeholder_18__

Потім ми завантажуємо наш __placeholder_56 __ & nbsp; _ '40' _ & nbsp;

__Placeholder_19__movs __placeholder_38__, 0x28
__Placeholder_20__

Ми можемо це довести.

__Placeholder_21 __: & gt; ? 0x28
int32 & nbsp; 40
UINT32 & NBSP; 40
Hex & nbsp; & nbsp; 0x28
восьминог; 050
одиниця & nbsp; & nbsp; 40
сегмент 0000: 0028
рядок & nbsp; "("
FVALUE: 40.0
Float: & nbsp; 0,000000f
Подвійний: 0,000000
Бінарне & nbsp; 0B00101000
Тринарі 0T1111
__Placeholder_22__

Потім ми переміщуємо модифікатор формату в & nbsp; _r0_.

__Placeholder_23__movs __placeholder_42__, __placeholder_51 __ & nbsp;
__Placeholder_24__

Потім ми розгалужуємось довго до __placeholder_62__ обгортка __placeholder_60__ __placeholder_47__ it.

__Placeholder_25__bl sym .__ rap_printf

__Placeholder_26__

Потім ми переміщуємо 250 десятків __placeholder_39__ 0xfa Hex в & nbsp; _r0_.

__Placeholder_27__movs __placeholder_43__, 0xfa
__Placeholder_28__

Потім ми переміщуємо 250 десятків, що знаємо, коли логічний зсув двічі буде 1000 десяткових __placeholder_40__ 0xfa Hex в & nbsp; _r0_.

__Placeholder_29__lsls __placeholder_44__, __placeholder_45__, 2
__Placeholder_30__

Тоді ми __placeholder_48__ Функція Sleep \ _MS.

__Placeholder_31__bl sym.sleep_ms
__Placeholder_32__

Потім ми продовжуємо весь петлю нескінченно.

__Placeholder_33__b 0x328
__Placeholder_34__

На нашому наступному уроці ми зламаємо цей дуже простий двійковий.