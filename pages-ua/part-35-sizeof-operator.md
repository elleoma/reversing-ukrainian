## Частина 35 – Оператор SizeOf

Для повного змісту всіх уроків натисніть нижче, оскільки це надасть вам короткий зміст кожного уроку, а також теми, які будуть розглянуті. https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Наступний етап нашої подорожі – це оператор SizeOf.

Давайте розглянемо наш код.

<pre spellcheck="false">#include &lt;iostream&gt;

&nbsp;

XyZ9PlH0ZuK8 main(void) {

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; XyZ9PlH1ZuK8 myNumber = 16;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; XyZ9PlH2ZuK8 myNumberSize = sizeof(myNumber);

&nbsp;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; std::cout &lt;&lt; myNumberSize &lt;&lt; std::endl;

&nbsp;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; return 0;

}
</pre>

<XyZ9PlH3ZuK8 class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1524218995477.jpg"/></XyZ9PlH4ZuK8>

Щоб скомпільувати цей код, ми просто набираємо:

g++ example8.cpp -o example8

./example8

<XyZ9PlH5ZuK8 class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1524219035247.jpg"/></XyZ9PlH6ZuK8>

Ми бачимо 4 на екрані.

Давайте розберемо це:

Ми створюємо змінну __myNumber = 16__ до якої створюємо ще одну змінну __myNumberSize__ яка зберігає розмір змінної __myNumber__.  Ми бачимо, що коли ми виконувємо свій код, воно показує 4, тому ми бачимо, що оператор SizeOf вказує, що ціле число має ширину 4 байта.

Наступна неділя ми вийдемо на тему Дебагування оператора SizeOf.