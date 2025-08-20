## PART 44-Оператор попередньої декреції

Для повного змісту всіх уроків, будь ласка, натисніть нижче, оскільки він дасть короткий короткий урок на додаток до тем, які він висвітлює.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-підручник

Давайте подивимось на наш приклад попереднього оператора. Оператор попереднього декларації зменшує задане значення до призначення дії.

Давайте розглянемо наш код.

<pre spellcheck="false">#include &lt;iostream&gt;

int main(void) {
&nbsp;&nbsp; &nbsp;int myNumber = 16;
&nbsp;&nbsp; &nbsp;int myNewNumber = --myNumber;

&nbsp;&nbsp; &nbsp;std::cout &lt;&lt; myNewNumber &lt;&lt; std::endl;
    std::cout &lt;&lt; myNumber &lt;&lt; std::endl;

&nbsp;&nbsp; &nbsp;return 0;
}
</pre>

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1529666614196.jpg"/></div>

Коли ми складаємо and запускати, ми бачимо, що 15 перегукуються до терміналу.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1529666685691.jpg"/></div>

Значення __mynumber __ було __16 __ та коли воно призначено оператору попередньої декларації, ми бачимо, що нове значення становить __15__, оскільки воно присвоюється __mynewnumber__.

Наступного тижня ми зануримося в оператор попередньої декларації налагодження.