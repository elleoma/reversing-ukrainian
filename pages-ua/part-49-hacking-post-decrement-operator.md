## PART 49-Злом оператора після декреції

Для повного змісту всіх уроків, будь ласка, натисніть нижче, оскільки він дасть короткий короткий урок на додаток до тем, які він висвітлює.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Давайте ще раз переглянемо наш код.

<pre spellcheck="false">#include &lt;iostream&gt;

int main(void) {
&nbsp;&nbsp; &nbsp;int myNumber = 16;
&nbsp;&nbsp; &nbsp;int myNewNumber = myNumber--;

&nbsp;&nbsp; &nbsp;std::cout &lt;&lt; myNewNumber &lt;&lt; std::endl;
    std::cout &lt;&lt; myNumber &lt;&lt; std::endl;

&nbsp;&nbsp; &nbsp;return 0;
}
</pre>

Давайте розглянемо налагодження минулого тижня.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1532690049930.jpg"/></div>

Як ми бачимо тут, значення в __R1__ при __ -мейн+68__ є __15__. Давайте хакемо!

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1532690140517.jpg"/></div>

Ще раз ми маніпулювали та змінили виконання програми на власні торги. З кожним із цих уроків розміру укусу ви продовжуєте краще зрозуміти процесора та як він взаємодіє з двійковою.

Я сподіваюся, що ця серія дає вам міцну основу для розуміння процесора ARM. Це завершує серію. Дякую всім за те, що ви прийшли в подорож!