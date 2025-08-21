## part 33 - налагодження подвійних змінних

Для повного змісту всіх уроків, будь ласка, натисніть нижче, оскільки він дасть короткий короткий урок на додаток до тем, які він висвітлює.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

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

Встановимо точку перерви в __ -мейн+24__ і продовжимо.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1523008442868.jpg"/></div>

Ми бачимо __STRD r2, \ [r11, \#-12 \] __ І ми повинні повністю розуміти, що це означає, що ми зберігаємо цінність у компенсації __- 12__ з реєстру __r11__ в __r2 __. там.&nbsp;&nbsp;

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1523008470513.jpg"/></div>

VOILA! &nbsp;WE див. __1337.77__ у цьому офсетному місці або спеціально зберігається в __0X7EFFF230__ у пам'яті.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1523008491495.jpg"/></div>

Давайте поступаємо двічі, який виконує __VLDR D0, \ [r11, \#-12 \] __ Як ми розуміємо, що __1337.77__ тепер буде завантажений у коефіцор подвійної точної математики __d0 __register.&nbsp;let, що зараз друкує значення в такому місці.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1523008515533.jpg"/></div>

Нарешті, давайте продовжимо і подивимось, що значення перегукується до terminal.&nbsp;.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1523008538297.jpg"/></div>

Наступного тижня ми зануримося в злом подвійних змінних.