## PART 46-Хакерство оператора попередньої декреції

Для повного змісту всіх уроків, будь ласка, натисніть нижче, оскільки він дасть короткий короткий урок на додаток до тем, які він висвітлює.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Давайте переглянемо наш код.

<pre spellcheck="false">#include &lt;iostream&gt;

int main(void) {
&nbsp;&nbsp; &nbsp;int myNumber = 16;
&nbsp;&nbsp; &nbsp;int myNewNumber = --myNumber;

&nbsp;&nbsp; &nbsp;std::cout &lt;&lt; myNewNumber &lt;&lt; std::endl;
    std::cout &lt;&lt; myNumber &lt;&lt; std::endl;

&nbsp;&nbsp; &nbsp;return 0;
}
</pre>

Ми пам’ятаємо, коли компілюємо, отримуємо 15.

Давайте налагоджуємо.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1530875391750.jpg"/></div>

Давайте розірвемося.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1530875474311.jpg"/></div>

Давайте розглянемо, що знаходиться всередині __R3 __ і зламаємо його.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1530875492398.jpg"/></div>

Тепер, як ми продовжуємо, ми бачимо, що це не успішно зламало, чому це?

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1530875528881.jpg"/></div>

Ми повторно запускаємо двійкову та розриваємо і бачимо цінність тут за адресою __r1 __hold __15__.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1530875553276.jpg"/></div>

Коли ми продовжуємо, ми бачимо 15, яких ми не хочемо.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1530875636786.jpg"/></div>

Тепер ми знову ламаємося і роздрукуємо значення.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1530875661356.jpg"/></div>

Цього разу ми встановили __R1__, і ми можемо побачити, що ми успішно зламали!

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1530875673374.jpg"/></div>

Це ваш перший досвід, коли вони дійсно розбивають регістри та бачення, де зберігаються речі та як це може вплинути на результат. Знайдіть час і запустіть це самостійно, щоб ви справді мали міцну ручку з цього приводу.

Наступного тижня ми зануримося в оператор після декреції.