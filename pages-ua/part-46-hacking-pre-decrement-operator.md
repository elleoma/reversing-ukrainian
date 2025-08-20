## part 46-Hacking попередній оператор

Для повного змісту всіх уроків, будь ласка, натисніть нижче, оскільки він дасть короткий короткий урок на додаток до тем, які він висвітлює.&nbsp;nbsp

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

Давайте розглянемо, що знаходиться всередині __r3 __ та hack it.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1530875492398.jpg"/></div>

Тепер, як ми продовжуємо, ми бачимо, що це зробив not успішно hack, чому це?

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1530875528881.jpg"/></div>

Ми повторно запускаємо двійковий and BREAK and Див. Значення тут за адресою __R1 __Hold __15__.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1530875553276.jpg"/></div>

Коли ми продовжуємо, ми бачимо 15, яких ми не хочемо.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1530875636786.jpg"/></div>

Тепер ми знову ламаємо and надрукувати значення.

nbsp

Цього разу ми встановили __R1__ and, ми можемо побачити, що ми успішно зламали!

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1530875673374.jpg"/></div>

Це ваш перший досвід, коли дійсно розбивають регістри and, бачачи, де зберігаються речі and, як це може впливати на результат. Знайдіть час and запустіть це самостійно, щоб ви справді мали міцну ручку з цього приводу.

Наступного тижня ми зануримося в оператор після декреції.