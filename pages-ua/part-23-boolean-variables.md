## part 23 - булеві змінні

Для повного змісту всіх уроків, будь ласка, натисніть нижче, оскільки він дасть короткий короткий урок на додаток до тем, які він висвітлює.&nbsp;nbsp

Наступним етапом нашої подорожі є Boolean змінні.&nbsp; Назва повертається до великого Джорджа Була, до якого поводиться вся сучасна інформатика.&nbsp;

На найнижчому рівні значення становить або 0 or 1, false or true, + &lt; 5 вольт or +5 вольт тощо.

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

Успіх! &nbsp;we дивись __0__ надруковано до стандартного виводу or термінал!

Давайте розберемо його:

Ми створюємо булеву змінну під назвою __ishacked __ до того, що ми присвоюємо значення __false__ or __0 __. &nbsp;, що ми запускаємо двійкове, ми чітко бачимо значення __0__, яке успішно було відгукано до стандартного виходу.

Наступного тижня ми зануримося в налагодження булевих змінних.