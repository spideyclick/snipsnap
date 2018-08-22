# snipsnap

This program is for monitoring and making quick edits to the clipboard. It's intended for use on Windows, though with some work could be made to use for Linux.

Use with AutoHotkey and add a shortcut to your startup folder to truly make it a fast app. You can run this autohotkey script on startup to make editing the clipboard as easy as hitting a shortchut.

DetectHiddenWindows, On
#c::
  WinRestore, snipsnap
  WinActivate, snipsnap
  sleep, 4000
  WinHide, snipsnap
return
