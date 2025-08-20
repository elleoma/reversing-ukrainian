## part 43-Hacking після інкрементального оператора

Для повного змісту всіх уроків, будь ласка, натисніть нижче, оскільки він дасть короткий короткий урок на додаток до тем, які він висвітлює.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-підручник

Давайте переглянемо наш код.

<pre spellcheck="false">#include &lt;iostream&gt;

int main(void) {
&nbsp;&nbsp; &nbsp;int myNumber = 16;
&nbsp;&nbsp; &nbsp;int myNewNumber = ++myNumber;

&nbsp;&nbsp; &nbsp;std::cout &lt;&lt; myNewNumber &lt;&lt; std::endl;

&nbsp;&nbsp; &nbsp;return 0;
}
</pre>

Ми створюємо Variable&nbsp;__mynumber = 16&nbsp;__to, який ми створюємо ще одну зміннукси9plh87zuk8__mynewnumber__. show&nbsp;__16__&nbsp;as value of&nbsp;__mynewnumber__&nbsp;and&nbsp;__17__&nbsp;as of&nbsp;__mynumber&nbsp;__as&nbsp;__mynewnumber__&nbsp;does not збільшується як ony&nbsp;__mynumber__&nbsp; intoraped.

Коли ми після запровадження значення змінної збільшується після призначення її іншій змінній.&nbsp; для приклад&nbsp;__mymber__&nbsp;is&nbsp;__16__&nbsp;so, це збільшується після того, як він призначається після того, як він призначається після того, як він прискорюється після того, як він прискорюється після того, як він прискорюється після того, як він прискорюється після того, як це прискорюється після того, як це прискорюється після пристосування після відступу після пристосування to&nbsp;__mynewnumber__&nbsp;so, тому ми get&nbsp;__17__.

Давайте налагоджуємо.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1529062708632.jpg"/></div>

Давайте розірвемо On&nbsp; __ \*main+28__&nbsp;and.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1529062741325.jpg"/></div>

Як ми можемо побачити значення in&nbsp;__r3__&nbsp;is __16__ and значення in&nbsp;__r2__&nbsp;is __17__. Ми можемо бачити, що, як вони завантажені з пам'яті в регістри in&nbsp; __ \*main+12__&nbsp;dectly шляхом the&nbsp;__mov__&nbsp;інструкція and&nbsp; __ \*main+24__&nbsp;we add __1__ of&nbsp;__r3__&nbsp;and value812 OF&nbsp;__R2__.

Давайте hack ця дитина!

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1529062819877.jpg"/></div>

Ми знаємо, що тепер можемо встановити цінність __R3__ на бажання нашого серця!

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1529062853544.jpg"/></div>

Коли ми продовжуємо, ми бачимо функцію C ++ __Cout__, перегукується з нашим новим зламаним значенням на екрані!

Наступного тижня ми зануримося в оператор попереднього декларації.