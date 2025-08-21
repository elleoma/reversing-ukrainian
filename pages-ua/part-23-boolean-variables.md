## Частина 23 – Булеві змінні

Для повного змісту змісту всіх уроків натисніть нижче, оскільки це надасть вам короткий зміст кожного уроку, а також теми, які будуть обговорені. https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Наступний етап нашої подорожі – булеві змінні. Назва походить від великого Джорджа Буля, від якого всі сучасні комп'ютерні науки походять.

На найнижчому рівні значення може бути either 0 або 1, хибне або правдиве, + < 5 вольт або +5 вольт тощо.

Давайте розглянемо наш код.

<pre spellcheck="false">#include &lt;iostream&gt;

&nbsp;

XyZ9PlH0ZuK8 main(void) {

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; bool isHacked = false;

&nbsp;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; std::cout &lt;&lt; isHacked &lt;&lt; std::endl;

&nbsp;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; return 0;

}
</pre>

<XyZ9PlH1ZuK8 class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520192758105.jpg"/></XyZ9PlH2ZuK8>

Щоб скомпільувати цей код, ми просто набираємо:

<pre spellcheck="false">g++ example4.cpp -o example4

./example4
</pre>

<XyZ9PlH3ZuK8 class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520196655358.jpg"/></XyZ9PlH4ZuK8>

УСПІШНО! Ми бачимо __0__ виведено на стандартний вивід або термінал!

Давайте розіб'ємо:

Ми створюємо булеву змінну під назвою __isHacked __, до якої призначаємо значення __false__ або __0__. Коли ми запускаємо бінарний файл, ми явно бачимо значення __0__, яке успішно було виведено на стандартний вивід.

Наступного тижня ми вийдемо на тему Дебагування булевих змінних.