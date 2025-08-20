## part 10 - вказівник Stack

Для повного змісту всіх уроків, будь ласка, натисніть нижче, оскільки він дасть короткий короткий урок на додаток до тем, які він висвітлює.&nbsp;nbsp

Стек - це абстрактний тип даних, до якого є LIFO (останній у першому виході) .&nbsp;, коли ми push Значення на стек, коли він вискакує стека and, коли він вискочив із стека.

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

Ми бачимо __HEX 30__ or __48 DECIMAL__ Перейшов у __R7 __. &nbsp;LETS знову вступає.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520238832288.jpg"/></div>

Ми бачимо значення __sp__ зміна від __0x7efff3a0__ до __0xefff39c __. &nbsp;that - це рух назад __4 байт __.

Відповідь обертається тим, що стек росте __ вниз __. &nbsp;, коли ми говоримо, що вершина стека ви можете собі уявити, щоб серія табличок розміщується __beneath__ один одного.

Спочатку __sp__ був на __0x7efff3a0__.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520218097215.jpg"/></div>

Коли ми натиснули __R7__ на стек, нова цінність покажчика __Stack__ зараз __0x7efff39c__, щоб ми могли бачити, як стек справді зростає __downward__ в пам'яті.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520239285552.jpg"/></div>

Тепер давайте знову вступити.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520143279567.jpg"/></div>

Ми можемо побачити значення __hex 10__ or __decimal 16__ перемістилося в __r7 __. &nbsp;notice __sp__ зробив not.

Перш ніж ми знову вступимо, давайте подивимось на значення всередині __SP__.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520216970660.jpg"/></div>

Давайте знову вступити.

nbsp

Ми бачимо, що значення в стеку було вискакувано з стека and, покладеним назад у __R7__, тому значення __GHEX 30__ повертається в __R7__, а також __SP__ повертається на __0x73fff3a0__.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520232081853.jpg"/></div>

Будь ласка, знайдіть час, щоб ввести код, складайте and Посилання на це and, потім перейдіть через двійковий у GDB.&nbsp;Stack, є критично важливими для розуміння зворотного інженерії and зловмисного програмного забезпечення, а також будь -якого нерухомості.

Наступного тижня ми зануримось у процедури завантаження мікропрограмного забезпечення ARM.