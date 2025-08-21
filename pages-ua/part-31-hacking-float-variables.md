## PART 31 - Змінні зламали плаваючі змінні

Для повного змісту всіх уроків, будь ласка, натисніть нижче, оскільки він дасть короткий короткий урок на додаток до тем, які він висвітлює.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

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

Давайте розійдемося на __ -мейн+20__ і продовжимо до цього моменту.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1521799125882.jpg"/></div>

Давайте вивчимо, яка цінність знаходиться всередині __R11-8 __. &nbsp;WE чітко бачимо, що це __1337.09998__, що наближає наше значення в нашому первісному коді C ++.&nbsp;

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1521799166328.jpg"/></div>

Ми також можемо побачити це значення у високій пам'яті.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1521799204709.jpg"/></div>

Давайте розлучимося на __ -мейн+28__ і продовжимо.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1521799242840.jpg"/></div>

We see a strange new instruction.&nbsp;We see __vldr__ and the value within __r11, \#8__ being moved into__ s0__.&nbsp;So what is __s0__?&nbsp;We have a math co-processor which has a series of additional registers that work with decimal or floating-point числа.&nbsp;here ми бачимо приклад такого, до якого значення __1337.09998 __ є переміщеним у __s0 __. &nbsp;the __vldr__ інструкція завантажує постійну цінність у кожен елемент одноточного або подвійного реєстрації, такого, такого, такого, такого S0__.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1521799279756.jpg"/></div>

Ми можемо бачити ці спеціальні регістри лише в тому випадку, якщо ми робимо інформацію про те, як ми виконуємо всі, як ми робимо нижче.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1521799307421.jpg"/></div>

Нижче ми бачимо, що значення зараз переміщується в __S0__.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1521799331767.jpg"/></div>

Давайте хакемо!

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1521799362535.jpg"/></div>

Давайте тепер подивимось на регістри і подивимось, що сталося.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1521799386349.jpg"/></div>

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1521799407513.jpg"/></div>

Як ви бачите, ми зламали значення (менше точній проблемі змінної Float точні до 6 десяткових місць)!

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1521799441419.jpg"/></div>

Нарешті, коли ми продовжуємо, ми бачимо, що наше зламане значення перегукується з терміналом, коли виконується C ++ __cout __function.

Наступного тижня ми зануримося у подвійні змінні.