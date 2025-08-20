## part 29 - float змінні

Для повного змісту всіх уроків, будь ласка, натисніть нижче, оскільки він дасть короткий короткий урок на додаток до тем, які він висвітлює.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-підручник

Наступний етап нашої подорожі-це змінні з плаваючою комою.&nbsp;

Змінна з плаваючою комою відрізняється від цілого числа, оскільки вона має дробове значення, яке ми позначаємо з періодом.

Давайте розглянемо наш код.

<pre spellcheck="false">#include &lt;iostream&gt;

&nbsp;

float main(void) {

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; int myNumber = 1337.1;

&nbsp;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; std::cout &lt;&lt; myNumber &lt;&lt; std::endl;

&nbsp;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; return 0;

}
</pre>

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520592872663.jpg"/></div>

Щоб скласти це, ми просто вводимо:

g ++ example6.cpp -o example6

./example6

Успіх! &nbsp;WE див.

Давайте розберемо його:

Ми присвоюємо змінну з плаваючою комою __ __ безпосередньо у змінну __mynumber __ і потім роздрукуємо її до терміналу за допомогою функції C ++ __cout__.

Поки що ми добре розуміємо регістри ARM, однак на наступному тижні ми запровадимо регістри в коопроцесорі математики, які працюють з змінними з плаваючою комою.&nbsp;. Маніпульований через регістри математики математики.

Наступного тижня ми зануримося в налагодження змінних поплавків.