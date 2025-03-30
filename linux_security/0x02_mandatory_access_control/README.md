#  0. Is your Linux feeling like Fort Knox or a wide-open saloon today? 

SELinux modes: because even Linux needs its choose your adventure security setting. Enforcing is the hard mode, Permissive is the easy mode with cheat codes, and Disabled is the living life on the wild side option. What’s your Linux’s security mood today?

Write a bash script that prints the current SELinux mode on your system.

Depending on your machine, the output could change.
```
┌──(maroua㉿HBTN-LAB)-[~/0x02_mandatory_access_control]
└─🏴 `sudo ./0-analyse_mode.sh`
[sudo] password for maroua: 
SELinux status:                 disabled
```
---

#  1. AppArmor & SELinux: security socks - sometimes a match, sometimes a clash! 

Comparing AppArmor and SELinux is like having a fancy dress party for your system. AppArmor shows up in its unique costumes, and SELinux comes in with its policies, and sometimes they just stare at each other wondering, Are we at the right party or did we overdress?

write a bash script that displays the status of the AppArmor security profiles on a Linux system.

Depending on your machine, the output could change.
```
┌──(maroua㉿HBTN-LAB)-[~/0x02_mandatory_access_control]
└─🏴`sudo ./1-security_match.sh`
[sudo] password for maroua: 
apparmor module is loaded.
30 profiles are loaded.
27 profiles are in enforce mode.
   /usr/bin/evince
   /usr/bin/evince-previewer
   /usr/bin/evince-previewer//sanitized_helper
   /usr/bin/evince-thumbnailer
   /usr/bin/evince//sanitized_helper
   /usr/bin/man
   /usr/lib/NetworkManager/nm-dhcp-client.action
   /usr/lib/NetworkManager/nm-dhcp-helper
   /usr/lib/connman/scripts/dhclient-script
   /usr/lib/cups/backend/cups-pdf
   /usr/lib/snapd/snap-confine
   /usr/lib/snapd/snap-confine//mount-namespace-capture-helper
   /usr/sbin/cups-browsed
   /usr/sbin/cupsd
   /usr/sbin/cupsd//third_party
   /usr/sbin/haveged
   /{,usr/}sbin/dhclient
   docker-default
   libreoffice-senddoc
   libreoffice-soffice//gpg
   libreoffice-xpdfimport
   lsb_release
   man_filter
   man_groff
   nvidia_modprobe
   nvidia_modprobe//kmod
   tcpdump
3 profiles are in complain mode.
   /usr/sbin/sssd
   libreoffice-oosplash
   libreoffice-soffice
0 profiles are in kill mode.
0 profiles are in unconfined mode.
1 processes have profiles defined.
1 processes are in enforce mode.
   /usr/sbin/haveged (722) 
0 processes are in complain mode.
0 processes are unconfined but have a profile defined.
0 processes are in mixed mode.
0 processes are in kill mode.
```
---

#  2. Sudo, show me the SELinux's secret stash of HTTP ports! 

In Linux security, SELinux acts as a robust defender, offering precise access control and enforcing security policies. One of its key functions is managing network ports, guaranteeing secure service operation within set boundaries.

Write a Bash script that lists all ports managed by SELinux and filters out those related to HTTP services.

Depending on your machine, the output could change.
```
┌──(maroua㉿HBTN-LAB)-[~/0x00_mandatory_access_control]
└─🏴 sudo ./2-list_http.sh
[sudo] password for maroua: 
http_cache_port_t              tcp      3128, 8080, 8118, 10001-10010
http_cache_port_t              udp      3130
http_port_t                    tcp      80, 443, 488, 8008, 8009, 8443, 8448
pegasus_http_port_t            tcp      5988
pegasus_https_port_t           tcp      5989
```
---

#  3. Adding a touch of SELinux magic to TCP port! 

