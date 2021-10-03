# 0x17-web_stack_debugging_3

<h2>Requirements</h2>

<h3>General</h3>

<ul>
<li>All your files will be interpreted on Ubuntu 14.04 LTS</li>
<li>All your files should end with a new line</li>
<li>A <code>README.md</code> file at the root of the folder of the project is mandatory</li>
<li>Your Puppet manifests must pass <code>puppet-lint</code> version 2.1.1 without any errors</li>
<li>Your Puppet manifests must run without error</li>
<li>Your Puppet manifests first line must be a comment explaining what the Puppet manifest is about</li>
<li>Your Puppet manifests files must end with the extension <code>.pp</code> </li>
<li>Files will be checked with Puppet v3.4</li>
</ul>

<h3 class="panel-title">
      0. Strace is your friend
</h3>

<div>
        <span class="label label-info">
          mandatory
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="2867"></span>

<!-- Progress vs Score -->
<div class="task_progress_score_bar" data-task-id="1616" data-correction-id="253630">
        <div class="task_progress_bar">
          <div class="task_score_bar">
          </div>

<!-- Task Body -->
<p><a href="https://youtu.be/uHEzt1QuASo" target="_blank"><img src="https://holbertonintranet.s3.amazonaws.com/uploads/medias/2019/6/f5af5167e65bd3101f76.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20211003%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20211003T221650Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=59a0d50945123e59b4084201824c54360215d295c2262efb365a6a6b0fa86b3c" alt="" style="" /></a></p>

<p>Using <code>strace</code>, find out why Apache is returning a 500 error. Once you find the issue, fix it and then automate it using Puppet (instead of using Bash as you were previously doing).</p>

<p>Hint:</p>

<ul>
<li><code>strace</code> can attach to a current running process</li>
<li>You can use <a href="/rltoken/4KkxME6-3aY9fgfok6HNFA" title="tmux" target="_blank">tmux</a> to run <a href="/rltoken/OUc10nTtuZG65adFVbkYag" title="strace" target="_blank">strace</a> in one window and <code>curl</code> in another one</li>
</ul>

<p>Requirements:</p>

<ul>
<li>Your <code>0-strace_is_your_friend.pp</code> file must contain Puppet code</li>
<li>You can use whatever Puppet resource type you want for you fix</li>
</ul>

<p>Example:</p>

<pre><code>root@e514b399d69d:~# curl -sI 127.0.0.1
HTTP/1.0 500 Internal Server Error
Date: Fri, 24 Mar 2017 07:32:16 GMT
Server: Apache/2.4.7 (Ubuntu)
X-Powered-By: PHP/5.5.9-1ubuntu4.21
Connection: close
Content-Type: text/html

root@e514b399d69d:~# puppet apply 0-strace_is_your_friend.pp
Notice: Compiled catalog for e514b399d69d.ec2.internal in environment production in 0.02 seconds
Notice: /Stage[main]/Main/Exec[fix-wordpress]/returns: executed successfully
Notice: Finished catalog run in 0.08 seconds
root@e514b399d69d:~# curl -sI 127.0.0.1:80
root@e514b399d69d:~#
HTTP/1.1 200 OK
Date: Fri, 24 Mar 2017 07:11:52 GMT
Server: Apache/2.4.7 (Ubuntu)
X-Powered-By: PHP/5.5.9-1ubuntu4.21
Link: &lt;http://127.0.0.1/?rest_route=/&gt;; rel=&quot;https://api.w.org/&quot;
Content-Type: text/html; charset=UTF-8

root@e514b399d69d:~# curl -s 127.0.0.1:80 | grep Holberton
&lt;title&gt;Holberton &amp;#8211; Just another WordPress site&lt;/title&gt;
&lt;link rel=&quot;alternate&quot; type=&quot;application/rss+xml&quot; title=&quot;Holberton &amp;raquo; Feed&quot; href=&quot;http://127.0.0.1/?feed=rss2&quot; /&gt;
&lt;link rel=&quot;alternate&quot; type=&quot;application/rss+xml&quot; title=&quot;Holberton &amp;raquo; Comments Feed&quot; href=&quot;http://127.0.0.1/?feed=comments-rss2&quot; /&gt;
        &lt;div id=&quot;wp-custom-header&quot; class=&quot;wp-custom-header&quot;&gt;&lt;img src=&quot;http://127.0.0.1/wp-content/themes/twentyseventeen/assets/images/header.jpg&quot; width=&quot;2000&quot; height=&quot;1200&quot; alt=&quot;Holberton&quot; /&gt;&lt;/div&gt;  &lt;/div&gt;
                            &lt;h1 class=&quot;site-title&quot;&gt;&lt;a href=&quot;http://127.0.0.1/&quot; rel=&quot;home&quot;&gt;Holberton&lt;/a&gt;&lt;/h1&gt;
        &lt;p&gt;Yet another bug by a Holberton student&lt;/p&gt;
root@e514b399d69d:~#
</code></pre>

</div>
