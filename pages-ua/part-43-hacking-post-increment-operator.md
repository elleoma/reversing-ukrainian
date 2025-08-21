## PART 43-Злом оператора після інвентаризації

Для повного змісту всіх уроків, будь ласка, натисніть нижче, оскільки він дасть короткий короткий урок на додаток до тем, які він висвітлює.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Давайте переглянемо наш код.

<pre spellcheck="false">#include &lt;iostream&gt;

int main(void) {
&nbsp;&nbsp; &nbsp;int myNumber = 16;
&nbsp;&nbsp; &nbsp;int myNewNumber = ++myNumber;

&nbsp;&nbsp; &nbsp;std::cout &lt;&lt; myNewNumber &lt;&lt; std::endl;

&nbsp;&nbsp; &nbsp;return 0;
}
</pre>

Ми створюємо Variable&nbsp;__mynumber = 16&nbsp;__to, який ми створюємо ще одну зміннукси9plh20zuk8__mynewnumber__, що після інкрементів значення of&nbsp;__mynumber __. &nbsp;we див. show&nbsp;__16__&nbsp;as значення of&nbsp;__mynewnumber__&nbsp;and&nbsp;__17__&nbsp;as Значення of&nbsp;__mynumber&nbsp;__as&nbsp;__mynewnumber__&nbsp;does не збільшується як єдинийdiv__mynumber__&nbsp;get, як це є постійним оператором.

Коли ми після запровадження значення змінної збільшується після присвоєння її іншій змінній.&nbsp; для example&nbsp;__mymber__&nbsp;is&nbsp;__16__&nbsp;so, це збільшується після того, як він призначається після того, як він призначається після того, як він прискорюється після того, як він прискорюється після того, як він прискорюється після того, як це прискорюється після того, як він прискорюється після того, як він прискорюється після того, як він прискорюється після пристосування після відстоювання to&nbsp;__mynewnumber__&nbsp;so, тому ми get&nbsp;__17__.

Давайте налагоджуємо.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1529062708632.jpg"/></div>

Давайте розірвемо On&nbsp; __ \*main+28__&nbsp; і продовжуємо.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1529062741325.jpg"/></div>

Як ми бачимо значення in&nbsp;__r3__&nbsp;is __16__ та значення in&nbsp;__r2__&nbsp;is __17__. Ми можемо бачити, що, як вони завантажені з пам'яті в регістри in&nbsp; __ \*main+12__&nbsp;dectly за допомогою the&nbsp;__mov__&nbsp;instruction and&nbsp; __ \**mentemezcyz9plh53zuk8 __ \*mente+241x __1__ Of&nbsp;__r3__&nbsp; і тоді поставте це значення Oflyz9plh57zuk8__r2__.

Давайте зламаємо цю дитину!

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1529062819877.jpg"/></div>

Ми знаємо, що тепер можемо встановити цінність __R3__ на бажання нашого серця!

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1529062853544.jpg"/></div>

Коли ми продовжуємо, ми бачимо функцію C ++ __Cout__, перегукується з нашим новим зламаним значенням на екрані!

Наступного тижня ми зануримося в оператор попереднього декларації.