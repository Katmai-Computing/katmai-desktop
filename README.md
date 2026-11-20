# Katmai desktop (beta)

Learn how a qubit works with six free lessons and a spin simulation. Everything works offline, with no account and no hardware. If you have a Katmai board, you can also connect it to check the electronics and take a live receiver reading.

## Download

| Computer | Installer |
| --- | --- |
| Mac with Apple silicon (M1 or later) | [Katmai-Mac-AppleSilicon.dmg](https://github.com/Katmai-Computing/katmai-desktop/releases/latest/download/Katmai-Mac-AppleSilicon.dmg) |
| Mac with an Intel processor | [Katmai-Mac-Intel.dmg](https://github.com/Katmai-Computing/katmai-desktop/releases/latest/download/Katmai-Mac-Intel.dmg) |
| Windows 10 or 11 (64-bit) | [Katmai-Windows-Setup.exe](https://github.com/Katmai-Computing/katmai-desktop/releases/latest/download/Katmai-Windows-Setup.exe) |

Not sure which Mac you have? Open the Apple menu and choose **About This Mac**. If it lists a **Chip** such as Apple M1, M2, M3 or M4, choose Apple silicon. If it lists a **Processor** made by Intel, choose Intel.

## Install on a Mac

1. Open the downloaded `.dmg` file and drag **Katmai** into **Applications**.
2. Open **Katmai** from your Applications folder.
3. This beta is not yet notarized by Apple, so the first time macOS says it could not verify Katmai. Click **Done**. Then open **System Settings**, choose **Privacy & Security**, scroll down to the "Katmai was blocked" message and click **Open Anyway**. Confirm with **Open Anyway** and your password. After this, Katmai opens normally.

## Install on Windows

1. Run **Katmai-Windows-Setup.exe**.
2. This beta is not yet code signed, so Windows may show "Windows protected your PC". Click **More info**, then **Run anyway**.
3. Katmai installs for your account and opens. You can find it later in the Start menu.

## Updating

Download the newest installer and install it over the old version. Your course progress stays on your computer.

## Checking the download (optional)

Each release includes `SHA256SUMS.txt`. On a Mac, run `shasum -a 256 Katmai-Mac-AppleSilicon.dmg`. On Windows, run `Get-FileHash Katmai-Windows-Setup.exe` in PowerShell. Compare the result with the file.

---

Made by [Katmai Computing](https://www.katmaicomputing.com). This repository only hosts the installers.
