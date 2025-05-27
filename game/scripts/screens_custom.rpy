
style centered_style:
    xalign 0.5
    yalign 0.25
    spacing 20
    xmaximum 1500
    box_wrap True
    color (0, 0, 0)
    

style note_style:
    color "#000"   
    font "fonts/khand.TTF"
    size 34
    spacing 20
    line_leading -5
    outlines [ (absolute(1), "999", absolute(0), absolute(0)) ]

style note_ps_style is note_style:
    yoffset 28
    xoffset 0

style fraction_style is note_style:
    justify centered
    size 42
    xoffset 1225
    yoffset -120
    
transform tweak_fraction:
    rotate 15

init python:
    def EndingsLeftString(num_of_endings):
        completed_endings_count = str(len(persistent.completed_endings))
        total = str(num_of_endings)
        return completed_endings_count + "/" + total

screen Final_Note(message, front=True):

    if front:
        image "other/note_front.png"
        $back = False
    else:
        image "other/note_back.png"
        $back = True
        

    vbox:
        style "centered_style"
        if back:
            $fraction = str(len(persistent.completed_endings))+"/"+str(num_of_endings)
            text fraction style "fraction_style" at tweak_fraction

        for msg in message:
            if msg == message[-1]:
                text msg style "note_ps_style"
            else:
                text msg style "note_style"




init python:
    ###code by discord user Remix#1655
    ###A clever way for detecting when the mouse has moved during a choice screen and setting a timer to auto-advance
    def mouse_move_makes_menu_select():
        if not "current_mouse_pos" in globals():
            globals()["current_mouse_pos"] = renpy.get_mouse_pos()
        else:
            if renpy.get_mouse_pos() != globals()["current_mouse_pos"]:
                items = renpy.current_screen().scope['items']
                item_captions = [i[0] for i in items]

                if not "Fail" in item_captions:
                    raise ValueError, "No menu choice found for 'Fail'"

                fail_item = item_captions.index("Fail")
                renpy.ui.pausebehavior( 0.0, items[fail_item][1].value )
                renpy.restart_interaction()

screen mouse_move_auto_choice(items, duration=0.3):
    style_prefix "choice"

    vbox:
        for i in items:
            if i.caption != "Fail": ## we do NOT show the Fail caption
                textbutton i.caption action i.action
    timer duration action Function(mouse_move_makes_menu_select) repeat True



screen fast_choice(items, duration=10.0):

    style_prefix "choice"

    vbox:
        for i in items:
            if i.caption != items[-1].caption: ## we do NOT show the last caption
                textbutton i.caption action i.action
    timer duration action items[-1].action #Do last action if timer expires



screen choice_end(items):
    style_prefix "choice_end"

    vbox:
        for i in items:
            textbutton i.caption action i.action


style choice_end_vbox is vbox
style choice_end_button is button
style choice_end_button_text is button_text

style choice_end_vbox:
    xalign 0.5
    yalign 0.5
    yanchor 0.5
    spacing 150

style choice_end_button is default:
    #properties gui.button_properties("choice_button")
    xalign 0.5   

style choice_end_button_text is default:
    #properties gui.button_text_properties("choice_button")
    font "fonts/tommys.ttf"
    size 100
    xalign 0.5



