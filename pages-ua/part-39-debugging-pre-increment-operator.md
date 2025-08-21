## Частина 39 – Дебагування оператора попередньої інкрементації

Для повного змісту змісту всіх уроків, будь ласка, натисніть нижче, оскільки це надасть вам короткий зміст кожного уроку, а також теми, які будуть розглянуті. https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Давайте знову розглянемо наш код.

<pre spellcheck="false">#include &lt;iostream&gt;

&nbsp;

int main(void) {

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; int myNumber = 16;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; int myNewNumber = ++myNumber;

&nbsp;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; std::cout &lt;&lt; myNewNumber &lt;&lt; std::endl;

&nbsp;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; return 0;

}
</pre>

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1526639245794.jpg"/></div>

Щоб скомпільувати цей код, ми просто набираємо:

g++ example9.cpp -o example9

./example9

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1526639272084.jpg"/></div>

Ми бачимо 17 виводиться на екран.

Давайте розберемо це:

Ми створюємо змінну __myNumber = 16__ до якої створюємо ще одну змінну __myNewNumber__ яка попередньо збільшує значення __myNumber__.  Ми бачимо, що коли ми виконуватимемо наш код, він показує 17.

Коли ми попередньо збільшуємо значення змінної, воно збільшується до призначення йому іншої змінної.  Наприклад, __myNumber__ є __16__, тому воно збільшується до призначення йому __myNewNumber__ і тому ми отримуємо __17__.

Давайте дебагуємо.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1526639315124.jpg"/></div>

Ми робимо свій звичний старт в gdb і зупиняємося в main.  Зверніть увагу на __main+24__ ми переміщаємо значення __1__ в __r3__.  Потім ми бачимо на __main+28__ ми зберігаємо це значення в __r11-8__ до якої ми встановимо зупинку і продовжимо.

<XyZ9PlH10ZuK8 class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1526639338414.jpg"/></XyZ9PlH11ZuK8>

Під час оцінки значення в __r3__ на цій стадії ми бачимо __17__.  Пам'ятайте, що в нашому оригінальному коді значення змінної __myNumber__ було __16__.  Ми бачимо, що оператор попередньої інкрементації був успішним у збільшенні значення __1__ до надання нам __17__.

<XyZ9PlH12ZuK8 class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1526639366619.jpg"/></XyZ9PlH13ZuK8>

Ми бачимо, що коли ми продовжимо через код, значення __17__ буде успішно виведено в термінал, як очікувалося.

<XyZ9PlH14ZuK8 class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1526639388837.jpg"/></XyZ9PlH15ZuK8>

Наступна неділя ми вийдемо на тему Хакінгу Дебагування Оператора Представної Інкрементації.