## PART 37 - Оператор Hacking Sizeof

Для повного змісту всіх уроків, будь ласка, натисніть нижче, оскільки він дасть короткий короткий урок на додаток до тем, які він висвітлює.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Давайте переглянемо наш код.

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

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1525429032559.jpg"/></div>

Пам'ятайте, що ми створюємо змінну __mynumber = 16__, до якої ми створюємо іншу змінну __mynumbersize__, яка містить значення розміру __mynumber __. &nbsp;we бачимо, що коли ми виконуємо наш код, він показує 4, тому ми бачимо, що оператор Sizeof вказує на ціле двобайки широко.

Давайте розглянемо код минулого тижня, коли ми починаємо з налагодження та розриву на Main.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1525429072643.jpg"/></div>

Давайте розірвемося на __main+20__, як ми бачимо, що значення __4__ переміщується в __r3__.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1525429109049.jpg"/></div>

Давайте розглянемо, що відбувається в __main+16__, як ми бачимо, що ми зберігаємо значення __ $ r11-8__ того, що існує в __r3__, що в нашому випадку __16 __. &nbsp;. __16 __. &nbsp;WE бачимо це тут, коли ми вивчаємо значення всередині __ $ r11-8__.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1525429200465.jpg"/></div>

Як ми бачимо вище значення всередині __ $ r11-12__ IS__ 4__, оскільки це представляє значення, яке __SizeOf__ повертається як ціле число __16 __, насправді 4 байти широко.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1525429249458.jpg"/></div>

Нарешті, коли ми продовжуємо виконання, ми насправді бачимо значення __4__ перегукується з терміналом.

Давайте хакемо!

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1525429287002.jpg"/></div>

Ми біжимо і розриваємося на __main+28__.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1525429310244.jpg"/></div>

Ми бачимо, що цінність у __R3__ - __4__, що очікується.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1525429336631.jpg"/></div>

Ми ламаємося на __main+36__.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1525429367083.jpg"/></div>

Ми бачимо, що значення в __R1__ є __4__, що повинно мати логічний сенс, оскільки цінність зберігалася з __R3__ в __R11-12__, а потім назад до __R1__.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1525429391206.jpg"/></div>

Давайте зламаємо значення в __R1__!

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1525429414806.jpg"/></div>

Успіх! &nbsp;we зламали машину!

Наступного тижня ми зануримося в оператор попереднього інкрементації.