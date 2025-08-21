## part 30 - налагодження змінних поплавків

Для повного змісту всіх уроків, будь ласка, натисніть нижче, оскільки він дасть короткий короткий урок на додаток до тем, які він висвітлює.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

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

Давайте розійдемося на __ -мейн+20__ і продовжимо до цього моменту.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1521196123405.jpg"/></div>

Давайте вивчимо, яка цінність знаходиться всередині __R11-8 __. &nbsp;we чітко бачимо, що це __13337.09998__, що наближає наше значення в нашому первісному c ++ code.&nbsp;, що ми не маємо, що ми не бачимо, що ми не пам’ятаємо. Forward.&nbsp;

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1521196151522.jpg"/></div>

Ми також можемо побачити це значення у високій пам'яті.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1521196178255.jpg"/></div>

Давайте розлучимося на __ -мейн+28__ і продовжимо.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1521196203419.jpg"/></div>

Ми бачимо нову інструкцію.&nbsp;we див. __Vldr__ та значення в межах __r11, \#8__ переміщується в __ s0 __. &nbsp;so Що таке __s0 __? &nbsp;we, що має математику, який має серію додаткових регістерів, які працюють з математикою, або флотуючим, що має низку. числа.&nbsp;here ми бачимо приклад такого, до якого значення __1337.09998 __ є переміщеним у __s0 __. &nbsp;.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1521196373197.jpg"/></div>

Ми можемо бачити ці спеціальні регістри лише в тому випадку, якщо ми робимо інформацію про те, як ми виконуємо всі, як ми робимо нижче.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1521196414932.jpg"/></div>

Нижче ми бачимо, що значення зараз переміщується в __S0__.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1521196439893.jpg"/></div>

Наступного тижня ми зануримось у зламати змінні поплавця.