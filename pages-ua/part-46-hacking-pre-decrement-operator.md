## Частина 46 – Хакінг попередньо-декрементного оператора

Для повного змісту всіх уроків натисніть нижче, оскільки це надасть вам короткий зміст кожного уроку, а також теми, які будуть розглянуті. https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Давайте знову розглянемо наш код.

<pre spellcheck="false">#include &lt;iostream&gt;

int main(void) {
&nbsp;&nbsp; &nbsp;int myNumber = 16;
&nbsp;&nbsp; &nbsp;int myNewNumber = --myNumber;

&nbsp;&nbsp; &nbsp;std::cout &lt;&lt; myNewNumber &lt;&lt; std::endl;
    std::cout &lt;&lt; myNumber &lt;&lt; std::endl;

&nbsp;&nbsp; &nbsp;return 0;
}
</pre>

Пам'ятаємо, коли ми компілюємо, отримуємо 15.

Давайте відлагодимо.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1530875391750.jpg"/></div>

Давайте розб'ємо.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1530875474311.jpg"/></div>

Давайте переглянемо вміст __r3 __і хакнемо його.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1530875492398.jpg"/></div>

Тепер, продовжуючи, бачимо, що він не зміг успішно хакнути, чому це?

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1530875528881.jpg"/></XyZ9PlH10ZuK8>

Ми знову запускаємо бінарник і розбиваємо і бачимо значення тут в __r1 __держить __15__.

<XyZ9PlH11ZuK8 class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1530875553276.jpg"/></XyZ9PlH12ZuK8>

Поки продовжується, бачимо 15, який ми не хочемо.

<XyZ9PlH13ZuK8 class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1530875636786.jpg"/></XyZ9PlH14ZuK8>

Тепер знову розбиваємо і друкуємо значення.

<XyZ9PlH15ZuK8 class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1530875661356.jpg"/></XyZ9PlH16ZuK8>

Цього разу ми встановлюємо __r1__ і бачимо, що ми успішно хакнули!

<XyZ9PlH17ZuK8 class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1530875673374.jpg"/></XyZ9PlH18ZuK8>

Це ваш перший досвід з глибоким розбіром регістрів і баченням, де вони зберігаються, і як це може впливати на результат. Вдієте час і виконайте це самостійно, щоб мати міцну основу цього.

Наступна неділя ми вийдемо на оператор після-декрементний.