Write a Bash script that adds a new SELinux port, http_port_t, for TCP port 81, allowing SELinux to manage security policies related to HTTP traffic on that port.

Depending on your machine, the output could change.
```
┌──(maroua㉿HBTN-LAB)-[~/0x00_mandatory_access_control]
└─🏴 sudo semanage port -l | grep "http_port_t"
http_port_t                    tcp      80, 443, 488, 8008, 8009, 8443, 8448
pegasus_http_port_t            tcp      5988
┌──(maroua㉿HBTN-LAB)-[~/0x00_mandatory_access_control]
└─🏴 sudo ./3-add_port.sh
[sudo] password for maroua: 
┌──(maroua㉿HBTN-LAB)-[~/0x00_mandatory_access_control]
└─🏴 sudo semanage port -l | grep "http_port_t"
http_port_t                    tcp      81, 80, 443, 488, 8008, 8009, 8443, 8448
pegasus_http_port_t            tcp      5988
```
---

#  4. SELinux: Where user mappings are the gatekeepers of the security circus! 

In the domain of SELinux (Security-Enhanced Linux), user mappings play a crucial role in defining the security context and access controls for users on a system.

Write a Bash script that lists all SELinux user mappings.

Depending on your machine, the output could change.
```
┌──(maroua㉿HBTN-LAB)-[~/0x00_mandatory_access_control]
└─🏴` sudo ./4-list_user.sh`
[sudo] password for maroua: 

                Labeling   MLS/       MLS/                          
SELinux User    Prefix     MCS Level  MCS Range                      SELinux Roles

root            sysadm     s0         s0-s0:c0.c1023                 staff_r sysadm_r system_r
staff_u         staff      s0         s0-s0:c0.c1023                 staff_r sysadm_r
sysadm_u        sysadm     s0         s0-s0:c0.c1023                 sysadm_r
system_u        user       s0         s0-s0:c0.c1023                 system_r
unconfined_u    unconfined s0         s0-s0:c0.c1023                 system_r unconfined_r
user_u          user       s0         s0                             user_r
xdm             user       s0         s0                             xdm_r
```
---

#  5. SELinux: Where user gets his VIP pass to the security party! 

In SELinux, user mappings play a crucial role in defining the security context and access controls for users on a system. These mappings allow administrators to specify how Linux login names correspond to SELinux user identities, thereby determining the security policies that apply to each user’s actions.

Write a Bash script that adds a new login mapping in SELinux, linking the Linux login name with the SELinux user identity user_u.

- Your script should accept the new login as an arguments $1.

Depending on your machine, the output could change.
```
┌──(maroua㉿HBTN-LAB)-[~/0x00_mandatory_access_control]
└─🏴 sudo semanage login -l
[sudo] password for maroua: 
Login Name           SELinux User         MLS/MCS Range        Service

__default__          unconfined_u         s0-s0:c0.c1023       *
root                 unconfined_u         s0-s0:c0.c1023       *
sddm                 xdm                  s0-s0                *
┌──(maroua㉿HBTN-LAB)-[~/0x00_mandatory_access_control]
└─🏴 sudo ./5-add_selinux.sh maroua
[sudo] password for maroua: 
┌──(maroua㉿HBTN-LAB)-[~/0x00_mandatory_access_control]
└─🏴 sudo semanage login -l
[sudo] password for maroua: 
Login Name           SELinux User         MLS/MCS Range        Service

__default__          unconfined_u         s0-s0:c0.c1023       *
maroua               user_u               s0                   *
root                 unconfined_u         s0-s0:c0.c1023       *
sddm                 xdm                  s0-s0                *
```
---

#  6. SELinux booleans: where security settings get sassy! 

SELinux booleans are like magical buttons in the world of Linux security. With a simple command, administrators can toggle these switches to customize SELinux’s defenses, ensuring their systems stay safe from digital threats.

Write a Bash script to list all SELinux booleans defined on the system.

