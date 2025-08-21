## Частина 38 – Пропрефіксний оператор інкременту

Для повного змісту змісту всіх уроків натисніть нижче, оскільки це надасть вам короткий зміст кожного уроку, а також теми, які будуть розглянуті. https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Наступний етап нашої подорожі – це пропрефіксний оператор інкременту. 

Давайте розглянемо наш код.

<pre spellcheck="false">#include &lt;iostream&gt;

&nbsp;

XyZ9PlH0ZuK8 main(void) {

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; XyZ9PlH1ZuK8 myNumber = 16;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; XyZ9PlH2ZuK8 myNewNumber = ++myNumber;

&nbsp;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; std::cout &lt;&lt; myNewNumber &lt;&lt; std::endl;

&nbsp;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; return 0;

}
</pre>

<XyZ9PlH3ZuK8 class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1526036616866.jpg"/></XyZ9PlH4ZuK8>

Щоб скомпільувати цей код, ми просто набираємо:

g++ example9.cpp -o example9

./example9

<XyZ9PlH5ZuK8 class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1526036640627.jpg"/></XyZ9PlH6ZuK8>

Ми бачимо 17 виведене на екран.

Давайте розберемо це:

Ми створюємо змінну __myNumber = 16__ до якої створюємо ще одну змінну __myNewNumber__ яка пропрефіксно збільшує значення __myNumber__.  Ми бачимо, що коли ми виконуватимемо наш код, воно показуватиме 17.

Коли ми пропрефіксно збільшуваємо значення змінної, вона збільшується перед тим, як бути присвоєна іншій змінній.  Наприклад, __myNumber__ є __16__, тому воно збільшується перед тим, як бути присвоєне __myNewNumber__, тому тому ми отримуємо __17__.

Наступного тижня ми вийдемо на глибину Дебагування Пропрефіксного оператора інкременту.