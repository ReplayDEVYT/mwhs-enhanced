## This file contains options that can be changed to customize your game.
##
## Lines beginning with two '#' marks are comments, and you shouldn't uncomment
## them. Lines beginning with a single '#' mark are commented-out code, and you
## may want to uncomment them when appropriate.


## Basics ######################################################################

## A human-readable name of the game. This is used to set the default window
## title, and shows up in the interface and error reports.
##
## The _() surrounding the string marks it as eligible for translation.

define config.name = _("MetaWare High School (Demo)")


## Determines if the title given above is shown on the main menu screen. Set
## this to False to hide the title.

define gui.show_name = False
#57686174 2073686f 77732069 6e737465 61643f

## The version of the game.
define config.version = "1.1.0.0"
#436f6e66 69726d73 206d756c 74697665 7273696f 6e207468 656f7279 21212121 2121


## Text that is placed on the game's about screen. Place the text between the
## triple-quotes, and leave a blank line between paragraphs.

define gui.about = _p("""
Writing, Coding, and Music by The Creator.
Mod by mizmii

Charatcter Art by SparkBag.
Background Art by Keeby.
Logo Art by Alexander A. McDonald.

Released on April 2nd, 2020.
""")

#57686174 20646f65 73203230 3230206d 65616e
#496e7465 726e6574 2073686f 7773206e 6f206869 74732066 6f722061 6e79206f 66207468 65736520 70656f70 6c65

## A short name for the game used for executables and directories in the built
## distribution. This must be ASCII-only, and must not contain spaces, colons,
## or semicolons.

define build.name = "MetaWareHighSchoolDemo"


## Sounds and music ############################################################

## These three variables control which mixers are shown to the player by
## default. Setting one of these to False will hide the appropriate mixer.

define config.has_sound = True
define config.has_music = True
define config.has_voice = False

#57687920 69732076 6f696365 2046616c 73653f20 57652068 61766520 766f6963 65732e2e 2e

define config.default_music_volume = 0.1
define config.default_sfx_volume = 1.0


## To allow the user to play a test sound on the sound or voice channel,
## uncomment a line below and use it to set a sample sound to play.

# define config.sample_sound = "sample-sound.ogg"
# define config.sample_voice = "sample-voice.ogg"


## Uncomment the following line to set an audio file that will be played while
## the player is at the main menu. This file will continue playing into the
## game, until it is stopped or another file is played.


define config.main_menu_music = menumusic


## Transitions #################################################################
##
## These variables set transitions that are used when certain events occur.
## Each variable should be set to a transition, or None to indicate that no
## transition should be used.

## Entering or exiting the game menu.

define config.enter_transition = dissolve
define config.exit_transition = dissolve


## Between screens of the game menu.

define config.intra_transition = dissolve


## A transition that is used after a game has been loaded.

define config.after_load_transition = Dissolve(0.5)


## Used when entering the main menu after the game has ended.

define config.end_game_transition = None


## SKIP TO MY LOU MY DARLLLLLING
define config.allow_skipping = True
define config.skip_indicator = True


## A variable to set the transition used when the game starts does not exist.
## Instead, use a with statement after showing the initial scene.


## Window management ###########################################################
##
## This controls when the dialogue window is displayed. If "show", it is always
## displayed. If "hide", it is only displayed when dialogue is present. If
## "auto", the window is hidden before scene statements and shown again once
## dialogue is displayed.
##
## After the game has started, this can be changed with the "window show",
## "window hide", and "window auto" statements.

define config.window = "hide"


## Transitions used to show and hide the dialogue window

define config.window_show_transition = Dissolve(.5)
define config.window_hide_transition = Dissolve(0)


## Preference defaults #########################################################

## Controls the default text speed. The default, 0, is infinite, while any other
## number is the number of characters per second to type out.

default preferences.text_cps = 60
#646f6573 206e6f74 206d6174 63682064 65666175 6c742063 68617261 63746572 2074616c 6b696e67 20737065 656473

## The default auto-forward delay. Larger numbers lead to longer waits, with 0
## to 30 being the valid range.

default preferences.afm_time = 15


## Save directory ##############################################################
##
## Controls the platform-specific place Ren'Py will place the save files for
## this game. The save files will be placed in:
##
## Windows: %APPDATA\RenPy\<config.save_directory>
##
## Macintosh: $HOME/Library/RenPy/<config.save_directory>
##
## Linux: $HOME/.renpy/<config.save_directory>
##
## This generally should not be changed, and if it is, should always be a
## literal string, not an expression.

define config.save_directory = "MetawareHighSchoolDemo-1554161441"
#44697265 63746f72 7920666f 756e642e 20446174 6120696e 61636365 73736962 6c652e20 416c736f 20766572 7920736d 616c6c20 286c696b 656c7920 756e7573 65642075 6e74696c 20706c61 79657220 61727269 76657329

## Icon ########################################################################
##
## The icon displayed on the taskbar or dock.


define config.window_icon = "icons/chrisicon.png"

##Sorry gamers. But you can't turn back (unless you are me).
if not config.developer:
    define config.hard_rollback_limit = 0
else:
    define config.hard_rollback_limit = 100
#4966206f 6e6c7920 4920636f 756c6420 6368616e 67652074 68697320 76616c75 652e2e2e


