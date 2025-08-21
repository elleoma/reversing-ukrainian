Частина 10 - Стековий вказівник

Для повного змісту змісту всіх уроків, будь ласка, натисніть нижче, оскільки це надасть вам короткий зміст кожного уроку, а також теми, які будуть розглянуті. https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Стек - це абстрактний тип даних, який є LIFO (Last In First Out). Коли ми надсилаємо значення на стек, воно потрапляє в стековий вказівник, а коли воно видаляється з стека, воно видаляється зі стека і потрапляє в регістр, який ви оберігаєте.

Код часу! Опять же, не розчаровуйтеся, якщо ви не розумієте всього в прикладі коду тут. Воно стане ясним протягом наступних кількох уроків.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520149187367.jpg"/></div>

Для компіляції:

<pre spellcheck="false">as -o sp_demo.o sp_demo.s

ld -o sp_demo sp_demo.o
</pre>

Ще раз завантажуємо бінарний файл в GDB, щоб побачити, що відбувається.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520209893418.jpg"/></div>

Давайте крок за кроком увійдемо один раз.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520232603248.jpg"/></div>

Ми бачимо __hex 30__ або __48 десятичний__ переміщений в __r7__. Давайте крок за кроком увійдемо знову.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520238832288.jpg"/></XyZ9PlH10ZuK8>

Ми бачимо зміну значення __sp__ від __0x7efff3a0__ до __0xefff39c__. Це зміна на __4 байти__ назад. Чому стековий вказівник рухається назад, ви можете запитати!

Відповідь полягає в тому, що стек зростає __НИЗКАРОКУ__. Коли ми кажемо, що верхня частина стека, ви можете уявити собі ряд тарілок, які розміщені __НИЖЧЕ__ одна від іншої.

Оригінально __sp__ був у __0x7efff3a0__.

<XyZ9PlH11ZuK8 class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520218097215.jpg"/></XyZ9PlH12ZuK8>

Коли ми надіслали __r7__ на стек, нове значення __Стековий вказівник__ тепер __0x7efff39c__, тому ми бачимо, що Стек справжньо зростає __НИЗКАРОКУ__ в пам'яті.

<XyZ9PlH13ZuK8 class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520239285552.jpg"/></XyZ9PlH14ZuK8>

Давайте крок за кроком увійдемо знову.

<XyZ9PlH15ZuK8 class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520143279567.jpg"/></XyZ9PlH16ZuK8>

Ми бачимо значення __hex 10__ або __16 десятичний__ переміщений в __r7__. Зверніть увагу, що __sp__ не змінився.

До того, як крок за кроком увійти знову, давайте подивимося на значення всередині __sp__.

<XyZ9PlH17ZuK8 class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520216970660.jpg"/></XyZ9PlH18ZuK8>

Давайте крок за кроком увійдемо знову.

<XyZ9PlH19ZuK8 class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520233070958.jpg"/></XyZ9PlH20ZuK8>

Ми бачимо, що значення в стеку було виведено зі стека і повернуто в __r7__, тому значення __hex 30__ знову знаходиться в __r7__, а також __sp__ знову знаходиться в __0x73fff3a0__.

<XyZ9PlH21ZuK8 class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1520232081853.jpg"/></XyZ9PlH22ZuK8>

Будь ласка, візьміть час, щоб набрати код, скомпільувати і зв'язати його, а потім крок за кроком пройдіть бінарний файл в GDB. Стекові операції критичні для розуміння відтворення інженерії і аналізу шкідливого програмного забезпечення, а також будь-якої відладки будь-якого типу.

Наступного тижня ми вийдемо в ARM Фірмові процедури завантаження.