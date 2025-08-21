## Частина 26 – Цілі змінні

Для повного змісту змісту всіх уроків натисніть нижче, оскільки це надасть вам короткий зміст кожного уроку, а також теми, які будуть обговорені. https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Наступний етап нашої подорожі – цілі змінні.

32-бітний регістр може зберігати 2^32 різні значення. Варіант цілих значень, які можна зберігати в 32 бітах, залежить від використовуваної представлення цілих чисел. З двох найбільш поширених представлень діапазон становить від 0 до 4 294 967 295 (2^32 − 1) для представлення як беззнакового бінарного числа, а від −2 147 483 648 (−2^31) до 2 147 483 647 (2^31 − 1) для представлення за допомогою двійкового доповнення.

Увага! З 32-бітними адресами пам'яті можна безпосередньо звертатися до максимально можливої кількості 4 ГБ адресованої пам'яті за байтами.

Давайте розглянемо наш код.

<pre spellcheck="false">#include &lt;iostream&gt;

&nbsp;

XyZ9PlH0ZuK8 main(void) {

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; XyZ9PlH1ZuK8 myNumber = 777;

&nbsp;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; std::cout &lt;&lt; myNumber &lt;&lt; std::endl;

&nbsp;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; return 0;

}
</pre>

<XyZ9PlH2ZuK8 class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520215369999.jpg"/></XyZ9PlH3ZuK8>

Для компіляції цього ми просто набираємо:

g++ example5.cpp -o example5

./example5

<XyZ9PlH4ZuK8 class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520195285687.jpg"/></XyZ9PlH5ZuK8>

УСПІШНО!  Ми бачимо __777__ виведене на стандартний вивід або термінал!

Давайте розберемо це:

Ми призначаємо ціле число __777 __ безпосередньо змінній __myNumber __ і потім друкуємо його на термінал за допомогою функції c++ __cout__.

Наступна неділя ми вийдемо на тему Дебагування цілих змінних.