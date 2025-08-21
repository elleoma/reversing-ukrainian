## Частина 42 – Дебагування оператора після інкременту

Для повного змісту змісту всіх уроків, будь ласка, натисніть нижче, оскільки це надасть вам короткий зміст кожного уроку, а також теми, які будуть обговорені. https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Давайте знову переглянемо свій код.

<pre spellcheck="false">#include &lt;iostream&gt;

int main(void) {
&nbsp;&nbsp; &nbsp;int myNumber = 16;
&nbsp;&nbsp; &nbsp;int myNewNumber = ++myNumber;

&nbsp;&nbsp; &nbsp;std::cout &lt;&lt; myNewNumber &lt;&lt; std::endl;

&nbsp;&nbsp; &nbsp;return 0;
}
</pre>

Ми створюємо змінну __myNumber = 16__ до якої створюємо ще одну змінну __myNewNumber__ яка після інкременту збільшує значення __myNumber__.  Ми бачимо, що коли ми виконуватимемо свій код, воно показуватиме __16__ як значення __myNewNumber__ і __17__ як значення __myNumber__ як __myNewNumber__ не збільшується, оскільки тільки __myNumber__ збільшується, оскільки це після оператор.

Коли ми після інкременту збільшувємо значення змінної, воно збільшується після призначення йому іншої змінної.  Наприклад, __myNumber__ є __16__, тому воно збільшується після призначення йому __myNewNumber__, тому ми отримуємо __17__.

Давайте дебагуємо.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1528458112325.jpg"/></div>

Давайте зупинимося на __\*XyZ9PlH17ZuK8 __і продовжимо.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1528458131421.jpg"/></div>

Як ми бачимо, значення в __r3 __є 16 і значення в __r2 __є 17.  Ми бачимо, що вони завантажені з пам'яті в регістр в __\*main+12__ прямо за допомогою інструкції __mov__ і __\*main+24__ ми додаємо 1 в __r3__ і потім кладемо це значення в __r2__.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1528458142344.jpg"/></div>

Далі ми продовжимо і побачимо, що __cout __c++ функція викликана, яка відображає значення в термінал (стандартний вивід) як очікується.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1528458154804.jpg"/></XyZ9PlH10ZuK8>

Наступна неділя ми вийдемо на хакінг оператора після інкременту.