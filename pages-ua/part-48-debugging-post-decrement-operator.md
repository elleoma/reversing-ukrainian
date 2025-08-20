## PART 48-Налагодження оператора після декреції

Для повного змісту всіх уроків, будь ласка, натисніть нижче, оскільки він дасть короткий короткий урок на додаток до тем, які він висвітлює.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-підручник

Давайте переглянемо наш код.

<pre spellcheck="false">#include &lt;iostream&gt;

int main(void) {
&nbsp;&nbsp; &nbsp;int myNumber = 16;
&nbsp;&nbsp; &nbsp;int myNewNumber = myNumber--;

&nbsp;&nbsp; &nbsp;std::cout &lt;&lt; myNewNumber &lt;&lt; std::endl;
    std::cout &lt;&lt; myNumber &lt;&lt; std::endl;

&nbsp;&nbsp; &nbsp;return 0;
}
</pre>

Ми бачимо наш дуже простий код C ++ вище, до якого ми не робимо нічого іншого, як призначати число у змінну, на яку ми ініціюємо ще одну int змінну and, присвоєні початкову змінну, до якої вона є після декларації. Потім ми виводимо кожне значення до терміналу.

Давайте налагоджуємо.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1532085310684.jpg"/></div>

Зрозуміло, що значення для оператора після декларації завантажується в __R1__ на __main+68 __Sо, давайте розірвемося на __Main+72__.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1532085326445.jpg"/></div>

Ми чітко бачимо, що __R1 __Does насправді має значення __15__, до якого було зменшено від нашої первісної цінності.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1532085443370.jpg"/></div>

Наступного тижня ми зануримось у оператор після декреції Hacking.