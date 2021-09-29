# 0x18. Webstack monitoring
<h2>Learning Objectives</h2>

<p>At the end of this project, you are expected to be able to <a href="/rltoken/SPQiERiTz9g8iT8tsfxZVQ" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>Why is monitoring needed</li>
<li>What are the 2 main area of monitoring</li>
<li>What are access logs for a web server (such as Nginx)</li>
<li>What are error logs for a web server (such as Nginx)</li>
</ul>

<h2>Requirements</h2>

<h3>General</h3>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files will be interpreted on Ubuntu 16.04 LTS</li>
<li>All your files should end with a new line</li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>All your Bash script files must be executable</li>
<li>Your Bash script must pass <code>Shellcheck</code> (version <code>0.3.7</code>) without any error</li>
<li>The first line of all your Bash scripts should be exactly <code>#!/usr/bin/env bash</code></li>
<li>The second line of all your Bash scripts should be a comment explaining what is the script doing</li>
</ul>

## Tasks

<h3 class="panel-title">
      0. Sign up for Datadog and install datadog-agent
    </h3>

<div>
        <span class="label label-info">
          Mandatory
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="2867"></span>

    <!-- Progress vs Score -->

    <!-- Task Body -->
<p>For this task head to <a href="/rltoken/Uho9kxbX9KHCSYAQ-Zl1AQ" title="https://www.datadoghq.com/" target="_blank">https://www.datadoghq.com/</a> and sign up for a free <code>Datadog</code> account. When signing up, you&rsquo;ll have the option of selecting statistics from your current stack that <code>Datadog</code> can monitor for you. Once you have an account set up, follow the instructions given on the website to install the <code>Datadog</code> agent. </p>

<p><img src="https://holbertonintranet.s3.amazonaws.com/uploads/medias/2019/6/6b0ea6345a6375437845.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20210929%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20210929T192135Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=b4198b7975a4fb42430763abc2a575699dd720a14aa221060985304c117bbc5e" alt="" style="" /></p>

<ul>
<li>Sign up for Datadog - <strong>Please make sure you are using the US website of Datagog (.com)</strong></li>
<li>Install <code>datadog-agent</code> on <code>web-01</code></li>
<li>Create an <code>application key</code></li>
<li>Copy-paste in your Intranet user profile (<a href="/rltoken/2D6j3Y6G9c8o_t278-Cu_w" title="here" target="_blank">here</a>) your DataDog <code>API key</code>  and your DataDog <code>application key</code>.</li>
<li>Your server <code>web-01</code> should be visible in Datadog under the host name <code>XX-web-01</code>

<h3 class="panel-title">
      1. Monitor some metrics
</h3>

<div>
        <span class="label label-info">
          Mandatory
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="2867"></span>

    

    <!-- Progress vs Score -->

    <!-- Task Body -->
<p>Among the litany of data your monitoring service can report to you are system metrics. You can use these metrics to determine statistics such as reads/writes per second, which can help your company determine if/how they should scale. Set up some <code>monitors</code> within the <code>Datadog</code> dashboard to monitor and alert you of a few. You can read about the various system metrics that you can monitor here: <a href="/rltoken/naY47nur2yPJNw8tdACnzQ" title="System Check" target="_blank">System Check</a>.</p>

<p><img src="https://holbertonintranet.s3.amazonaws.com/uploads/medias/2019/6/6a4551974aadc181e97a.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20210929%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20210929T192135Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=d928382ba074facac1852b71bc2ef1ca83673909b11dc9591856cd43c620e784" alt="" style="" /></p>

<ul>
<li>Set up a monitor that checks the number of read requests issued to the device per second.</li>
<li>Set up a monitor that checks the number of write requests issued to the device per second.</li>
</ul>

  </div>

<h3 class="panel-title">
      2. Create a dashboard
</h3>

<div>
        <span class="label label-info">
          Mandatory
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="2867"></span>

    <!-- Progress vs Score -->

    <!-- Task Body -->
<p>Now create a dashboard with different metrics displayed in order to get a few different visualizations.</p>

<ul>
<li>Create a new <code>dashboard</code></li>
<li>Add at least 4 <code>widgets</code> to your dashboard. They can be of any type and monitor whatever you&rsquo;d like</li>
<li>Create the answer file <code>2-setup_datadog</code> which has the <code>dashboard_id</code> on the first line. <strong>Note</strong>: in order to get the id of your dashboard, you may need to use <a href="/rltoken/VrzQP39UUFMmAKZx0IZLuw" title="Datadog&#39;s API" target="_blank">Datadog&rsquo;s API</a></li>
</ul>

  </div>