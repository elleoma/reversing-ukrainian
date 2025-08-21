## part 35 - sizeof оператор

Для повного змісту всіх уроків, будь ласка, натисніть нижче, оскільки він дасть короткий короткий урок на додаток до тем, які він висвітлює.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Наступний етап нашої подорожі - це оператор Sizeof.&nbsp;

Давайте розглянемо наш код.

<pre spellcheck="false">#include &lt;iostream&gt;

&nbsp;

int main(void) {

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; int myNumber = 16;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; int myNumberSize = sizeof(myNumber);

&nbsp;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; std::cout &lt;&lt; myNumberSize &lt;&lt; std::endl;

&nbsp;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; return 0;

}
</pre>

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1524218995477.jpg"/></div>

Щоб скласти це, ми просто вводимо:

g ++ example8.cpp -o example8

./example8

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1524219035247.jpg"/></div>

Ми бачимо 4 надруковані на екрані.

Давайте розберемо його:

Ми створюємо змінну __mynumber = 16__, на яку ми створюємо ще одну змінну __mynumbersize__, яка містить значення розміру __mymumber __. &nbsp;we бачимо, що коли ми виконуємо наш код, він показує 4, тому ми бачимо, що оператор SizeOf вказує на ціле чисельність 4 байт.

Наступного тижня ми зануримось у налагодження оператора Sizeof.