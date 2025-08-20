## part 33 - налагодження подвійних змінних

Для повного змісту всіх уроків, будь ласка, натисніть нижче, оскільки він дасть короткий короткий урок на додаток до тем, які він висвітлює.

Давайте розглянемо наш код.

<pre spellcheck="false">int main(void) {

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; double myNumber = 1337.77;

&nbsp;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; std::cout &lt;&lt; myNumber &lt;&lt; std::endl;

&nbsp;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; return 0;

}
</pre>

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1523008391034.jpg"/></div>

Давайте налагоджуємо!

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1523008417137.jpg"/></div>

Встановимо breakpoint на __Main+24__ and Продовжуйте.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1523008442868.jpg"/></div>

We see the __strd r2, \[r11, \#-12\]__ and we have to fully understand that this means we are storing the value at the offset of __-12__ from регістр __r11__ into __r2__.&nbsp;Let’s now дослідити what exactly resides там.&nbsp;&nbsp;

nbsp

VOILA! &nbsp;WE див. __1337.77__ у цьому офсетному місці or, спеціально зберігається в __0x7efff230__ в пам'яті.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1523008491495.jpg"/></div>

Давайте вступаємо в двічі, який виконує __VLDR D0, \ [r11, \#-12 \] __ Як ми розуміємо, що __1337.77__ тепер буде завантажено у коефіцієнт подвійної точки зору математики __d0 __register.&nbsp;let, що зараз друкує значення.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1523008515533.jpg"/></div>

Нарешті продовжимо and ДОГЛЯДУЙТЕ ЗНАЧЕННЯ ЗВ'ЯЗАННЯ ДО ТЕМПЛІТАЛУ.&nbsp;this завершує нашу функцію __cout__ c ++.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1523008538297.jpg"/></div>

Наступного тижня ми зануримося в подвійні змінні Hacking.