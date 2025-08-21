Частина 41 – Оператор післяінкременту

Для повного змісту всіх уроків натисніть нижче, оскільки це надасть вам короткий зміст кожного уроку, а також теми, які будуть розглянуті. https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Давайте підійдемо до нашого коду.

<pre spellcheck="false">#include &lt;iostream&gt;

XyZ9PlH0ZuK8 main(void) {
&nbsp;&nbsp; &nbsp;XyZ9PlH1ZuK8 myNumber = 16;
&nbsp;&nbsp; &nbsp;XyZ9PlH2ZuK8 myNewNumber = ++myNumber;

&nbsp;&nbsp; &nbsp;std::cout &lt;&lt; myNewNumber &lt;&lt; std::endl;

&nbsp;&nbsp; &nbsp;return 0;
}
</pre>

<XyZ9PlH3ZuK8 class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1527849027049.jpg"/></XyZ9PlH4ZuK8>

Щоб скомпільувати цей код, ми просто набираємо:

g++ example10.cpp -o example10

./example10

<XyZ9PlH5ZuK8 class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1527849063244.jpg"/></XyZ9PlH6ZuK8>

Ми бачимо 16 і 17 виведені на екран.

Давайте розберемо це:

Ми створюємо змінну __myNumber = 16__ до якої створюємо ще одну змінну __myNewNumber__ яка післяінкрементує значення змінної __myNumber__.  Бачимо, що коли ми виконуватимемо наш код, воно показуватиме __16__ як значення змінної __myNewNumber__ і __17__ як значення змінної __myNumber__ оскільки змінна __myNewNumber__ не збільшується, оскільки тільки змінна __myNumber__ збільшується, оскільки вона є післяоператором.

Коли ми післяінкрементуємо значення змінної, воно збільшується після призначення йому іншої змінної.  Наприклад, змінна __myNumber__ має значення __16__, тому вона збільшується після призначення їй змінної __myNewNumber__, тому ми отримуємо __17__.

Наступна неділя ми підійдемо до Розробки Оператора післяінкременту.