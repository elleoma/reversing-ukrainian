Частина 45 – Дебагування оператора попереднього зменшення

Для повного змісту всіх уроків натисніть нижче, оскільки це надасть вам короткий зміст кожного уроку, а також теми, які будуть розглянуті. https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Давайте знову розглянемо свій код.

<pre spellcheck="false">#include &lt;iostream&gt;

int main(void) {
&nbsp;&nbsp; &nbsp;int myNumber = 16;
&nbsp;&nbsp; &nbsp;int myNewNumber = --myNumber;

&nbsp;&nbsp; &nbsp;std::cout &lt;&lt; myNewNumber &lt;&lt; std::endl;
    std::cout &lt;&lt; myNumber &lt;&lt; std::endl;

&nbsp;&nbsp; &nbsp;return 0;
}
</pre>

Пам'ятаємо, коли ми компілюємо, отримуємо 15.

Давайте дебагуємо.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1530270075261.jpg"/></div>

Давайте зупинимося.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1530270088297.jpg"/></div>

Як ми бачимо, __r3 __держить 15. Увага! Хакінг цього значення може не бути останнім місцем, де воно буде зберігатися. Пам'ятайте це на наступну неделю і знову розгляньте дебаговий код вище, щоб спробувати вирішити його.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1530270183626.jpg"/></div>

Як ми бачимо, __r1__ теж містить 15. Увага! Вище заява.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1530270209438.jpg"/></XyZ9PlH10ZuK8>

Продовжуючи, ми бачимо, що наш __cout __функція відтворює 15 для обох областей, як очікувалося.

Наступна неділя ми вийдемо в глибину в хакінг оператора попереднього зменшення.