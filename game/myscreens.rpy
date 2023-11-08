screen wiggles():
    imagebutton:
        idle "wiggles.png"
        xalign 0.3
        yalign 0.5
        action Jump("wigglewin")
screen countdown:
    timer 0.01 repeat True action If(time > 0, true=SetVariable('time', time - 0.01), false=[Hide('countdown'), Jump(timer_jump)])
    bar value time range timer_range xalign 0.5 yalign 0.9 xmaximum 300 at alpha_dissolve
