Частина 3 - Дебагування "Hello World"

Сьогодні ми візьмемося за дебагування нашого дуже простого програми "Hello world!".

Давайте переглянемо наш код.

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

Будь ласка, переконайтеся, що збудували Radare2 з джерела. До кожного уроку, БУДЬ ЛАСКА, виконайте наступні дії.

<pre spellcheck="false">git pull
radare2 sys/install.XyZ9PlH21ZuK8
</pre>

Ви можете перевірити, чи версія є актуальною.

<pre spellcheck="false">radare2 -v

</pre>

У моїй ситуації, як і у вас.

<pre spellcheck="false">radare2 5.2.0-git 25988 @ darwin-x86-64 git.5.1.1
commit: 510ddab0e523bed173b3954e5f61abf395812f7d build: 2021-03-21__05:40:51
</pre>

Тепер поверніться до нашого проекту репозиторію. Давайте запустимо наш дебагер.

<pre spellcheck="false">radare2 -w arm -b 16 0x02_hello_world.XyZ9PlH16ZuK8
</pre>

Давайте зробимо аналіз автоматично.

<pre spellcheck="false">aaaa
</pre>

Давайте спробуємо потрапити до головної частини програми.

<pre spellcheck="false">s main
</pre>

Давайте перейдемо до візуального режиму, натиснувши __V__ і потім __p__ двічі, щоб потрапити до хорошого режиму дебагування.

<XyZ9PlH12ZuK8 class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1616343654275.jpg"/></XyZ9PlH13ZuK8>

Давайте розіб'ємо цю дуже просту програму.

<pre spellcheck="false">push {r4, lr}
</pre>

Ми просто встановлюємо аргументи своєї функції, де ми відправляємо значення _r4_ і _lr_ (регистр зв'язку) на стік.

Далі ми здійснюємо перехід до _sym.stdio\_init\_all_ функції, яка ініціалізує стандартний вхід і вихід.

<pre spellcheck="false">XyZ9PlH18ZuK8 sym.stdio_init_all
</pre>

Далі ми завантажуємо значення в місці _0x00000338_ в регистр _r4_. Це місце, де знаходиться рядок __"Hello world!"__.

<pre spellcheck="false">ldr r4, [0x00000338]
</pre>

Щоб підтвердити це, ми можемо виконати наступні дії, натиснувши : всередині поточного візуального режиму і потім натиснувши наступні команди.

<pre spellcheck="false">:&gt; psz @ [0x00000338]
Hello world!
:&gt; psz @ 0x00004cf8
Hello world!
</pre>

Як ви можете побачити, значення всередині _0x00000338_ є тим же значенням, що і в місці _0x0004cf8_.

Далі ми переміщаємо і встановлюємо флаги (тобто _s_ в _movs_) вміст _r4_ в _r0_.

<pre spellcheck="false">movs r0, r4
</pre>

Далі ми здійснюємо перехід до функції puts-обгортки. Дебагер перетворив нашу _printf_ функцію в нашому коді на цю обгорткову функцію.

<pre spellcheck="false">XyZ9PlH19ZuK8 sym.__wrap_puts
</pre>

Далі ми здійснюємо _movs_ 250 десятичне, 0xfa шістнадцятне, яке є 1/4 нашим 1000 мілісекундним сповільненням в _r0_.

<pre spellcheck="false">movs r0, 0xfa
</pre>

Далі ми логічно зміщуємо ліворуч, 2, і встановлюємо флаги. Це, звичайно, збільшує наше значення 250 на 2 і знову на 2, що робить 250 десятичне 1000 десятичне, яке є нашим мілісекундним затримкою і встановлює це значення 1000 десятичного в _r0_.

<pre spellcheck="false">lsls r0, r0, 2
</pre>

Якщо ви незнайомі з інструкціями ARM 32-ї збірки, будь ласка, зверніться до цієї чудової таблиці, наданої Keil.

https://developer.XyZ9PlH10ZuK8.com/documentation/ddi0210/c/Introduction/Instruction-set-summary/XyZ9PlH11ZuK8-instruction-summary?lang=en

Далі ми здійснюємо перехід до нашої функції _sleep\_ms_.

<pre spellcheck="false">XyZ9PlH20ZuK8 sym.sleep_ms
</pre>

Далі ми здійснюємо перехід безумовно назад до _0x328_, яке є нашою циклічною стрічкою.

<pre spellcheck="false">b 0x328
</pre>

Ви також можете побачити графічний режим, натиснувши __V__ знову в поточному вікні.

<XyZ9PlH14ZuK8 class="slate-resizable-image-embed slate-image-embed__resize-middle"><img src="/imgs/1616345144033.jpg"/></XyZ9PlH15ZuK8>

Це чудовий спосіб слідкувати за більш складним кодом. Я хотів показати вам це, оскільки ви зможете використовувати це далі, коли виконуватимете більші аналіз.

У наступному урокі ми змінимо нашу просту програму і перетворимо її знову на __.uf2__ і знову перезавантажимо на Pico.