---
title: kernel upgrade bustage
date: 2010-03-22
uuid: urn:uuid:4125ab24-35f4-11df-8495-08002769b3d1
---

Ubuntu upgraded my VM to a new kernel a few days ago.  As I've come to expect,
this broke openafs and the virtualbox kernel modules.  This is exactly what
[dkms][] is supposed to avoid, by rebuilding your kernel modules whenever your
kernel changes, but dkms is stymied by Ubuntu's package manager here.

The problem is that while there's a package which contains the latest kernel,
there's no package which contains the corresponding kernel headers; you need to
get those manually.  So when your kernel package is upgraded, dkms can't
rebuild your kernel modules, since you lack the new headers.

This is silly, but it's easy enough to get your kernel modules working again:

 * Get the new kernel headers:

        sudo apt-get install linux-headers-$(uname -r)

 * Now tell dkms to rebuild each of your kernel modules.  There's probably a
   way to do this all at once, but it's easy enough to specify each module.
   For instance, to rebuild openafs, I run:

        sudo dkms build -m openafs -v 1.4.11

 * You may also want to delete your outdated linux-headers packages.  You can list them with

        dpkg -l | grep linux-headers

   and remove them with `apt-get remove (package-name)`.

I filed a [ticket][] about this with Ubuntu.  If it's bothering you too, please
vote for it!

[dkms]: http://en.wikipedia.org/wiki/Dynamic_Kernel_Module_Support
[ticket]: http://brainstorm.ubuntu.com/idea/23637/
