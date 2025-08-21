## PART 42-Налагодження оператора після інвентації

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

Ми створюємо змінну __mynumber = 16__, на яку ми створюємо ще одну змінну __mynewnumber__, що після інкрементів значення __mynumber __. &nbsp;we бачимо, що коли ми виконуємо наш код, він показує __16__ як цінність __mynewnumber__ і __17__ як цінність __mynumber__ as __mmynumbumbumbumbumbumbumbumbumbrum __, як не ґрунтується як __mynumber__ as __mmynumbumbumbumbumbumbumbumbumbumbumbumbru__, як не ґрунтується __s __mynumber__ збільшується, оскільки це пост -оператор.

Коли ми після запровадження значення змінної збільшується після призначення її іншій змінній.&nbsp; для прикладу __mynumber__ __16__, тому він збільшується після того, як його призначають __mynewnumbum__, тому ми отримуємо __17__.

Давайте налагоджуємо.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1528458112325.jpg"/></div>

Давайте розірвемося на __ \*main+28 __ і продовжуємо.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1528458131421.jpg"/></div>

Як ми бачимо значення в __R3 __ен 16 і значення в __R2 __ен 17. Ми можемо бачити, що, як вони завантажені з пам'яті в регістри в __ \*основному+12__ безпосередньо за допомогою __mov__ інструкції та __ \*основного+24__, ми додаємо 1 в __r3__, а потім вкладаємо це значення в __r2__.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1528458142344.jpg"/></div>

По мірі продовження ми можемо побачити функцію __cout __c ++ під назвою, яка переливає значення до терміналу (стандартний вихід), як очікувалося.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1528458154804.jpg"/></div>

Наступного тижня ми занурюємось у хакерський оператор після інвентації.