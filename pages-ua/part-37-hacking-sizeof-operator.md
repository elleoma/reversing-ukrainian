Частина 37 – Хакінг оператора SizeOf

Для повного змісту змісту всіх уроків, будь ласка, натисніть нижче, оскільки це надасть вам короткий зміст кожного уроку, а також теми, які будуть розглянуті.

Давайте знову розглянемо наш код.

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

Пам'ятайте, що ми створюємо змінну __myNumber = 16__ до якої створюємо ще одну змінну __myNumberSize__ яка зберігає значення розміру __myNumber__.  Ми бачимо, що коли ми виконуємо наш код, воно показує 4, тому ми бачимо, що оператор SizeOf вказує, що ціле число має ширину 4 байти.

Давайте переглянемо код попередньої тижневої роботи, оскільки починаємо з відлагодження та зупинки на головній.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1525429072643.jpg"/></div>

Давайте зупинимося на __main+20__ оскільки ми бачимо значення __4__ яке переміщується в __r3__.

<XyZ9PlH10ZuK8 class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1525429109049.jpg"/></XyZ9PlH11ZuK8>

Давайте розглянемо, що відбувається на __main+16__ оскільки ми бачимо, що зберігаємо значення в __$r11-8__ те, що існує в __r3__ яке в нашому випадку є __16__.  Це має сенс, оскільки коли ми розглядаємо нашу початкову код, значення __myNumber__ насправді було __16__.  Ми бачимо це тут, коли ми розглядаємо значення всередині __$r11-8__.

<XyZ9PlH12ZuK8 class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1525429200465.jpg"/></XyZ9PlH13ZuK8>

Як ми бачимо вище, значення всередині __$r11-12__ є __4__ оскільки воно представляє значення, яке повертає __SizeOf__ як ціле число __16__ насправді має ширину 4 байти.

<XyZ9PlH14ZuK8 class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1525429249458.jpg"/></XyZ9PlH15ZuK8>

Нарешті, коли ми продовжимо виконання, насправді побачимо значення __4__ відображене в терміналі.

Давайте хакнемо!

<XyZ9PlH16ZuK8 class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1525429287002.jpg"/></XyZ9PlH17ZuK8>

Ми запускаємо і зупиняємося на __main+28__.

<XyZ9PlH18ZuK8 class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1525429310244.jpg"/></XyZ9PlH19ZuK8>

Ми бачимо значення в __r3__ є __4__ яке очікується.

<XyZ9PlH20ZuK8 class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1525429336631.jpg"/></XyZ9PlH21ZuK8>

Ми зупиняємося на __main+36__.

<XyZ9PlH22ZuK8 class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1525429367083.jpg"/></XyZ9PlH23ZuK8>

Ми бачимо значення в __r1__ є __4__ яке повинно мати логічне значення, оскільки значення було збережено з __r3__ в __r11-12__ і потім знову в __r1__.

<XyZ9PlH24ZuK8 class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1525429391206.jpg"/></XyZ9PlH25ZuK8>

Давайте хакнемо значення в __r1__!

<XyZ9PlH26ZuK8 class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1525429414806.jpg"/></XyZ9PlH27ZuK8>

Успіх!  Ми здійснили хакінг машини!

Наступна неділя ми вийдемо в оператор Pre-Increment.