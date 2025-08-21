## part 3 - налагодження Hello World

Сьогодні ми зануримося в налагодження нашого дуже простого "Привіт Світ!", Програма.

Давайте розглянемо наш код.

<pre spellcheck="false">#include &lt;stdio.h&gt;
#include "pico/stdlib.h"

int main()&nbsp;
{	
&nbsp; stdio_init_all();

&nbsp; while(1)&nbsp;
&nbsp; {
&nbsp;   printf("Hello world!\n");

&nbsp; &nbsp; sleep_ms(1000);
&nbsp; }
    
  return 0;
}
</pre>

Будь ласка, переконайтеся, що ви будуєте Radare2 з джерела. Перед кожним уроком, будь ласка, заповніть наступне.

<pre spellcheck="false">git pull
radare2 sys/install.sh
</pre>

Ви можете перевірити, що версія актуальна.

<pre spellcheck="false">radare2 -v

</pre>

У моєму випадку, оскільки для вас буде інакше.

<pre spellcheck="false">radare2 5.2.0-git 25988 @ darwin-x86-64 git.5.1.1
commit: 510ddab0e523bed173b3954e5f61abf395812f7d build: 2021-03-21__05:40:51
</pre>

Тепер повернемося до нашого проекту репо. Давайте розберемо наш налагоджувач.

<pre spellcheck="false">radare2 -w arm -b 16 0x02_hello_world.elf
</pre>

Давайте автоматично проаналізуємо.

<pre spellcheck="false">aaaa
</pre>

Давайте прагнемо до головного.

<pre spellcheck="false">s main
</pre>

Давайте перейдемо у візуальний режим, ввівши __v__, а потім двічі __p__, щоб дістатися до хорошого подання налагоджувача.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1616343654275.jpg"/></div>

Давайте розберемо цю дуже просту програму.

<pre spellcheck="false">push {r4, lr}
</pre>

Ми просто налаштовуємо наші аргументи функції, де ми натискаємо на значення _R4_ та _LR_ (Реєстр посилань) на стек.

Потім ми bl (гілка довгою) до _sym.stdio \ _init \ _all_ функція, яка стандартний вхід і вихід INIT.

<pre spellcheck="false">bl sym.stdio_init_all
</pre>

Потім ми завантажуємо значення в розташуванні _0x00000338_ в регістр _r4_. Ось де живе, __ "Привіт світ!"

<pre spellcheck="false">ldr r4, [0x00000338]
</pre>

Щоб довести це, ми можемо зробити наступне, натиснувши: всередині поточного візуального режиму, а потім набравши наступне.

<pre spellcheck="false">:&gt; psz @ [0x00000338]
Hello world!
:&gt; psz @ 0x00004cf8
Hello world!
</pre>

Як ви чітко бачите значення всередині _0x00000338 _ є значенням на _0x0004cf8_.

Потім ми переміщуємо і встановлюємо прапори (це _s_ в _movs_) вміст _r4_ в _r0_.

<pre spellcheck="false">movs r0, r4
</pre>

Потім ми розгалужуємось довго до обгортки. Налагоджувач перетворив нашу _printf _function у нашому коді на цю функцію обгортки.

<pre spellcheck="false">bl sym.__wrap_puts
</pre>

Тоді ми _movs _250 десятковий, 0xfa hex, що становить 1/4 наш 1000 мілісекундного сну в _r0_.

<pre spellcheck="false">movs r0, 0xfa
</pre>

Потім ми логічно перемикаємо ліворуч, 2, і встановлюємо прапори. Це, звичайно, помножує наше 250 значення на 2, а потім знову на 2, що займає 250 десяткових до 1000 десяткових знаків, що є нашою мілісекундною затримкою і розміщує це 1000 десяткове значення в _R0_.

<pre spellcheck="false">lsls r0, r0, 2
</pre>

Якщо ви не знайомі з ARM 32 інструкціями збірки, зверніться до цієї чудової таблиці, наданої Keil.

https://developer.arm.com/documentation/ddi0210/c/Introduction/Instruction-set-summary/ARM-instruction-summary?lang=en

Потім ми розгалужуємось довго до нашої функції _sleep \ _ms_.

<pre spellcheck="false">bl sym.sleep_ms
</pre>

Потім ми розгалужуємо безумовну назад до _0x328_, що є нашим циклом.

<pre spellcheck="false">b 0x328
</pre>

Ви також можете побачити перегляд графіка, натиснувши __v__ знову у поточному вікні.

<div class="slate-resizable-image-embed slate-image-embed__resize-middle"><img src="/imgs/1616345144033.jpg"/></div>

Це прекрасний спосіб простежити більш досконалий код. Я хотів показати вам все це, оскільки ви можете використовувати цей рух вперед, коли ви робите більший аналіз.

На нашому наступному уроці ми зламаємо нашу просту програму та перетворимо її на __. UF2__ та повторно розгортається в Піко.