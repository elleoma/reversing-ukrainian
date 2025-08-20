## part 14 - Hello World

Для повного змісту всіх уроків, будь ласка, натисніть нижче, оскільки він дасть короткий короткий урок на додаток до тем, які він висвітлює.&nbsp;https://github.com/mytechnotalent/Reverse-Engineering-підручник

Сьогодні ми починаємо свою подорож у світ C ++ and, отримуючи краще розуміння того, як C ++ взаємодіє з нашим процесором ARM. Попередні уроки в цій серії зосереджуються на основах процесора ARM and дотику до своєї архітектури and Як все в кінцевому підсумку переводиться на мову складання and, а потім в кінцевому підсумку, а потім в кінцевому підсумку в машинній мові. Ми починаємо з нашої першої програми в C ++, яка є нашою програмою "Hello World ".&nbsp;LET's Dive у and розірвати кожну лінію вниз поетапно and див. and Збережіть його на нашому пристрої. <pre spellcheck="false">#include &lt;iostream&gt;
&nbsp;
int main(void) {
    std::cout &lt;&lt; “Hello World” std::endl;
&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;return 0;
}
</pre>

<div class="slate-resizable-image-embed"><img src="/imgs/1520191083072.jpg"/></div>

Щоб скласти це, ми просто вводимо:

<pre spellcheck="false">g++ example1.cpp -o example1
</pre>

Ми просто тоді вводимо:

<pre spellcheck="false">./example1
</pre>

![](/imgs/1520237920732.jpg)

  

Успіх! &nbsp;we див. "Hello World", надрукований до стандартного виводу or термінал! Давайте розірве його за лінією:

__ \. and візьміть весь вміст цього file and вставити його у існуючий код

We call __iostream__ because we need a declaration for a функція називається __cout__ and __endl__.&nbsp;The __cout__ функція allows us to print text to the standard output or terminal and the __endl__ функція creates a new line after the text has було відображено. Розділ main, який є цілим числом типу, є точкою входу в програму main nbsp BIRIN.&nbsp;ВАРТІВ, що помітить __Void__ всередині __()__, що вказує на те, що він буде проведений nbsp. __STD __інує простір імен, який є просто просто механізмом організації коду в логічні групи, щоб запобігти зіткненню імен, коли ви маєте справу з декількома бібліотеками. Ви побачите багато прикладів, де вони заявляють про використання STD простору імен; Однак я ніколи не буду використовувати цей підхід, оскільки він може спричинити зіткнення імен у більш складних додатках. __&lt;&lt;__ Оператор називається перевантаженим оператором.&nbsp; Вони по суті є функцією, дуже схожа на __printf__ у мові c.&nbsp;we - це просто __ "Hello World" __ thling __ usyz9plh4zuk8 " з __&lt;&lt;__ перевантажений оператор.&nbsp;we push __endl__, що створює нову лінію до console. The final line is the return 0.&nbsp;Since our main функція is of type int, we have to return something.&nbsp;In C++ 11 there is no need for this in the main функція however is required for every other функція.&nbsp;I will stick to tradition and просто включіть його. Наступний етап полягає в тому, що ми складаємо file.&nbsp; Перше, що виникає, - це весь вміст заголовка ioStream, переходить у джерело file, як ми обговорювали.&nbsp;. Компіляція відбувається, коли решта рядків нашого існуючого коду про аналізи через.&nbsp;EssEvery У нас є весь вміст ioStream у новий Hello World console, тоді весь вміст нашого існуючого file додається до sen file. Компанія приймає наш текст Hello World cpp file and перетворює його в проміжний формат під назвою obj file.&nbsp;an styntax, що створюється, є конструкцією конференції variables xyz9. Після створення дерева код генерується.&nbsp;this означає, що зараз у нас є машинний код, що наш процес ARM виконає.&nbsp;every cpp підручник (переклади), що має власні відповідні OBJ file, що пов'язано з власним об'єктом OBJ file, що пов'язано з відповідним OBJ file, що пов'язано з власним об'єктом OBJ file, що пов'язано з власним завдання це.&nbsp;

Linking takes our obj files, our скомпільований files, in addition to the C++ Standard Library and finds where each symbol and функція is and link them all together into one executable.&nbsp;&nbsp;&nbsp;

Наведені вище концепції можуть здатися трохи заплутаними, якщо ви новачок у програмуванні, однак, коли ви кодуєте and компілювати and Пізніше налагодження and hack У мові Асамблеї все це стане дуже зрозумілим and, ви дізнаєтесь, що він дізнається, що обробляє. Наступного тижня ми зануримося в налагодження Hello World.