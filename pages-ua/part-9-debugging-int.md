## part 9 - налагодження int

Сьогодні ми збираємось налагодити нашу дуже просту програму int. Давайте розглянемо код.

__0x04 \ _int.c__

<pre spellcheck="false">#include &lt;stdio.h&gt;
#include "pico/stdlib.h"

int main()&nbsp;
{
&nbsp; stdio_init_all();

&nbsp; while(1)&nbsp;
&nbsp; {
&nbsp; &nbsp; int x = 40;&nbsp;

&nbsp; &nbsp; printf("%d\n", x);&nbsp;

&nbsp; &nbsp; sleep_ms(1000);
&nbsp; }

&nbsp; return 0;
}
</pre>

Давайте розберемося в нашому налагоджувач.

<pre spellcheck="false">radare2 -w arm -b 16 0x04_int.elf
</pre>

Давайте автоматично проаналізуємо.

<pre spellcheck="false">aaaa
</pre>

Давайте прагнемо main.

<pre spellcheck="false">s main
</pre>

Перейдемо у візуальний режим, typing&nbsp;__v__&nbsp;and then&nbsp;__p__&nbsp;twice, щоб дістатися до хорошого налагоджувач виду.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1617350497179.jpg"/></div>

Ми починаємо з налаштування значення повернення main.

nbsp

Ми call стандартний init init.

<pre spellcheck="false">bl sym.stdio_init_all
</pre>

Потім ми завантажуємо наш формат модифікатор %d OFOSS9PLH90ZUK8_R4_.

<pre spellcheck="false">ldr r4, [0x0000033c]
</pre>

Ми можемо це довести.

<pre spellcheck="false">:&gt; psz @ [0x0000033c]
%d
</pre>

Потім ми завантажуємо наш int&nbsp;_'40'_&nbsp;INTO&nbsp;_R1 _ Чим _0x28_ hex.

<pre spellcheck="false">movs r1, 0x28
</pre>

Ми можемо це довести.

nbsp

Потім ми переміщуємо модифікатор формату Of&nbsp;_r0_.

<pre spellcheck="false">movs r0, r4&nbsp;
</pre>

Потім ми розгалужуємось довго до обгортки printf and call it.

<pre spellcheck="false">bl sym.__wrap_printf

</pre>

Потім ми переміщуємо 250 десятків or 0xfa hex of&nbsp;_r0_.

<pre spellcheck="false">movs r0, 0xfa
</pre>

Потім ми переміщуємо 250 десятків, що знаємо, коли логічний зсув двічі буде 1000 десяткових десятків or 0xfa hex th&nbsp;_r0_.

<pre spellcheck="false">lsls r0, r0, 2
</pre>

Тоді ми call Функція Sleep \ _MS.

<pre spellcheck="false">bl sym.sleep_ms
</pre>

Потім ми продовжуємо весь петлю нескінченно.

<pre spellcheck="false">b 0x328
</pre>

На нашому наступному уроці ми будемо hack цей дуже простий двійковий.