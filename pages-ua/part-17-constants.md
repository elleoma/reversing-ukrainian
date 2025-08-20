## part 17 - константи

Для повного змісту всіх уроків, будь ласка, натисніть нижче, оскільки він дасть короткий короткий урок на додаток до тем, які він висвітлює.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-підручник

Поки що ми створили, налагодив and зламав простий струнний ехо до стандартного терміналу.&nbsp;we розшириться на цьому прикладі, додавши постійну.

Постійна в C ++ - це значення, яке буде змінювати not протягом усього виконання програми (якщо не зламається) .&nbsp;it використовується таким чином, що у вас є декларація на початку коду, щоб якщо ваша майбутня архітектура програми коли -небудь змінювала, ви можете переосмислити постійну в одному місці, а не оновлювати код через вашу базу коду.

Це стандартна практика кодувати наші константи у всіх обмеженнях, щоб, коли ми бачимо, що вона посилається десь у коді, ми знаємо, що значення є постійною.

Ми починаємо з нашої другої програми в C ++, яка є нашою "постійною" програмою.&nbsp;let's Dive в and розірвати кожну лінію вниз поетапно and див., Як працює ця мова.&nbsp;we Will call this __example2.cpeppepmpemz8 це нашому пристрою.

<pre spellcheck="false">#include &lt;iostream&gt;
&nbsp;
int main(void) {
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; cons tint YEAR = 2017;
&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; std::cout &lt;&lt; YEAR &lt;&lt; std::endl;
&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; return 0;
}
</pre>

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520149852856.jpg"/></div>

Щоб скласти це, ми просто вводимо:

<pre spellcheck="false">g++ example2.cpp -o example2
</pre>

Ми просто тоді вводимо:

<pre spellcheck="false">./example2
</pre>

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520148263310.jpg"/></div>

Успіх! &nbsp;we дивись "__2017__", надрукований до стандартного виводу or термінал!

Давайте розберемо його:

Ми використовуємо __const __keyword, щоб вказати на постійну, до якої ми присвоюємо ціле значення 2017 року.

Потім ми використовуємо __cout __function, щоб надрукувати її до стандартного виводу or термінал and nbsp нова лінія з функцією __endl__.

Це все! &nbsp;very просто.

Наступного тижня ми зануримось у константи налагодження.