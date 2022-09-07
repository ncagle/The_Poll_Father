<div id="top"></div>
<!--
comment block
-->


[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
<!-- [![MIT License][license-shield]][license-url] -->

<div align="center">
  <h1 align="center">
    The Poll Father
    <br/>
    <sub>Updated by Nat Cagle</sub>
    <br/>
    <sub>2022-09-07</sub>
  </h1>

  <p align="center">
    Polldaddy Poll.fm Auto Vote Bot
    <br />
    <a href="https://github.com/github_username/repo_name/issues">Report Bug</a>
    ·
    <a href="https://github.com/github_username/repo_name/issues">Request Feature</a>
  </p>
</div>

____________________________________________________________

## About The Project

This is pretty easy to use. Just download the Python script and associated text files. Edit the variables for the form,answer,number of votes, and voting interval.
If using the Tor version, be sure to add your tor hash password found in your torrc file.  

____________________________________________________________

### Built With

Original:

[![Python 2.7][Python2]][Python-url]

Updated to:

[![Python 3][Python3]][Python-url]

____________________________________________________________

### Prerequisites

* Python 2.7+
* <code>pip install requests</code>
* <code>pip install TorRequest</code> (For the Tor version)

____________________________________________________________

### Disclaimer

This script will (**may not -- I have not tested it with new tor functionality**) work on polls that do not allow multiple votes from one person.  The useragents and proxy settings will help try and mask your mass voting, but they will not get you around IP blocks.  If someone wants to give a shot at forking this and adding that functionality, I will be happy to merge it in.

____________________________________________________________

### Example

You want to rig this poll: https://polldaddy.com/poll/9206448/ for the answer "It's a great way to keep kids in line during a crazy time of year.", and you want to vote 1000 times.  The poll_id comes from the url: <code>https://polldaddy.com/poll/<b>9206448</b>/</code>.  The answer_id comes from the looking at the source code for the associated checkbox: <code>\<input type="radio" name="PDI_answer" id="PDI_answer41930288" value="**41930288**"></code>.

Thus, you would want the variables to be set to:
```
poll_id = 9206448
answer_id = 41930288
number_of_votes = 1000
```

____________________________________________________________

<!-- LICENSE
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.
-->


<!-- CONTACT -->
## Contact

Project Link - <a href="https://github.com/ncagle/The_Poll_Father">The Poll Father</a>

Nat Cagle - <a href="https://github.com/ncagle">github.com/ncagle</a>

[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

Master:     Poll Daddy Hack<br/>
Created by: Alex Beals<br/>
Date:       2016-02-20<br/>
<a href="https://github.com/dado3212/PollDaddyHack">dado3212/PollDaddyHack</a>
<br/>

Fork:       Voting Bot (Added Tor functionality)<br/>
Updated by: Kenny McAvoy<br/>
Date:       2017-06-28<br/>
<a href="https://github.com/kennymcavoy/VotingBot">kennymcavoy/VotingBot</a>
<br/>

Fork:       Voting Bot (Poll.fm)<br/>
Updated by: James Chen<br/>
Date:       2020-05-04<br/>
<a href="https://github.com/jchen3652/VotingBot">jchen3652/VotingBot</a>
<br/>

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/ncagle/The_Poll_Father.svg?style=for-the-badge
[contributors-url]: https://github.com/ncagle/The_Poll_Father/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/ncagle/The_Poll_Father.svg?style=for-the-badge
[forks-url]: https://github.com/ncagle/The_Poll_Father/network/members
[stars-shield]: https://img.shields.io/github/stars/ncagle/The_Poll_Father.svg?style=for-the-badge
[stars-url]: https://github.com/ncagle/The_Poll_Father/stargazers
[issues-shield]: https://img.shields.io/github/issues/ncagle/The_Poll_Father.svg?style=for-the-badge
[issues-url]: https://github.com/ncagle/The_Poll_Father/issues
[license-shield]: https://img.shields.io/github/license/ncagle/The_Poll_Father.svg?style=for-the-badge
[license-url]: https://github.com/ncagle/The_Poll_Father/blob/main/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/ncagle/
[Python2]: https://img.shields.io/badge/python-2.7-blue?style=for-the-badge&logo=python&logoColor=white
[Python3]: https://img.shields.io/badge/python-3-purple?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org/
