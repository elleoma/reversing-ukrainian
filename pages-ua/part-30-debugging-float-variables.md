## part 30 - Змінні налагодження поплавців

Для повного змісту всіх уроків, будь ласка, натисніть нижче, оскільки він дасть короткий короткий урок на додаток до тем, які він висвітлює.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-підручник

Давайте переглянемо наш код.

<pre spellcheck="false">#include &lt;iostream&gt;

&nbsp;

int main(void) {

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; float myNumber = 1337.1;

&nbsp;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; std::cout &lt;&lt; myNumber &lt;&lt; std::endl;

&nbsp;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; return 0;

}
</pre>

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1521196070985.jpg"/></div>

Давайте налагоджуємо!

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1521196099167.jpg"/></div>

Давайте розійдемося на __ -мейн+20__ and, продовжуйте до цього моменту.

nbsp

Давайте вивчимо, яка цінність знаходиться всередині __R11-8 __. &nbsp;WE чітко бачимо, що це __13337.09998__, що наближає наше значення в нашому первісному C ++ код.&nbsp;keep __1337.1__ Тому, будь ласка, пам’ятайте, що ми рухаємось вперед.&nbsp;

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1521196151522.jpg"/></div>

Ми також можемо побачити це значення у високій пам'яті.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1521196178255.jpg"/></div>

Давайте розірвемося на __main+28__ and.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1521196203419.jpg"/></div>

We see a strange new інструкція.&nbsp;We see __vldr__ and the value within __r11, \#8__ being moved into__ s0__.&nbsp;So what is __s0__?&nbsp;We have a math co-processor which has a series of additional registers that work with decimal or з плаваючою коімом &nbsp;here ми бачимо приклад такого, до якого значення __1337.09998 __is переміщується в __s0 __. &nbsp; __vldr__ regindric reginism reginisc8 AS__ S0__.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1521196373197.jpg"/></div>

Ми можемо бачити ці спеціальні регістри лише в тому випадку, якщо ми робимо інформацію про те, як ми виконуємо всі, як ми робимо нижче.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1521196414932.jpg"/></div>

Нижче ми бачимо, що значення зараз переміщується в __S0__.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1521196439893.jpg"/></div>

На наступному тижні ми зануримось у змінні FLOAT Hacking.