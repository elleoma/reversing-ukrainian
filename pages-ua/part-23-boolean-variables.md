## part 23 - булеві змінні

Для повного змісту всіх уроків, будь ласка, натисніть нижче, оскільки він дасть короткий короткий урок на додаток до тем, які він висвітлює.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Наступний етап нашої подорожі - це булева змінні.&nbsp; Назва повертається до великого Джорджа Була, до якого походить усі сучасні інформатики.&nbsp;

На найнижчому рівні значення становить або 0, або 1, помилкове, або справжнє, + &lt; 5 вольт або +5 вольт тощо.

Давайте розглянемо наш код.

<pre spellcheck="false">#include &lt;iostream&gt;

&nbsp;

int main(void) {

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; bool isHacked = false;

&nbsp;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; std::cout &lt;&lt; isHacked &lt;&lt; std::endl;

&nbsp;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; return 0;

}
</pre>

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520192758105.jpg"/></div>

Щоб скласти це, ми просто вводимо:

<pre spellcheck="false">g++ example4.cpp -o example4

./example4
</pre>

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520196655358.jpg"/></div>

Успіх! &nbsp;we бачимо __0__ надруковано до стандартного виходу або терміналу!

Давайте розберемо його:

Ми створюємо булеву змінну під назвою __ishacked __ до того, що ми присвоюємо значення __false__ або __0 __. &nbsp;, коли ми запускаємо двійкове, ми чітко бачимо значення __0__, яке успішно було перегукується з стандартним результатом.

Наступного тижня ми зануримося в налагодження булевих змінних.