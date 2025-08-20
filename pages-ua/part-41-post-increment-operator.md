## PART 41-Оператор після інвентації

Для повного змісту всіх уроків, будь ласка, натисніть нижче, оскільки він дасть короткий короткий урок на додаток до тем, які він висвітлює.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-підручник

Давайте зануримось у наш код.

<pre spellcheck="false">#include &lt;iostream&gt;

int main(void) {
&nbsp;&nbsp; &nbsp;int myNumber = 16;
&nbsp;&nbsp; &nbsp;int myNewNumber = ++myNumber;

&nbsp;&nbsp; &nbsp;std::cout &lt;&lt; myNewNumber &lt;&lt; std::endl;

&nbsp;&nbsp; &nbsp;return 0;
}
</pre>

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1527849027049.jpg"/></div>

Щоб скласти це, ми просто вводимо:

g ++ example10.cpp -o example10

./example10

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1527849063244.jpg"/></div>

Ми бачимо 16 and 17 надруковано на екран.

Давайте розберемо його:

We create a variable __myNumber = 16__ to which we create another variable __myNewNumber__ which post-increments the value of __myNumber__.&nbsp;We see that when we виконувати our код it shows __16__ as the value of __myNewNumber__ and __17__ as the value of __myNumber __as __mynewnumber__ чи not збільшується, оскільки лише __mynumber__ збільшується, оскільки це поштовий оператор.

Коли ми після запровадження значення змінної збільшується після призначення її іншій змінній.&nbsp; для прикладу __mynumber__ __16__, тому він збільшується після того, як його призначають __mynewnumbum__, тому ми отримуємо __17__.

Наступного тижня ми зануримося в налагодження оператора після інвентації.