## Частина 31 – Хакінг змінних Float

Для повного змісту змісту всіх уроків натисніть нижче, оскільки це надасть вам короткий зміст кожного уроку, а також теми, які будуть обговорені. https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Давайте знову переглянемо наш код.

<pre spellcheck="false">#include &lt;iostream&gt;

&nbsp;

int main(void) {

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; int myNumber = 1337.1;

&nbsp;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; std::cout &lt;&lt; myNumber &lt;&lt; std::endl;

&nbsp;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; return 0;

}
</pre>

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1521799049547.jpg"/></div>

Давайте переглянемо попередній урок.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1521799097861.jpg"/></div>

Давайте зупинимося на __main+20__ і продовжимо на цьому місці.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1521799125882.jpg"/></div>

Давайте побачимо, яку вартість знаходиться всередині __r11-8__.  Вже дуже добре бачимо, що це __1337.09998__, яка наближається до нашої вартості в нашому оригінальному коді C++.  Увага: плаваючий має близько 7 цифр десятичної точності, тому ми не бачимо __1337.1__.  Будьте пам'ятні цьому, оскільки ми йдемо далі.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1521799166328.jpg"/></div>

Ми також бачимо цю вартість в високій пам'яті.

<XyZ9PlH10ZuK8 class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1521799204709.jpg"/></XyZ9PlH11ZuK8>

Давайте зупинимося на __main+28__ і продовжимо.

<XyZ9PlH12ZuK8 class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1521799242840.jpg"/></XyZ9PlH13ZuK8>

Ми бачимо дивну нову інструкцію.  Ми бачимо __vldr__ і значення всередині __r11, \#8__ переміщується в__ s0__.  А що таке __s0__?  Ми маємо математичний процесор, який має серію додаткових регістрів, які працюють з десятковими або плаваючими-цілочисельними числами.  Тут ми бачимо приклад такого, до якого значення __1337.09998 __переміщується в __s0__.  Інструкція __vldr__ завантажує константне значення в кожний елемент однобайтової або подвійної точності регістра, наприклад __s0__.

<XyZ9PlH14ZuK8 class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1521799279756.jpg"/></XyZ9PlH15ZuK8>

Ми можемо побачити ці спеціальні регістри тільки якщо ми зробимо команду info registers all, як ми робимо нижче.

<XyZ9PlH16ZuK8 class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1521799307421.jpg"/></XyZ9PlH17ZuK8>

Нижче ми бачимо значення, яке тепер переміщується в __s0__.

<XyZ9PlH18ZuK8 class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1521799331767.jpg"/></XyZ9PlH19ZuK8>

Давайте хакнемо!

<XyZ9PlH20ZuK8 class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1521799362535.jpg"/></XyZ9PlH21ZuK8>

Давайте тепер подивимося на регістри і побачимо, що відбулося.

<XyZ9PlH22ZuK8 class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1521799386349.jpg"/></XyZ9PlH23ZuK8>

<XyZ9PlH24ZuK8 class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1521799407513.jpg"/></XyZ9PlH25ZuK8>

Як бачите, ми вже хакнули значення (з урахуванням проблеми точності змінної float, яка відповідає 6 десятичним місцям).

<XyZ9PlH26ZuK8 class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1521799441419.jpg"/></XyZ9PlH27ZuK8>

Нарешті, продовжуючи, ми бачимо наш хакований вміст відбитий знову на терміналі, коли функція C++ __cout __ виконує.

Наступна неділя ми вийдемо на подвійні змінні.