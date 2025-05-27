##Figuring this out might have been the most frustrating part of making this game.
##Deleting files is dangerous. Don't screw with this please. I have this part hidden for a reason.
##I hold no liability for anything that happens to your computer if you tamper with this functionality.

##Update (2025): Ok I implemented it in a way where I'm not as nervous about it anymore.
##Instead of deleting the entire directory, we now delete each file we expect should exist.
##This way we will never delete anything we do not intend to

label the_end:
    $_skipping = False
    $persistent._clear() 
    $renpy.save_persistent()
    $delete_all_saves()

    show screen delete_screen_runner
    show screen delete_text

    $renpy.pause(delay=6, hard=True)

    if not config.developer:
        python:
            import os
            os.chdir(renpy.config.basedir)
            for file in ALL_FILES:
                try:
                    if os.path.isfile(file):
                        os.remove(file)
                except:
                    pass
            for dir in ALL_DIRS:
                try:
                    if os.path.isdir(dir):
                        os.rmdir(dir)
                except:
                    pass

            if renpy.windows:
                import subprocess
                tempBatFileName='goodbye.bat'
                windows_bat_string = "@echo off\ntimeout /t 3 >nul"
                for file in ALL_FILES:
                    if os.path.isfile(file):
                        file_win = file.replace("/", "\\")
                        windows_bat_string += "\ndel /f /q \"" + file_win + "\""
                for dir in ALL_DIRS:
                    if os.path.isdir(dir):
                        dir_win = dir.replace("/", "\\")
                        windows_bat_string += "\nrmdir \"" + dir_win + "\""
                windows_bat_string += "\ndel /f /q \"" + tempBatFileName + "\""
                open(tempBatFileName, 'w').write(windows_bat_string)
                CREATE_NO_WINDOW = 0x08000000
                subprocess.Popen(config.basedir + "/" + tempBatFileName, close_fds=True, creationflags=CREATE_NO_WINDOW)
    python:
        renpy.quit()