## part 34 - хакерство подвійних змінних

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

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1523615576064.jpg"/></div>

Давайте налагоджуємо!

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1523615640968.jpg"/></div>

Встановимо точку перерви в __ -мейн+24__ і продовжимо.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1523615666432.jpg"/></div>

Ми бачимо __STRD r2, \ [r11, \#-12 \] __ І ми повинні повністю зрозуміти, що це означає, що ми зберігаємо цінність у компенсації __- 12__ з реєстру __r11__ в __r2 __. там.&nbsp;&nbsp;

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1523615689648.jpg"/></div>

VOILA! &nbsp;WE див. __1337.77__ у цьому офсетному місці або спеціально зберігається в __0X7EFFF230__ у пам'яті.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1523615716304.jpg"/></div>

Давайте вступаємо двічі, який виконує __VLDR D0, \ [r11, \#-12 \] __ Як ми розуміємо, що __1337.77__ тепер буде завантажений у подвійний точний математичний копроцесор __d0 __register.&nbsp;let, який зараз друкує значення в цьому місці нижче.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1523615745800.jpg"/></div>

Давайте зламаємо реєстр __D0__!

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1523615775560.jpg"/></div>

Тепер давайте переглянемо значення всередині __d0__.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1523615802811.jpg"/></div>

Продовжуємо.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1523615835964.jpg"/></div>

Успішно зламано!

Наступного тижня ми занурюємось у оператор Sizeof.