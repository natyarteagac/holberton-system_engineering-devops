      <h1 class="gap">0x06. Regular expression</h1>


  <ul class="list-group metadata" id="project-metadata">
  <li class="list-group-item">
    <i class="fa fa-folder-open fa-fw"></i>
    <em>Foundations &gt; System engineering &amp; DevOps &gt; Scripting</em>
  </li>


<li class="list-group-item">
      <i class="fa fa-user fa-fw"></i> By Sylvain Kalache, co-founder at Holberton School
    </li>




<li class="list-group-item">
        <i class="fa fa-calendar fa-fw"></i>
            Ongoing project - started 07-05-2021, must end by 07-06-2021 (in about 4 hours)
          - you're done with <span id="student_task_done_percentage">100</span>% of tasks.
      </li>

<li class="list-group-item">
        <i class="fa fa-check fa-fw"></i>
          Checker was released at 07-05-2021 06:00 PM
      </li>

<li class="list-group-item">
        <i class="fa fa-check-square fa-fw"></i>
          <strong>Manual QA review must be done</strong>
          (request it when you are done with the project)
      </li>

<li class="list-group-item">
        <i class="fa fa-check-square fa-fw"></i>
        QA review fully automated.
      </li>


</ul>



<div id="project_id" style="display: none" data-project-id="78"></div>




<h2>Concepts</h2>

  <div class="panel panel-default">
    <div class="panel-body">
      <p>
        <em>For this project, students are expected to look at this concept:</em>
      </p>

<ul>
          <li>
            <a href="/concepts/29">Regular Expression</a>
          </li>
      </ul>
    </div>
  </div>


<div class="gap" id="project-description">
  <h2>Background Context</h2>

<p>For this project, you have to build your regular expression using Oniguruma, a regular expression library that which is used by Ruby by default. Note that other regular expression libraries sometimes have different properties.</p>

<p>Because the focus of this exercise is to play with regular expressions (regex), here is the Ruby code that you should use, just replace the regexp part, meaning the code in between the <code>//</code>:</p>

<pre><code>sylvain@ubuntu$ cat example.rb
#!/usr/bin/env ruby
puts ARGV[0].scan(/127.0.0.[0-9]/).join
sylvain@ubuntu$
sylvain@ubuntu$ ./example.rb 127.0.0.2
127.0.0.2
sylvain@ubuntu$ ./example.rb 127.0.0.1
127.0.0.1
sylvain@ubuntu$ ./example.rb 127.0.0.a
</code></pre>

<h2>Resources</h2>

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="/rltoken/SJ2eQ7V2iQlCgLc-L96zWg" title="Regular expressions - basics" target="_blank">Regular expressions - basics</a> </li>
<li><a href="/rltoken/qyjWL-J1_qUaZGR690gH1Q" title="Regular expressions - advanced" target="_blank">Regular expressions - advanced</a> </li>
<li><a href="/rltoken/WCjn8NgohbQ5NGXEObWZvQ" title="Rubular is your best friend" target="_blank">Rubular is your best friend</a> </li>
<li><a href="/rltoken/Zfvv_ydOCvJ_YaBB6eDqVw" title="Use a regular expression against a problem: now you have 2 problems" target="_blank">Use a regular expression against a problem: now you have 2 problems</a> </li>
<li><a href="/rltoken/Y-OVGcJ5cskdXWIBowiE_A" title="Learn Regular Expressions with simple, interactive exercises" target="_blank">Learn Regular Expressions with simple, interactive exercises</a> </li>
</ul>

<h2>Requirements</h2>

<h3>General</h3>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files will be interpreted on Ubuntu 14.04 LTS</li>
<li>All your files should end with a new line</li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>All your Bash script files must be executable</li>
<li>The first line of all your Bash scripts should be exactly <code>#!/usr/bin/env ruby</code></li>
<li>All your regex must be built for the Oniguruma library</li>
</ul>

</div>
