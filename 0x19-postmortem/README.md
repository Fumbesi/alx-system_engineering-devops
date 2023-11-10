Issue Summary:

During a period from 6:30am to 12:00 pm in Africa/Gaborone, our system faced a problem known as the Apache 500 error. This issue affected a service we provide, called Web Service, causing it to either slow down or become completely unavailable. Around 20% of users experienced difficulties during this time.

The main reason behind the Apache 500 error was a glitch in how our computer system, specifically the Apache server, was set up or how the code was written.

Timeline:

The trouble first came to our attention at 06:01am when our monitoring system alerted us to something being wrong. An engineer on our team also noticed some unusual things happening on the computer.

To figure out what went wrong, we began looking into various parts of our computer system, like server logs and settings. We initially thought that a recent update to the system's code might be the culprit, but this turned out not to be the case.

In the process, we explored some paths that ended up being dead ends. For instance, we spent time checking parts of the system that weren't actually causing the issue. When our initial investigations didn't lead to a solution, we reached out to more experienced team members for help.

Eventually, we managed to resolve the problem by making adjustments to the settings in the Apache server. This involved correcting some configurations and restarting the server.

Root Cause and Resolution:

The root cause of the Apache 500 error was essentially a confusion in the computer's decision-making process, particularly when it came to handling certain requests. To fix this, we made specific changes to the settings, allowing the server to operate smoothly again.

Corrective and Preventative Measures:

To prevent similar issues in the future, we have identified some areas for improvement:

Firstly, we aim to enhance our monitoring system to promptly detect any errors in the Apache server. This involves setting up additional alerts and automated checks for critical server configurations.

Secondly, to address the root cause, we plan to conduct regular audits of our server configurations. This involves checking and documenting the settings to ensure they are correct and up-to-date.

Lastly, in terms of code, we're implementing stricter review processes. This includes more thorough checks to catch potential issues before new code is deployed. We'll also provide ongoing training to our team members to keep them updated on best practices and potential pitfalls.

In conclusion, the Apache 500 error taught us the importance of quick detection, thorough investigation, and collaboration in resolving issues. By implementing the proposed measures, we aim to create a more resilient system, ensuring a smoother experience for our users in the future.
