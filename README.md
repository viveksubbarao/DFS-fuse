#### A demo of Distributed File System by Python and fusepy

```sh
ChendeMacBook-Pro:HelloPython chen$ df -h
Filesystem      Size   Used  Avail Capacity  iused    ifree %iused  Mounted on
/dev/disk1     233Gi  153Gi   80Gi    66% 40102119 20879099   66%   /
devfs          198Ki  198Ki    0Bi   100%      684        0  100%   /dev
map -hosts       0Bi    0Bi    0Bi   100%        0        0  100%   /net
map auto_home    0Bi    0Bi    0Bi   100%        0        0  100%   /home
```

```sh
ChendeMacBook-Pro:HelloPython chen$ mkdir MyHost
ChendeMacBook-Pro:HelloPython chen$ ls
Main.py   MyHost    README.md fuse.py   fuse.pyc  myfuse.py
```

```sh
ChendeMacBook-Pro:HelloPython chen$ python myfuse.py /tmp /Users/chen/Repository/PythonProjects/HelloPython/MyHost
```

```sh
ChendeMacBook-Pro:HelloPython chen$ ls MyHost/
13939-kubecfg.key                                      6627-kubecfg.key
16325-kubernetes.ca.crt                                6714-kubecfg.crt
17475-kubernetes.ca.crt                                7490-kubecfg.crt
18638-kubecfg.crt                                      9814-kubernetes.ca.crt
19556-kubecfg.key                                      99-kubecfg.key
20267-kubecfg.key                                      KSOutOfProcessFetcher.0.ppfIhqX0vjaTSb8AJYobDV7Cu68=
21777-kubernetes.ca.crt                                KSOutOfProcessFetcher.501.ppfIhqX0vjaTSb8AJYobDV7Cu68=
28273-kubecfg.crt                                      com.apple.launchd.PAbhvnP5qA
29983-kubernetes.ca.crt                                com.apple.launchd.lbIXRH5kud
3035-kubecfg.crt                                       parallels_crash_dumps
32272-kubecfg.crt                                      wifi-GBstaw.log
3880-kubecfg.key                                       wifi-chkWz1.log
4854-kubernetes.ca.crt                                 wifi-olyQty.log
```

```sh
ChendeMacBook-Pro:HelloPython chen$ df -h
Filesystem      Size   Used  Avail Capacity   iused    ifree %iused  Mounted on
/dev/disk1     233Gi  153Gi   79Gi    66%  40141036 20840182   66%   /
devfs          198Ki  198Ki    0Bi   100%       684        0  100%   /dev
map -hosts       0Bi    0Bi    0Bi   100%         0        0  100%   /net
map auto_home    0Bi    0Bi    0Bi   100%         0        0  100%   /home
Passthrough    233Gi  233Gi   80Gi    75% 18446744073688711434 20840182  100%   /Users/chen/Repository/PythonProjects/HelloPython/MyHost
```

