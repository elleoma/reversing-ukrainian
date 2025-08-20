## PART 47-Оператор після декреції

На цьому тижні ми звернемося до оператора після декларації. Давайте розглянемо наш код.

<pre spellcheck="false"><span class="hljs-meta">#include &lt;iostream&gt;</span>

<span class="hljs-функція"><span class="hljs-keyword">int</span> <span class="hljs-title">main</span><span class="hljs-params">(<span class="hljs-keyword">void</span>) </span> </span> {
&nbsp;&nbsp; &nbsp;<span class="hljs-keyword">int</span> mynumber = <span class="hljs-number">16</span>;
&nbsp;&nbsp; &nbsp;<span class="hljs-keyword">int</span> mynewnumber = mynumber--;

&nbsp;&nbsp; &nbsp;<span class="hljs-built_in">std</span> :: <span class="hljs-built_in">cout</span> &lt;&lt; mynewnumber &lt;&lt;p <span class="hljs-built_in">std</span> :: <span class="hljs-built_in">endl</span>;
    <span class="hljs-built_in">std</span> :: <span class="hljs-built_in">cout</span> &lt;&lt; mynumber nbsp&lt; <span class="hljs-built_in">std</span> :: <span class="hljs-built_in">endl</span>;

&nbsp;&nbsp; &nbsp;<span class="hljs-keyword">return</span> <span class="hljs-number">0</span>;
}
</pre>

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width">
<img src="/imgs/1531481191370.jpg"/>
</div>

 Під час складання ми бачимо __16__ and __15__ Надруковано відповідно.

<div class="slate-resizable-image-embed slate-image-embed__resize-full-width">
<img src="/imgs/1531481259797.jpg"/>
</div>

Ми бачимо, що в цьому сценарії __mynewnumber__ знижується як __mynumber-- __takes значення 16 and зменшує його до 15.

Наступного тижня ми зануримося в налагодження оператора після декларації.