Depending on your machine, the output could change.
```
┌──(maroua㉿HBTN-LAB)-[~/0x00_mandatory_access_control]
└─🏴 sudo ./6-list_booleans.sh
[sudo] password for maroua: 
SELinux boolean                State  Default Description

aide_mmap_files                (off  ,  off)  Control if AIDE can mmap files. AIDE can be compiled with the option 'with-mmap' in which case it will attempt to mmap files while running.
allow_cvs_read_shadow          (off  ,  off)  Determine whether cvs can read shadow password files.
allow_execheap                 (off  ,  off)  Allow unconfined executables to make their heap memory executable.  Doing this is a really bad idea. Probably indicates a badly coded executable, but could indicate an attack. This executable should be reported in bugzilla
allow_execmem                  (off  ,  off)  Allow unconfined executables to map a memory region as both executable and writable, this is dangerous and the executable should be reported in bugzilla")
allow_execmod                  (off  ,  off)  Allow all unconfined executables to use libraries requiring text relocation that are not labeled textrel_shlib_t")
allow_execstack                (off  ,  off)  Allow unconfined executables to make their stack executable.  This should never, ever be necessary. Probably indicates a badly coded executable, but could indicate an attack. This executable should be reported in bugzilla")
allow_ftpd_anon_write          (off  ,  off)  Determine whether ftpd can modify public files used for public file transfer services. Directories/Files must be labeled public_content_rw_t.
allow_ftpd_full_access         (off  ,  off)  Determine whether ftpd can login to local users and can read and write all files on the system, governed by DAC.
allow_ftpd_use_cifs            (off  ,  off)  Determine whether ftpd can use CIFS used for public file transfer services.
allow_ftpd_use_nfs             (off  ,  off)  Determine whether ftpd can use NFS used for public file transfer services.
allow_gssd_read_tmp            (off  ,  off)  Determine whether gssd can read generic user temporary content.
...
wm_write_xdg_data              (off  ,  off)  Grant the window manager domains write access to xdg data
xdm_sysadm_login               (off  ,  off)  Allow xdm logins as sysadm
xen_use_fusefs                 (off  ,  off)  Determine whether xen can use fusefs file systems.
xen_use_nfs                    (off  ,  off)  Determine whether xen can use nfs file systems.
xen_use_samba                  (off  ,  off)  Determine whether xen can use samba file systems.
xend_run_blktap                (off  ,  off)  Determine whether xend can run blktapctrl and tapdisk.
xguest_connect_network         (off  ,  off)  Determine whether xguest can configure network manager.
xguest_mount_media             (off  ,  off)  Determine whether xguest can mount removable media.
xguest_use_bluetooth           (off  ,  off)  Determine whether xguest can use blue tooth devices.
xscreensaver_read_generic_user_content (on   ,   on)  Grant the xscreensaver domains read access to generic user content
xserver_allow_dri              (off  ,  off)  Allow DRI access
xserver_gnome_xdm              (off  ,  off)  Use gnome-shell in gdm mode as the X Display Manager (XDM)
xserver_object_manager         (off  ,  off)  Support X userspace object manager
zabbix_can_network             (off  ,  off)  Determine whether zabbix can connect to all TCP ports
```
---

#  7. Sending emails with SELinux? Don't mind if we do! 

Write a Bash script that sets the SELinux boolean httpd_can_sendmail to on permanently.

Depending on your machine, the output could change.
```
┌──(maroua㉿HBTN-LAB)-[~/0x00_mandatory_access_control]
└─🏴 sudo ./7-set_sendmail.sh
[sudo] password for maroua: 
┌──(maroua㉿HBTN-LAB)-[~/0x00_mandatory_access_control]
└─🏴 sudo semanage boolean -lC
[sudo] password for maroua: 
SELinux boolean                State  Default Description

httpd_can_sendmail             (on   ,   on)  Determine whether httpd can send mail.
```