## Build configuration #########################################################
##
## This section controls how Ren'Py turns your project into distribution files.

init python:

    ## The following functions take file patterns. File patterns are case-
    ## insensitive, and matched against the path relative to the base directory,
    ## with and without a leading /. If multiple patterns match, the first is
    ## used.
    ##
    ## In a pattern:
    ##
    ## / is the directory separator.
    ##
    ## * matches all characters, except the directory separator.
    ##
    ## ** matches all characters, including the directory separator.
    ##
    ## For example, "*.txt" matches txt files in the base directory, "game/
    ## **.ogg" matches ogg files in the game directory or any of its
    ## subdirectories, and "**.psd" matches psd files anywhere in the project.

    ## Classify files as None to exclude them from the built distributions.

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify('dev/', None)

    ## To archive files, classify them as 'archive'.

    build.archive("music", "all")
    build.archive("images", "all")
    build.archive("data", "all")
    build.classify('**.ogg', 'music')
    build.classify("**.png", "images")
    build.classify("**.jpeg", "images")
    build.classify("**.rpyb", "data")
    build.classify("**.rpymc", "data")
    build.classify("**.rpym", "data")
    build.classify("**.rpyc", "data")
    build.classify("game/fonts/**", "data")
    build.classify("game/XX_demoscript_XX/**", "data")
    build.classify("game/scripts/words.rpy", "data")
    build.classify("game/scripts/trailer.rpy", "data")
    build.classify("game/scripts/shi.rpy", "data")
    build.classify("game/scripts/file_list.rpy", "data")
    
    #73686920 3d206465 617468
    #54686973 20697320 616c6c20 74686520 64617461 20492063 616e2774 20616363 6573732e 2e2e7468 6973206d 75737420 62652077 68792e


    ## Files matching documentation patterns are duplicated in a mac app build,
    ## so they appear in both the app and the zip file.

    build.documentation('*.html')
    build.documentation('*.txt')


## Set this to a string containing your Apple Developer ID Application to enable
## codesigning on the Mac. Be sure to change it to your own Apple-issued ID.

## define build.mac_identity = "Apple Development: notfungamesdeveloper@gmail.com (4N2PMH52X8)"
#54726965 6420656d 61696c69 6e672074 68697320 6163636f 756e742e 20466169 6c656420 746f2073 656e642e

## A Google Play license key is required to download expansion files and perform
## in-app purchases. It can be found on the "Services & APIs" page of the Google
## Play developer console.

# define build.google_play_key = "..."


## The username and project name associated with an itch.io project, separated
## by a slash.

# define build.itch_project = "renpytom/test-project"
#41636365 73732074 6f206974 63682e69 6f20616c 6c6f7765 642e204e 6f206d65 6e74696f 6e206f66 204d6574 61576172 652e
#72656e70 79746f6d 203d3d20 63726561 746f7220 6f662052 656e5079

define config.developer = "auto"

###Other

default preferences.gl_powersave = False
default preferences.gl_tearing = False
# ;)

### (2025) Options to make the game have the same behavior as it was released in (version 7.2.2)
##https://www.renpy.org/doc/html/incompatible.html
#4163636f 7264696e 6720746f 2061626f 76652067 616d6520 69732072 656c6561 73656420 6f6e2022 41707269 6c20326e 64203230 3230222e 20466976 65202279 65617222 20646966 66657265 6e63652c 206f7220 31383237 20646179 732e2046 696e616c 2067616d 65206d6f 7265206c 696b656c 7920746f 20657869 73742069 66207765 20617265 20746861 74206f6c 643f

#"""Disable""" mipmapping to match old renderer look 
define config.gl_lod_bias = -9999
#This setting is ignored, but turning this off reveals the option to turn on old renderer (gl1) in the graphics menu
define config.gl2 = False 

#7.3.0 
define config.keyword_after_python = True
define config.keep_side_render_order = False
define config.say_attribute_transition_callback_attrs = False

#7.3.3 
define config.early_start_store = True
define config.compat_viewport_minimum = True

#7.4.1
define config.pause_with_transition = True

#7.4.3
define config.dismiss_blocking_transitions = False

#7.4.7
define config.adjust_minimums = False
define config.atl_start_on_show = False
define config.input_caret_blink = False

#7.4.9
define config.relative_transform_size = False

#7.4.11
define config.always_unfocus = False

#7.5.0
define config.box_skip = False
define config.crop_relative_default = False
define config.layeredimage_offer_screen = False

#7.6.0
define config.fadeout_audio = 0.0
define config.linear_fades = True
define config.search_prefixes += ["images/"]
define config.sticky_layers = [ ]
define config.lenticular_bracket_ruby = False
define config.quadratic_volumes = True
define config.at_transform_compare_full_context = True

#7.7.0
define config.interpolate_exprs = False
define config.simple_box_reverse = True
define config.transitions_use_child_placement = False
define config.containers_pass_transform_events = set()
define config.say_replace_event = False
define config.screens_never_cancel_hide = False

#7.7.2
define config.fill_shrinks_frame = True

#7.8.0
define config.window_functions_set_auto = True
define config.window_next = False
define config.munge_in_strings = False
define config.limit_transform_crop = True
define config.limit_transform_crop = "only_float"
