## PART 42-Налагодження оператора після інвентації

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

We create a variable __myNumber = 16__ to which we create another variable __myNewNumber__ which post-increments the value of __myNumber__.&nbsp;We see that when we виконувати our код it shows __16__ as the value of __myNewNumber__ and __17__ as the value of __myNumber__ as __myNewNumber__ Чи збільшується not, оскільки лише __mynumber__ збільшується, оскільки він є пост -оператором.

Коли ми після запровадження значення змінної збільшується після призначення її іншій змінній.&nbsp; для прикладу __mynumber__ __16__, тому він збільшується після того, як його призначають __mynewnumbum__, тому ми отримуємо __17__.

Давайте налагоджуємо.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1528458112325.jpg"/></div>

Давайте розірвемося на __ \*main+28 __ і продовжуємо.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1528458131421.jpg"/></div>

Як ми бачимо значення в __r3 __is 16 and Значення в __r2 __is 17. Ми можемо бачити, що вони завантажені з пам'яті в регістри в __ \*main+12__ безпосередньо __ -mov__ and __ \*xyz9plh20 \ 24. add 1 в __r3__ and, а потім поставте це значення в __r2__.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1528458142344.jpg"/></div>

По мірі продовження ми можемо побачити функцію __cout __c ++ під назвою, яка переливає значення до терміналу (стандартний вихід), як очікувалося.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1528458154804.jpg"/></div>

На наступному тижні ми зануримось у оператор після інвентації Hacking.