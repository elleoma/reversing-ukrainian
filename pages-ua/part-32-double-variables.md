## part 32 - подвійні змінні

Для повного змісту всіх уроків, будь ласка, натисніть нижче, оскільки він дасть короткий короткий урок на додаток до тем, які він висвітлює.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-підручник

Наступний етап нашої подорожі-це змінні з плаваючою точкою з подвійною точністю.&nbsp;

Змінна з плаваючою комою з двома точними відрізняється від змінної з плаваючою комою, оскільки вона має 64-бітну ширину and 15-17 Значні цифри точності.

Давайте розглянемо наш код.

<pre spellcheck="false">#include &lt;iostream&gt;

&nbsp;

int main(void) {

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; double myNumber = 1337.77;

&nbsp;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; std::cout &lt;&lt; myNumber &lt;&lt; std::endl;

&nbsp;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; return 0;

}
</pre>

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1522403579256.jpg"/></div>

Щоб скласти це, ми просто вводимо:

G ++ example7.cpp -o example7

./example7

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1522403604790.jpg"/></div>

Успіх! &nbsp;WE див.

Давайте розберемо його:

Ми присвоюємо змінну з плаваючою комою __ __ безпосередньо у змінну __mynumber __ і потім роздрукуємо її до терміналу за допомогою функції C ++ __cout__.

Наступного тижня ми зануримося в налагодження подвійних змінних.