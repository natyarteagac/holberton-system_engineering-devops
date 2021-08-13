# 0x0A. Configuration management
<div class="gap" id="project-description">
  <h2>Background Context</h2>

<p><a href="https://youtu.be/ogYLFyp68cI" target="_blank"><img src="https://holbertonintranet.s3.amazonaws.com/uploads/medias/2019/6/6a0a8024f2b1c47a9d1e.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20210813%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20210813T202541Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=df12293a15713d9aca601a88cb0a0b3e89e51b48d6f5aa4fe2b5cdd0c5fc2052" alt="" style="" /></a></p>

<p>When I was working for SlideShare, I worked on an auto-remediation tool called <a href="/rltoken/ftFvBjxNPLoWcF9eHaK8yw" title="Skynet" target="_blank">Skynet</a> that monitored, scaled and fixed Cloud infrastructure. I was using a parallel job-execution system called MCollective that allowed me to execute commands to one or multiple servers at the same time. I could apply an action to a selected set of servers by applying a filter such as the server&rsquo;s hostname or any other metadata we had (server type, server environment&hellip;). At some point, a bug was present in my code that sent <code>nil</code> to the filter method. </p>

<p>There were 2 pieces of bad news:</p>

<ol>
<li>When MCollective receives <code>nil</code> as an argument for its filter method, it takes this to mean &lsquo;all servers&rsquo;</li>
<li>The action I sent was to terminate the selected servers</li>
</ol>

<p>I started the parallel job-execution and after some time, I realized that it was taking longer than expected. Looking at logs I realized that I was shutting down SlideShare&rsquo;s entire document conversion environment. Actually, 75% of all our conversion infrastructure servers had been shut down, resulting in users not able to convert their PDFs, powerpoints, and videos&hellip; Pretty bad!</p>

<p>Thanks to Puppet, we were able to restore our infrastructure to normal operation in under 1H, pretty impressive. Imagine if we had to do everything manually: launching the servers, configuring and linking them, importing application code, starting every process, and obviously, fixing all the bugs (you should know by now that complicated infrastructure always goes sideways)&hellip;</p>

<p>Obviously writing Puppet code for your infrastructure requires an investment of time and energy, but in the long term, it is for sure a must-have.</p>

<p><img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/292/4i8il3B.gif" alt="" style="" /></p>

<p>That was me ^_^&lsquo;: <a href="/rltoken/uHU1llO2UZXg8_funEgpJA" title="https://twitter.com/devopsreact/status/836971570136375296" target="_blank">https://twitter.com/devopsreact/status/836971570136375296</a></p>

<h2>Resources</h2>

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="/rltoken/r-NmkYO8bxIKp2qEx2ZjKQ" title="Intro to Configuration Management" target="_blank">Intro to Configuration Management</a> </li>
<li><a href="/rltoken/fuhnsI9_1_F4GrHwGT3GxA" title="Puppet resource type: file" target="_blank">Puppet resource type: file</a> (<em>check &ldquo;Resource types&rdquo; for all manifest types in the left menu</em>)</li>
<li><a href="/rltoken/Fqmb5rnChQgYAypvKoTxAQ" title="Puppet&#39;s Declarative Language: Modeling Instead of Scripting" target="_blank">Puppet&rsquo;s Declarative Language: Modeling Instead of Scripting</a></li>
<li><a href="/rltoken/oezu0m_hJ8nEVA6a9o17Tw" title="Puppet lint" target="_blank">Puppet lint</a> </li>
<li><a href="/rltoken/N70cVw8mG3707He-OxjP1w" title="Puppet emacs mode" target="_blank">Puppet emacs mode</a> </li>
</ul>

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
</ul>

# Tasks
<h3 class="panel-title">
      0. Create a file
    </h3>

<div>
        <span class="label label-info">
          Mandatory
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="2867"></span>

<p>Using Puppet, create a file in <code>/tmp</code>.</p>
<p>Requirements:</p>

<ul>
<li>File path is <code>/tmp/holberton</code></li>
<li>File permission is <code>0744</code></li>
<li>File owner is <code>www-data</code></li>
<li>File group is <code>www-data</code></li>
<li>File contains <code>I love Puppet</code></li>
</ul>
<h3 class="panel-title">
      1. Install a package
    </h3>

<div>
        <span class="label label-info">
          Mandatory
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="2867"></span>

<p>Using Puppet, install <code>puppet-lint</code>.</p>

<p>Requirements:</p>

<ul>
<li>Install <code>puppet-lint</code></li>
<li>Version must be <code>2.1.1</code></li>
</ul>
    <h3 class="panel-title">
      2. Execute a command
    </h3>

<div>
        <span class="label label-info">
          Mandatory
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="2867"></span>

<p>Using Puppet, create a manifest that kills a process named <code>killmenow</code>.</p>

<p>Requirements:</p>

<ul>
<li>Must use the <code>exec</code> Puppet resource</li>
<li>Must use <code>pkill</code> </li>
</ul>
