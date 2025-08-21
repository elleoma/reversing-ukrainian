## part 6 - налагодження char

Сьогодні ми налагоджуємо програму CHAR. Давайте розглянемо код.

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

Давайте розберемо наш налагоджувач.

<pre spellcheck="false">radare2 -w arm -b 16 0x03_char.elf
</pre>

Давайте автоматично проаналізуємо.

<pre spellcheck="false">aaaa
</pre>

Давайте прагнемо до головного.

<pre spellcheck="false">s main
</pre>

Давайте перейдемо у візуальний режим, typing&nbsp;__v__&nbsp;and then&nbsp;__p__&nbsp;twice, щоб дістатися до хорошого виду налагоджувача.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1616704139039.jpg"/></div>

Ми починаємо з налаштування нашого основного значення повернення.

<pre spellcheck="false">push {r4, lr}
</pre>

Ми call стандартний init init.

<pre spellcheck="false">bl sym.stdio_init_all
</pre>

Потім ми завантажуємо наш модифікатор формату %C в _R4_.

<pre spellcheck="false">ldr r4, [0x0000033c]
</pre>

Ми можемо це довести.

<pre spellcheck="false">:&gt; psz @ [0x0000033c]
%c
</pre>

Потім ми завантажуємо наш char _'x'_ в _r1_.

<pre spellcheck="false">movs r1, 0x78
</pre>

https://www.asciitable.com

Ви можете перевірити вище, що 0x78 HEX - це _'x'_.

Потім ми переміщуємо модифікатор формату в _R0_.

<pre spellcheck="false">movs r0, r4&nbsp;
</pre>

Потім ми розгалужуємось довго до обгортки printf та call it.

<pre spellcheck="false">bl sym.__wrap_printf

</pre>

Потім ми переміщуємо 250 десяткових або 0xfa HEX в _R0_.

<pre spellcheck="false">movs r0, 0xfa
</pre>

Потім ми переміщуємо 250 десятків, що знаємо, коли логічний зсув двічі буде 1000 десяткових або 0xfa HEX у _R0_.

<pre spellcheck="false">lsls r0, r0, 2
</pre>

Тоді ми call функція sleep \ _ms.

<pre spellcheck="false">bl sym.sleep_ms
</pre>

Потім ми продовжуємо весь петлю нескінченно.

<pre spellcheck="false">b 0x328
</pre>

На нашому наступному уроці ми зламаємо тип даних CHAR.