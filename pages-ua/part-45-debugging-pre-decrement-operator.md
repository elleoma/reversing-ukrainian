## PART 45-Налагодження оператора попереднього декреції

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

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1530270075261.jpg"/></div>

Давайте розірвемося.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1530270088297.jpg"/></div>

Як ми бачимо __R3 __ODS 15. Пам’ятайте, що зламати цю цінність може бути не остаточним місцем, яке воно може зберігатися. Пам'ятайте це на наступному тижні та перегляньте код налагодження вище, щоб побачити, чи зможете ви це зрозуміти.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1530270183626.jpg"/></div>

Як ми бачимо, __R1__ також має 15. Майте на увазі вищезазначене твердження.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1530270209438.jpg"/></div>

Під час продовження ми бачимо, що наша __cout __function переживає 15 для обох областей, як очікувалося.

Наступного тижня ми занурюємось у хакерський оператор попереднього декларації.