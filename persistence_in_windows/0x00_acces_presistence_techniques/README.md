#  0. Persistence Using Startup Folder 

In this lab, you will explore how attackers can maintain persistence on a machine by utilizing the Startup folder. The goal is to understand how programs can be configured to execute automatically when a user logs in, ensuring continuous access to the system. You will need to explore the Windows Startup folders, identify any malicious files placed there, and retrieve specific information to validate persistence.

**Steps:**

1-Locate the Startup Folders:
2-Explore Files in the Startup Folder: Check both the user-specific and global Startup folders for any executable or script files that may indicate persistence.

---

#  1. Persistence Using Registry Autorun 

In this task, you explored how malware authors can maintain persistence on a Windows system by leveraging the registry to automatically execute programs upon user login. By modifying specific registry keys under HKEYCURRENTUSER or HKEYLOCALMACHINE, you learned how programs, such as a PowerShell script, can be configured to run persistently.
Through careful investigation of the registry, you identified a script that executed automatically at login, searched for encoded information, and decoded the hidden flag within the PowerShell script. Once the flag was extracted, you ensured that all traces of your actions were thoroughly cleaned from the system.
This task also emphasized the importance of persistence mechanisms used by malicious actors and demonstrated the need for proper system hygiene by cleaning up all changes made to the system—removing the registry entries and any related files, clearing command history, and ensuring the environment was restored to its original state.
By completing this exercise, you gained hands-on experience in modifying system configurations to gain persistent access and learned the steps necessary to remove any traces left behind during the process.

**Hints:**

- Use the Registry Editor (regedit) to modify registry keys.
- Ensure that you have appropriate permissions to make changes to the global registry hive.
- Consider using monitoring tools to observe any changes made during this process.

---

#  2. Persistence Using Services 

In this lab, you explored how attackers can establish persistence on a Windows system by exploiting the Windows Services feature. By configuring a service to run automatically on system boot, you learned how malicious actors can ensure their programs continue running in the background without user intervention.
Through your investigation, you identified the **flag3** service and discovered a hidden base64-encoded password within its description. By decoding the password, you demonstrated how services can be used as a persistence mechanism. Additionally, this exercise highlighted the importance of monitoring and securing Windows Services to prevent unauthorized persistence.
The lab also emphasized the need for vigilance in detecting hidden services and understanding how attackers might exploit system features to maintain access. By completing the task and decoding the flag, you gained valuable insights into how system services can be manipulated to ensure continuous control over a compromised machine.
Lastly, it’s important to note that cleaning up the system after such tasks, including removing any created services, is essential to maintain security and integrity.

---

#  3. Persistence Using Scheduled Tasks 

As cybersecurity threats evolve, attackers continuously find ways to exploit legitimate system functionalities. Windows Scheduled Tasks provide a powerful automation mechanism, but they can also be manipulated to establish persistent access on a compromised system.
This task will guide you through the process of creating and configuring scheduled tasks, helping you understand their potential for abuse and how attackers use them for persistence.

**Challenge:**

Explore the Task Scheduler to locate a scheduled task. Within the task’s description, you will find the flag. This challenge demonstrates how attackers may exploit scheduled tasks to establish persistent access on a compromised system, and hide important information, such as flags, within the task’s details.
**Hints:**

- Use PowerShell cmdlets for efficient task management.
- Consider different trigger types (time-based, event-based) and how they can be exploited.
- Explore detection mechanisms to identify unauthorized scheduled tasks.

**Target Task Configuration:**

- Triggers: System startup or user logon
- Task Creation Method: Task Scheduler GUI orPowerShell
