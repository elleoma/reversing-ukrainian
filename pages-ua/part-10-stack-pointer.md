## part 10 - вказівник стека

Для повного змісту всіх уроків, будь ласка, натисніть нижче, оскільки він дасть короткий короткий урок на додаток до тем, які він висвітлює.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Стек - це абстрактний тип даних, до якого є LIFO (останнє в спочатку) .&nbsp;, коли ми відштовхуємо значення на стек, який він переходить у вказівник стека і коли він вискакує зі стека, він вискакує значення зі стека і в реєстр обраних.

Код часу! Знову ж таки, не відлякуйте, якщо ви не розумієте все в прикладі коду тут.&nbsp;it стане зрозумілим протягом наступних кількох уроків.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520149187367.jpg"/></div>

Компілювати:

<pre spellcheck="false">as -o sp_demo.o sp_demo.s

ld -o sp_demo sp_demo.o
</pre>

Ще раз дозволяє завантажити двійкову в GDB, щоб побачити, що відбувається.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520209893418.jpg"/></div>

Давайте вступити в один раз.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520232603248.jpg"/></div>

Ми бачимо, що __hex 30__ або __48 Decimal__ перейшов у __R7 __. &nbsp;LETS знову вступає.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520238832288.jpg"/></div>

Ми бачимо значення __sp__ зміна від __0x7efff3a0__ до __0xefff39c __. &nbsp;that - це рух назад __4 байт __.

Відповідь обертається тим, що стек росте __ вниз __. &nbsp;, коли ми говоримо, що верхня частина стека ви можете уявити серію табличок, що розміщуються __beneath__ один одного.

Спочатку __sp__ був на __0x7efff3a0__.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520218097215.jpg"/></div>

Коли ми натиснули __R7__ на стек, нова цінність покажчика __Stack__ зараз __0x7efff39c__, щоб ми могли бачити, як стек справді зростає __downward__ в пам'яті.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520239285552.jpg"/></div>

Тепер давайте знову вступити.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520143279567.jpg"/></div>

Ми можемо побачити значення __hex 10__ або __decimal 16__ переміщено в __r7 __. &nbsp;notice __sp__ не змінився.

Перш ніж ми знову вступимо, давайте подивимось на значення всередині __SP__.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520216970660.jpg"/></div>

Давайте знову вступити.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520233070958.jpg"/></div>

Ми бачимо, що цінність у стеку була вискакувана зі стека і повернулася назад у __R7__, тому значення __HEX 30__ повертається в __R7__, а також __SP__ повернеться на __0x73fff3a0__.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520232081853.jpg"/></div>

Будь ласка, знайдіть час, щоб ввести код, компілювати та зв’язати його, а потім перейти через двійковий у GDB.&nbsp;STACK Операції є критично важливими для розуміння зворотного інженерного та зловмисного аналізу, а також будь -якої налагодження.

Наступного тижня ми зануримось у процедури завантаження мікропрограмного забезпечення ARM.