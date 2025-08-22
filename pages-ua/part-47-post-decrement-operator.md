Частина 47 – Оператор післядеінкременту

Цього тижня ми розглянемо оператор післядеінкременту. Давайте вивчіть наш код.

<pre spellcheck="false"><span class="hljs-meta">#include &lt;iostream&gt;</span>

<span class="hljs-function"><span class="hljs-keyword">XMDX8ef30f44c654XMDX</span> <span class="hljs-title">main</span><span class="hljs-params">(<span class="hljs-keyword">void</span>)</span> </span>{
&nbsp;&nbsp; &nbsp;<span class="hljs-keyword">XMDX61134ae32703XMDX</span> myNumber = <span class="hljs-number">16</span>;
&nbsp;&nbsp; &nbsp;<span class="hljs-keyword">XMDX2645dcdb0317XMDX</span> myNewNumber = myNumber--;

&nbsp;&nbsp; &nbsp;<span class="hljs-built_in">std</span>::<span class="hljs-built_in">cout</span> &lt;&lt; myNewNumber &lt;&lt; <span class="hljs-built_in">std</span>::<span class="hljs-built_in">endl</span>;
    <span class="hljs-built_in">std</span>::<span class="hljs-built_in">cout</span> &lt;&lt; myNumber &lt;&lt; <span class="hljs-built_in">std</span>::<span class="hljs-built_in">endl</span>;

&nbsp;&nbsp; &nbsp;<span class="hljs-keyword">return</span> <span class="hljs-number">0</span>;
}
</pre>

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width">
<img src="/imgs/1531481191370.jpg"/>
</div>

 Під час компіляції ми бачимо __16__ і __15__ відповідно виведені на екран.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width">
<img src="/imgs/1531481259797.jpg"/>
</div>

Ми бачимо, що в цьому сценарії __myNewNumber__ все ж зменшується, оскільки __myNumber-- __бере значення 16 і зменшує його до 15.

Наступного тижня ми продовжимо вивчення операції відладки післядеінкременту.