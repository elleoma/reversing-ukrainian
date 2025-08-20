## part 31 - Hacking float змінні

Для повного змісту всіх уроків, будь ласка, натисніть нижче, оскільки він дасть короткий короткий урок на додаток до тем, які він висвітлює.&nbsp;xyz9plh9cuk8

Давайте переглянемо наш код.

<pre spellcheck="false">#include &lt;iostream&gt;

&nbsp;

int main(void) {

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; int myNumber = 1337.1;

&nbsp;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; std::cout &lt;&lt; myNumber &lt;&lt; std::endl;

&nbsp;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; return 0;

}
</pre>

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1521799049547.jpg"/></div>

Давайте розглянемо підручник минулого тижня.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1521799097861.jpg"/></div>

Давайте розірвемося на __ -мейн+20__ and, продовжуйте до цього моменту.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1521799125882.jpg"/></div>

Давайте вивчимо, яка цінність знаходиться всередині __R11-8 __. &nbsp;we чітко бачимо, що це __1337.09998__, що наближає наше значення в нашому первісному C ++ код.&nbsp;Keep __1337.1__ Тому, будь ласка, пам’ятайте про це, коли ми йдемо вперед.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1521799166328.jpg"/></div>

Ми також можемо побачити це значення у високій пам'яті.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1521799204709.jpg"/></div>

Давайте розірвемося на __ -мейн+28__ and Продовжуйте.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1521799242840.jpg"/></div>

Ми бачимо нову інструкцію.&nbsp;we див. __Vldr__ and значення в межах __r11, \#8__ переміщується в __ s0 __. &nbsp;so, що таке __s0 __? &nbsp;we має математику. or плаваючі числа.&nbsp;here. AS__ S0__.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1521799279756.jpg"/></div>

Ми можемо бачити ці спеціальні регістри лише в тому випадку, якщо ми робимо інформацію про те, як ми виконуємо всі, як ми робимо нижче.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1521799307421.jpg"/></div>

Нижче ми бачимо, що значення зараз переміщується в __S0__.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1521799331767.jpg"/></div>

Давайте hack!

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1521799362535.jpg"/></div>

Давайте тепер подивимось на реєстри and подивіться, що сталося.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1521799386349.jpg"/></div>

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1521799407513.jpg"/></div>

Як ви бачите, ми зламали значення (менше точній проблемі змінної Float точні до 6 десяткових місць)!

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1521799441419.jpg"/></div>

Нарешті, коли ми продовжуємо, ми бачимо, що наше зламане значення перегукується з терміналом, коли виконується C ++ __cout __function.

Наступного тижня ми зануримося у подвійні змінні.