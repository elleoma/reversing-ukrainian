## Частина 49 – Хакінг пост-декрементного оператора

Для повного змісту всіх уроків натисніть нижче, оскільки це надасть вам короткий зміст кожного уроку, а також теми, які будуть розглянуті. https://github.com/mytechnotalent/Reverse-Engineering-Tutorial

Давайте знову переглянемо наш код.

<pre spellcheck="false">#include &lt;iostream&gt;

XyZ9PlH0ZuK8 main(void) {
&nbsp;&nbsp; &nbsp;XyZ9PlH1ZuK8 myNumber = 16;
&nbsp;&nbsp; &nbsp;XyZ9PlH2ZuK8 myNewNumber = myNumber--;

&nbsp;&nbsp; &nbsp;std::cout &lt;&lt; myNewNumber &lt;&lt; std::endl;
    std::cout &lt;&lt; myNumber &lt;&lt; std::endl;

&nbsp;&nbsp; &nbsp;return 0;
}
</pre>

Давайте переглянемо попередній тиждень відлагодження.

<XyZ9PlH4ZuK8 class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1532690049930.jpg"/></XyZ9PlH5ZuK8>

Як ми бачимо тут, значення в __r1__ на __main+68__ становить __15__. Давайте хакнемо!

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width"><img src="/imgs/1532690140517.jpg"/></div>

Як ми знову змінили виконання програми на свій розсуд. З кожним з цих уроків у розмірі байта ви продовжуєте краще розуміти процесор і як він взаємодіє з бінарним кодом.

Я сподіваюся, що ця серія надасть вам міцну основу для розуміння процесора ARM. Ця серія закінчується. Дякую всім за участь у цій подорожі!