##Zeus Immunity

While doing research on Zeus malware and its MiTB attacks, I came across with the need to retrieve from a sample it's targets.

While there is work to retrieve from a sample it's configuration (CNC server, RC4 key, registry keys) I didn't find any that retrieved the webinjects part from a sample.

The plugin leaverages how Zeus does the MiTB:
* It hooks wininet.dll functions for iexplore (or nspr4.dll for firefox)
* The way it hooks is to insert a JMP instruction at the beginning of a hooked function (e.g. HttpSendRequestA)

By taking the jump, we start search the memory for instructions that resemble decryption / decoding routines. By setting a breakpoint at the end of those routines, we should be able to retrieve the targets URL and the injection to perform.

Tested on:

* Windows 7 SP1 x64
* Zeus 2.x [built with leaked source code](https://github.com/Visgean/Zeus)
* Immunity Debugger 1.85
