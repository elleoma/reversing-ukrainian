## Частина 43 – Хакінг пост-інкрементного оператора

Для повного змісту всіх уроків, будь ласка, натисніть нижче, оскільки це надасть вам короткий зміст кожного уроку, а також теми, які будуть розглянуті. https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Давайте знову розглянемо наш код.

<pre spellcheck="false">#include &lt;iostream&gt;

int main(void) {
&nbsp;&nbsp; &nbsp;int myNumber = 16;
&nbsp;&nbsp; &nbsp;int myNewNumber = ++myNumber;

&nbsp;&nbsp; &nbsp;std::cout &lt;&lt; myNewNumber &lt;&lt; std::endl;

&nbsp;&nbsp; &nbsp;return 0;
}
</pre>

Ми створюємо змінну __myNumber = 16__ до якої створюємо ще одну змінну __myNewNumber__ яка пост-інкрементує значення змінної __myNumber__. Ми бачимо, що коли ми виконуватимемо наш код, воно показуватиме __16__ як значення змінної __myNewNumber__ і __17__ як значення змінної __myNumber__ оскільки __myNewNumber__ не збільшується, оскільки тільки __myNumber__ збільшується, оскільки це пост-оператор.

Коли ми пост-інкрементуємо значення змінної, воно збільшується після призначення йому іншої змінної. Наприклад, __myNumber__ має значення __16__, тому воно збільшується після призначення йому змінної __myNewNumber__, тому ми отримуємо __17__.

Давайте відлагодимо.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1529062708632.jpg"/></div>

Давайте зупинимося на __\*main+28__&nbsp;and continue.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1529062741325.jpg"/></div>

Як ми бачимо, значення в __r3__ є __16__, а значення в __r2__ є __17__. Ми бачимо, що вони завантажені з пам'яті в регістр в __\*main+12__&nbsp;directly за допомогою інструкції __mov__ і __\*main+24__&nbsp;we add __1__ в __r3__ і потім підставляє це значення в __r2__.

Давайте хакнемо цю дитину!

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1529062819877.jpg"/></div>

Ми знаємо, що тепер ми можемо встановити значення __r3__ на своє бажання!

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1529062853544.jpg"/></XyZ9PlH10ZuK8>

Потім ми бачимо, що функція __cout__ мови C++ відображає на екран наш новий хакований значення!

Наступна неділя ми вийдемо на тему пре-декрементного оператора.