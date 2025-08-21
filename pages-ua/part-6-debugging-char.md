Частина 6 - Дебагування char

Сьогодні ми дебагуємо програму char. Давайте переглянемо код.

<pre spellcheck="false">#include &lt;stdio.h&gt;
#include "pico/stdlib.h"

int main()&nbsp;
{
&nbsp; stdio_init_all();

&nbsp; while(1)&nbsp;
&nbsp; {
&nbsp; &nbsp; char x = 'x';
&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;
&nbsp; &nbsp; printf("%c\n", x);

&nbsp; &nbsp; sleep_ms(1000);
&nbsp; }
&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;
&nbsp; return 0;
}
</pre>

Давайте запустимо наш дебагер.

<pre spellcheck="false">radare2 -w arm -b 16 0x03_char.XyZ9PlH10ZuK8
</pre>

Давайте зробимо автоматичну аналітику.

<pre spellcheck="false">aaaa
</pre>

Давайте перейдемо до головної частини програми.

<pre spellcheck="false">s main
</pre>

Давайте перейдемо в візуальний режим, натиснувши __V__ і потім __p__ двічі, щоб потрапити до хорошого дебагерського перегляду.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1616704139039.jpg"/></div>

Ми починаємо встановлювати значення повернення головної частини програми.

<pre spellcheck="false">push {r4, lr}
</pre>

Ми викликаємо стандартну ініціалізацію I/O.

<pre spellcheck="false">XyZ9PlH11ZuK8 sym.stdio_init_all
</pre>

Далі ми завантажуємо форматний модифікатор %c у _r4_.

<pre spellcheck="false">ldr r4, [0x0000033c]
</pre>

Ми можемо перевірити це.

<pre spellcheck="false">:&gt; psz @ [0x0000033c]
%c
</pre>

Далі ми завантажуємо символ char _'x'_ у _r1_.

<pre spellcheck="false">movs r1, 0x78
</pre>

https://www.asciitable.com

Ви можете перевірити це на сайті, що 0x78 в шістнадцятковій системі числення є _'x'_.

Далі ми переміщаємо форматний модифікатор у _r0_.

<pre spellcheck="false">movs r0, r4&nbsp;
</pre>

Далі ми здійснюємо стрибок на довгу відстань до printf обгортки і виконуємо її.

<pre spellcheck="false">XyZ9PlH12ZuK8 sym.__wrap_printf

</pre>

Далі ми переміщаємо 250 у десятковій системі числення або 0xfa у шістнадцятковій системі числення у _r0_.

<pre spellcheck="false">movs r0, 0xfa
</pre>

Далі ми переміщаємо 250 у десятковій системі числення, яке ми знаємо, що після логічного зміщення вліво двічі буде 1,000 у десятковій системі числення або 0xfa у шістнадцятковій системі числення у _r0_.

<pre spellcheck="false">lsls r0, r0, 2
</pre>

Далі ми викликаємо функцію sleep\_ms.

<pre spellcheck="false">XyZ9PlH13ZuK8 sym.sleep_ms
</pre>

Далі ми продовжуємо цикл while нескінченно.

<pre spellcheck="false">b 0x328
</pre>

У наступному урокі ми навчимося хакувати тип даних char.