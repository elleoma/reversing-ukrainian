Частина 44 – Пропрефіксний операційний декремент

Для повного змісту всіх уроків натисніть нижче, оскільки це надасть вам короткий зміст кожного уроку, а також теми, які будуть розглянуті. https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Давайте розглянемо наш приклад попереднього операційного декременту. Пропрефіксний операційний декремент зменшує задану вартість до виконання дії.

Давайте розглянемо наш код.

<pre spellcheck="false">#include &lt;iostream&gt;

XyZ9PlH0ZuK8 main(void) {
&nbsp;&nbsp; &nbsp;XyZ9PlH1ZuK8 myNumber = 16;
&nbsp;&nbsp; &nbsp;XyZ9PlH2ZuK8 myNewNumber = --myNumber;

&nbsp;&nbsp; &nbsp;std::cout &lt;&lt; myNewNumber &lt;&lt; std::endl;
    std::cout &lt;&lt; myNumber &lt;&lt; std::endl;

&nbsp;&nbsp; &nbsp;return 0;
}
</pre>

<XyZ9PlH3ZuK8 class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1529666614196.jpg"/></XyZ9PlH4ZuK8>

Під час компіляції та виконання ми бачимо 15 виведене в термінал.

<XyZ9PlH5ZuK8 class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1529666685691.jpg"/></XyZ9PlH6ZuK8>

Значення __myNumber __було __16 __і коли воно присвоюється з попереднім операційним декрементом, ми бачимо, що нове значення є __15__ оскільки воно присвоюється до __myNewNumber__.

Наступна неділя ми вийдемо на глибокий аналіз операційного декременту.