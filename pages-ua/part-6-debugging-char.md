Частина 6 - Дебагування char

Сьогодні ми дебагуємо програму char. Давайте переглянемо код.

ХМДХ<pre spellcheck="false">#include &lt;stdio.h&gt;
#include "pico/stdlib.h"

XMDX27c006cc56b1XMDX main()&nbsp;
{
&nbsp; stdio_init_all();

&nbsp; while(1)&nbsp;
&nbsp; {
&nbsp; &nbsp; char x = 'x';
&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;
&nbsp; &nbsp; XMDXf86a742b2f82XMDX("%c
", x);

&nbsp; &nbsp; sleep_ms(1000);
&nbsp; }
&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;
&nbsp; return 0;
}
</pre>ХМДХ

Давайте запустимо наш дебагер.

ХМДХ<pre spellcheck="false">XMDX62b186897c90XMDX -w XMDX27c475ab84b0XMDX -b 16 0x03_char.XMDX58f4224c1872XMDX
</pre>ХМДХ

Давайте зробимо автоматичний аналіз.

ХМДХ<pre spellcheck="false">aaaa
</pre>ХМДХ

Давайте перейдемо до головної частини програми.

ХМДХ<pre spellcheck="false">s main
</pre>ХМДХ

Давайте перейдемо в візуальний режим, натиснувши __V__ і потім __p__ двічі, щоб потрапити в добре підходящий дебагерський вигляд.

ХМДХ<XMDX9dd804ecc721XMDX class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1616704139039.jpg"/></XMDX07c1fb0c54aaXMDX>ХМДХ

Ми починаємо встановлювати значення повернення головної частини програми.

ХМДХ<pre spellcheck="false">push {r4, lr}
</pre>ХМДХ

Ми викликаємо стандартну ініціалізацію I/O.

ХМДХ<pre spellcheck="false">XMDXd52fb0592f8cXMDX sym.stdio_init_all
</pre>ХМДХ

Далі ми завантажуємо форматний модифікатор %c в _r4_.

ХМДХ<pre spellcheck="false">ldr r4, [0x0000033c]
</pre>ХМДХ

Ми можемо перевірити його.

ХМДХ<pre spellcheck="false">:&gt; psz @ [0x0000033c]
%c
</pre>ХМДХ

Далі ми завантажуємо символ char _'x'_ в _r1_.

ХМДХ<pre spellcheck="false">movs r1, 0x78
</pre>ХМДХ

ХМДХhttps://www.asciitable.comХМДХ

Ви можете перевірити на сайті, що 0x78 в шістнадцятковій системі є _'x'_.

Далі ми переміщаємо форматний модифікатор в _r0_.

ХМДХ<pre spellcheck="false">movs r0, r4&nbsp;
</pre>ХМДХ

Далі ми здійснюємо стрибок на велику відстань до обгортки printf і виконуємо її.

ХМДХ<pre spellcheck="false">XMDX665cb8fe8415XMDX sym.__wrap_printf

</pre>ХМДХ

Далі ми переміщаємо 250 у десятичній системі або 0xfa в шістнадцятковій системі в _r0_.

ХМДХ<pre spellcheck="false">movs r0, 0xfa
</pre>ХМДХ

Далі ми переміщаємо 250 у десятичній системі, яке ми знаємо, що після логічного зміщення вліво двічі буде 1,000 у десятичній системі або 0xfa в шістнадцятковій системі в _r0_.

ХМДХ<pre spellcheck="false">lsls r0, r0, 2
</pre>ХМДХ

Далі ми викликаємо функцію sleep\_ms.

ХМДХ<pre spellcheck="false">XMDX67187dbd89d6XMDX sym.sleep_ms
</pre>ХМДХ

Далі ми продовжуємо цикл while нескінченно.

ХМДХ<pre spellcheck="false">b 0x328
</pre>ХМДХ

У наступному урокі ми навчимося хакувати тип даних char.