screen okay(message, okay_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                textbutton _("Okay") action okay_action


##Special thanks to @Shawna#6408 for helping me getting this one to work.

default FILES = renpy.list_files(common=True)
define file_display_array = []

'''
(2025) This code is responsible for the crash that many players saw when ending the game for the first time.
Seeing the crash in livestreams, I wrote it off being not my fault thinking the game delting itself was somehow responsible and never looked into it properly, 
But alas, it had nothing to do with that. My inexperience was to blame all along. As a tribute to my neglignece, here is the original code.

    def addFileToDisplayArray():
        global FILES, file_display_array
        if len(FILES) >= 0:
            file_display_array.append(str(FILES.pop()))
            file_display_array.append(str(FILES.pop()))
            file_display_array.append(str(FILES.pop()))
            renpy.show_screen(_screen_name="delete_screen_display", msg=file_display_array )

I distinctly remember duplicating the line that pops the array as a hacky way to change the speed of the text displaying.
Little did I know it would result in a very nasty bug: the game crashing because it tried to pop an empty list!
'''

init python:
    def addFileToDisplayArray():
        global FILES, file_display_array
        if len(FILES) >= 3:
            file_display_array.append(str(FILES.pop()))
            file_display_array.append(str(FILES.pop()))
            file_display_array.append(str(FILES.pop()))
            renpy.show_screen(_screen_name="delete_screen_display", msg=file_display_array )

screen delete_screen_runner():
    timer 0.00001 action Function(addFileToDisplayArray) repeat True
    

screen delete_screen_display(msg):
    zorder 0
    # style_prefix "notify"

    hbox:
        text "[msg]":
            size 13


default deletePercent = 0.0

screen delete_text():

    vbox:
        xalign 0.5
        yalign 0.5
        spacing 50
        text "DELETING UNIVERSE...":
            xalign 0.5
            size 124
        # bar value AnimatedValue(value=deletePercent, delay=10.0):
        #     left_gutter 200
        #     right_gutter 200

        #timer 0.1 action Function(UpGoesTheBar(5.0)) repeat True


#(2025) custom graphics screen, copied so that we can change the behavior of the return button
#from a Return(0) to a Hide() like the accessibility screen 
#NOTE: Will need to update if updating renpy engine
screen choose_renderer_custom():
    layer config.interface_layer

    $ gl = False
    $ gles = False
    $ angle = False

    if renpy.android or renpy.ios or renpy.emscripten:
        $ gles = True

    elif renpy.windows:
        $ gl = True
        $ angle = True

    elif renpy.macintosh:
        $ gl = True

    elif renpy.linux:
        $ gl = True
        $ gles = True

    else:
        $ gl = True
        $ gles = True


    frame:
        style_group ""

        has side "c b":
            spacing gui._scale(10)
            xfill True
            yfill True

        fixed:

            vbox:

                xmaximum 0.48

                label _("Renderer")

                null height 10

                textbutton _("Automatically Choose"):
                    action _SetRenderer("auto")
                    style_suffix "radio_button"

                if not config.gl2:

                    if gl:
                        textbutton _("Force GL Renderer"):
                            action _SetRenderer("gl")
                            style_suffix "radio_button"

                    if angle:
                        textbutton _("Force ANGLE Renderer"):
                            action _SetRenderer("angle")
                            style_suffix "radio_button"

                    if gles:
                        textbutton _("Force GLES Renderer"):
                            action _SetRenderer("gles")
                            style_suffix "radio_button"


                if gl:
                    textbutton _("Force GL2 Renderer"):
                        action _SetRenderer("gl2")
                        style_suffix "radio_button"

                if renpy.renpy.windows:
                    textbutton _("Force ANGLE2 Renderer"):
                        action _SetRenderer("angle2")
                        style_suffix "radio_button"

                if gles:
                    textbutton _("Force GLES2 Renderer"):
                        action _SetRenderer("gles2")
                        style_suffix "radio_button"

                null height 10

                label _("Gamepad")

                null height 10

                textbutton _("Enable (No Blocklist)"):
                    action SetField(_preferences, "pad_enabled", "all")
                    style_suffix "radio_button"

                textbutton _("Enable"):
                    action SetField(_preferences, "pad_enabled", True)
                    style_suffix "radio_button"

                textbutton _("Disable"):
                    action SetField(_preferences, "pad_enabled", False)
                    style_suffix "radio_button"

                null height 10

                textbutton _("Calibrate"):
                    action ui.invokesinnewcontext(_gamepad.calibrate)
                    xfill True

            vbox:

                xmaximum 0.48
                xpos 0.5

                label _("Powersave")

                null height 10

                textbutton _("Enable"):
                    action Preference("gl powersave", True)
                    style_suffix "radio_button"

                textbutton _("Disable"):
                    action Preference("gl powersave", False)
                    style_suffix "radio_button"

                null height 10

                label _("Framerate")

                null height 10

                textbutton _("Screen"):
                    action Preference("gl framerate", None)
                    style_suffix "radio_button"

                textbutton _("60"):
                    action Preference("gl framerate", 60)
                    style_suffix "radio_button"

                textbutton _("30"):
                    action Preference("gl framerate", 30)
                    style_suffix "radio_button"

                null height 10

                label _("Tearing")

                null height 10

                textbutton _("Enable"):
                    action Preference("gl tearing", True)
                    style_suffix "radio_button"

                textbutton _("Disable"):
                    action Preference("gl tearing", False)
                    style_suffix "radio_button"

                null height 10

        vbox:

            text _("Changes will take effect the next time this program is run.") substitute True

            null height 10

            hbox:
                spacing gui._scale(25)

                textbutton _(u"Quit"):
                    action Quit(confirm=False)
                    yalign 1.0

                if not renpy.display.interface.safe_mode:
                    textbutton _("Return"):
                        action Hide("choose_renderer_custom")
                        yalign 1.0