## Частина 48 – Дебагування оператора після зменшення

Для повного змісту змісту всіх уроків натисніть нижче, оскільки це надасть вам короткий зміст кожного уроку, а також теми, які будуть обговорені. https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Давайте знову розглянемо наш код.

<pre spellcheck="false">#include &lt;iostream&gt;

int main(void) {
&nbsp;&nbsp; &nbsp;int myNumber = 16;
&nbsp;&nbsp; &nbsp;int myNewNumber = myNumber--;

&nbsp;&nbsp; &nbsp;std::cout &lt;&lt; myNewNumber &lt;&lt; std::endl;
    std::cout &lt;&lt; myNumber &lt;&lt; std::endl;

&nbsp;&nbsp; &nbsp;return 0;
}
</pre>

Ми бачимо дуже простий наш код на C++, до якого ми нічого більше робимо, ніж присвоюємо число змінній, до якої ми ініціалізовуємо ще одну змінну int і присвоюємо оригінальну змінну, до якої вона піддеінкрементується. Потім ми виводимо кожну вартість у термінал.

Давайте дебагуємо.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1532085310684.jpg"/></div>

Вже ясно, що значення для оператора після зменшення завантажується в __r1__ на __main+68 __так що давайте зупинимося на __main+72__.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1532085326445.jpg"/></div>

Ми можемо чітко побачити, що __r1 __насправді містить значення __15__, до якого було зменшено з нашої початкової вартості.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1532085443370.jpg"/></div>

Наступна неділя ми вийдемо на хакінг оператора після зменшення.

Навчання продовжується далі.