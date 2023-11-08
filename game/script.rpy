define m = Character("Marie")
define r = Character("Rebecca")
define ja = Character("James")
define c = Character("Caleb")
define je = Character("Jenny")
define sa = Character("Sasha")
define se = Character("Sean")
define ju = Character("Julie")
define w = Character("???")
define o = Character("Tutorial")
define t = Character("Mr. Koro")
define tv = Character("Tv")
define music.rebecca = "rebecca.mp3"
define music.james = "james.mp3"
define music.marie = "marie.mp3"

init:
    $ timer_range = 0
    $ timer_jump = 0
transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0

transform cen:
    xalign 0.5
    yalign 1.0

transform ls:
    xalign 0.0
    yalign 1.0
transform rs:
    xalign 1.0
    yalign 1.0
transform lcen:
    xalign 0.3
    yalign 1.0
transform rcen:
    xalign 0.6
    yalign 1.0

label start:
    play music rebecca
    "ring!"
    w "Hey!"
    w "Rebecca wake up! Class ended like HOURS ago."
    r "wha-? What's going on?"
    scene classroom with fade
    show julie sad at rs
    r "It's Julie my best friend in all her super spooky glory"
    r "She looks worried. I wonder what's wrong."
    ju "Finally you're up! I need your help! Please!"
    r "Alright, alright what is it?"
    show rebecca suprise at ls
    ju "It's Mr.wiggles I lost him at recess and now he's lost forever!"
    r "Julie, take a couple of breaths. He's not lost forever and we've got plenty of time to look before the busses get to school."
    ju "*sigh* I guess…"
    show julie thinking at rs
    r "Let's get going then!"
    ju "Mr.Wiggles here we come!"
    scene black with fade
    o "Hey there, I'm Tutorial!"
    o "Sit tight cause I'm gonna teach you how to properly play this game here~"
    o "Hidden somewhere in the schoolyard is Julies toy Mr.Wiggles."
    o "Once you spot him just give him a click and the game will end!"
    o "Don't take too long though… the buses are coming."
    o "That's all for now! See ya~"
    scene schoolyard with fade
    show rebecca neutral at ls
    r "Well now that we're out here…"
    r "Do you know where you left him?"
    ju "Well I don't know exactly but I was picking flowers near the grass over there."
    show julie sad at rs
    ju "Don't get the wrong idea or anything! It was Mr.Wiggle's idea, I hated every second of it."
    show rebecca happy at ls
    r "Ok, sure Julie"
    label wigglestart:
        $ time = 5
        $ timer_range = 5
        $ timer_jump = "wiggleloss"
        show screen countdown
        call screen wiggles
    label wigglewin:
        hide screen countdown
        r "I've got him!"
        show rebecca happy at ls
        ju "YES! Thanks so much, Rebecca I don't know what I'd do without you."
        show julie happy at rs
        r "I got him right on time too, here come the buses."
        ju "Bye, Becca!"
        r "Bye, Julie!"
        jump wiggleend
    label wiggleloss:
        r "I couldn't find him, Julie"
        show rebecca sad at ls
        ju "…"
        show julie sad at rs
        r "I'm sorry"
        ju "…"
        scene black with fade
        o "Well… that could have gone better"
        o "Normally I wouldn't do this but since it's your first time… "
        o "Why don't you try that again"
        with fade
        o "Have fun~"
        jump wigglestart
    label wiggleend:
    stop music
    scene policestation with fade
    play music james
    show james frustrated at ls
    w "Here I am again, waiting for that peppy little newby girl."
    w "I swear every day she redefines what it means to be late…"
    "*Bang!*"
    w "James! James! James!"
    show sasha happy at rs
    ja "Here she comes and there goes my peace and quiet."
    ja "Hey Sasha."
    sa "Hey, Hey! I am SOOoooo sorry I'm late."
    ja "Let me guess, the train was late, your toaster exploded and you missed your stop."
    sa "Well… actually my microwave blew up this time."
    ja "We don't have time for this Sarah get in the car."
    sa "It's Sasha."
    ja "Ok Sokka."
    sa "I-"
    ja "We're on parking duty today because you were late again."
    ja "At this rate, I'll never do anything interesting again."
    sa "Sorry bossman it won't happen again."
    show sasha attention at rs
    ja "I told you to lay off the nickname Sandbag."
    sa "Sa-Sha."
    show james happy at ls
    ja "Whatever."
    scene outside with fade
    show sasha happy at rs
    sa "Well…"
    sa "shifts over and we don't have much to show for it."
    sa "you sure you know how this stuff works James?"
    show james frustrated at ls
    ja "What's that supposed to mean Small-fry!"
    sa "Nothing Bossman- Uh James."
    show sasha attention at rs
    ja "We're leaving."
    sa "Holy Moly, what a temper."
    scene policestation with fade
    show sasha happy at rs
    sa "Andddd my paperwork is all wrapped up!"
    show james happy at ls
    ja "Same here Sushi"
    sa "Ignoring that… you wanna hit up the bar bossman"
    ja "Sure why not"
    sa "Don't be like that I know you have the most fun out of all of us."
    sa "Even if you are a lightweight."
    show james frustrated at ls
    ja "You wanna say that again!?"
    sa "No, No I do not"
    stop music
    scene cafe with fade
    play music rebecca
    show rebecca happy at ls
    r "So if I move the one down and two times seven is fourteen then the answer is-"
    w "Hey Rebecca back onto the homework again I see."
    show caleb working at rs
    r "Well that's what I was doing."
    show rebecca angry at ls
    w "Sorry, Sorry! I just wanted to take your order."
    show rebecca happy at ls
    r "It's fine Caleb"
    r "Anyways"
    r "One rose-red wonder drink with extra whipped cream and marshmallows, please!"
    c "Sometimes I wonder how your teeth say in your mouth with all the sugar in that drink."
    show caleb happy at rs
    r "Hey it's what I want so it's what I'm going to get."
    c "If you say so."
    c "Marie! One rose red with extra cream and mallows for the kid"
    m "Coming right up."
    r "All right! back to my old enemy."
    r "Homework."
    with fade
    hide caleb happy
    show marie happy at cen
    m "Here's your order Becca."
    show rebecca happy at ls
    r "Thanks."
    m "How is the work going?"
    r "Well I'm doing good with everything but the last questions."
    show rebecca neutral at ls
    m "You've just got to multiply those numbers, honey."
    r "Wait, wait what about those ones."
    m "You just ignore those cause they're outside the brackets."
    m "Just remember your PEMDAS and you'll be alright."
    r "Thanks"
    show rebecca happy at ls
    r "She seems so happy today. She's been even gloomier than usual recently."
    with fade
    r "Oh! It's five Oclock already, I gotta go!"
    r "Bye guys see you soon!"
    show marie working at rs
    m "See you later!"
    scene rebeccahouse with fade
    je "Becca's how was school?"
    show jenny at rs
    r "It was great, only one complaint from Mr. Koro today."
    show rebecca happy at ls
    je "That's awesome you really are my superstar."
    show sean happy at cen
    se "Good job squirt."
    r "Also, Also I helped Julie find Mr.Wiggles again."
    je "It's good that you helped her but she has to put a leash on him or something."
    r "That's a pretty good idea but I think she'd still find a way to lose him."
    scene black
    stop music
    with fade
    play music marie
    "crash!"
    w "Dad I know you do your best for me but coming home sober once and a while wouldn't hurt."
    w "Shudup girl I'm fine like this."
    w "But-"
    "*slap*"
    w "Why'r you still talkin when' dinner ain't made"
    w "Yes sir…"
    w "thas better."
    scene mariahouse with fade
    stop music
    show james drunk at ls
    play music james
    ja "Oh god my head is pounding."
    ja "Damn hangovers."
    ja "I hope breakfast is ready…"
    ja "I'm going to be late if I don't get going now."
    scene policestation with fade
    label murderstart:
        scene policestation
        ja "It's quiet. What's going on?"
        show james neutral at ls
        sa "Hey James Pssst James!"
        show sasha neutral at rs
        ja "Your being quiet. Is something wrong?"
        ja "Have I died and gone to heaven?"
        show james happy at ls
        sa "Very funny bossman but now's not the time"
        ja "Spit it out newby what happened"
        show james neutral at ls
        sa "There's been a murder I need you to figure this stuff out."
        sa "I'm totally stumped"
        show james frustrated at ls
        ja "Why didn't you say that FIRST!"
        sa "Oops sorry."
        ja "Welp, let's hear it, Sarah."
        sa "First of all it's Sasha I know you know my name"
        ja "Get on with it."
        show james neutral at ls
        sa "Ok! So there are three suspects."
        sa "The victim was found in her living room surrounded by clears signs of a struggle"
        sa "The autopsy shows that she was beaten to death using a blunt object at around midnight."
        sa "The victim was"
        with fade
        show sasha neutral at rs
        sa "and multiple"
        with fade
        show sasha neutral at rs
        sa "were made but never looked into"
        sa "So the first suspect is the neighbour who is known to dislike the victim's family. He doesn't have an alibi for midnight but he claims to have been sleeping. He has to key to the house so he could have gotten in if he wanted to. The interrogation team says that he looked suspicious in questioning."
        sa "The second suspect was walking by the property and claims to have heard loud noises from inside the house that where he found the victim's father crying over the body. His fingerprints were found on the victim but I don't really think that he did it."
        ja "Less opinions more facts Serena."
        show james frustrated at ls
        sa "You KNOW my name damn it."
        ja "Murder case get back to it."
        sa "Ok, Ok, the third and last suspect is the victim's father he was found crying over his daughter's body. His fingerprints were on the victim but he says that he only touched her after the murder because of shock. While he had the opportunity there does not seem to be a motive."
        sa "So what do you think bossman?"
        scene black with fade
        o "Heyo! Me again!"
        o "This game's a little harder than the others."
        o "What you're gonna do is pick the suspect who you think is the murder."
        o "To do this click on the 'select' option then pick your suspect."
        o "If you need to hear something over again then pick on the information you want repeated."
        o "Work quickly though you're on a timer~"
        o "Why you ask?"
        o "Cause I said so silly!"
        scene policestation
        $ time = 10
        $ timer_range = 10
        $ timer_jump = "murdertime"
        show screen countdown
    menu:
        "The neighboor":
            jump murderwin
        "The father":
            jump murderof
        "The passerby":
            jump murderciv
    label murderwin:
        hide screen countdown
        show sasha happy at rs
        sa "Alright James! We got it."
        show james happy at ls
        ja "You mean I got it."
        sa "Yeah, yeah whatever."
        jump murderend
    label murderciv:
        hide screen countdown
        show sasha neutral
        sa "Really James."
        sa "I mean it's possible but where's the motive."
        sa "We're missing something take a look at it again."
        jump murderstart
    label murderof:
        hide screen countdown
        show sasha neutral at rs
        sa "James you can't be serious."
        sa "That's"
        with fade
        sa "Even with"
        with fade
        sa "He's a grieving father"
        sa "Try again bossman…"
        jump murderstart
    label murdertime:
        hide screen countdown
        scene black with fade
        o "Well not sure how when the answer was in front of you but you failed."
        o "Sorry but I'm gonna have to give you a game over."
        o "Try again sweetie~"
        jump murderstart
    label murderend:
        sa "Good job bossman…"
        ja "Listen squirt it's all in a day's work."
    stop music
    scene classroom with fade
    play music rebecca
    r "You know what Julie?"
    show rebecca neutral at ls
    ju "What is it?"
    show julie thinking at rs
    r "It's Marie"
    ju "That barista at Rose cafe?"
    r "Yes! Her!"
    r "She's always so gloomy! I'm sure something is wrong!"
    show rebecca sad at ls
    ju "This again, she's always been like this, it's nothing to worry about."
    show julie sad at rs
    ju "But if you're that worried about her we can swoop in after school and save her from whatever evil villain is bothering her."
    r "It's not a game Julie!!!"
    show rebecca angry at ls
    ju "Sorry Becca but I just don't think there's anything wrong with her."
    r "Alright…"
    ju "*sigh*"
    r "I'm still going to Rose after school though!!"
    show rebecca happy at ls
    ju "Your parents are gonna stop giving you an allowance if you keep spending it all at the same place!"
    show julie happy at rs
    r "Maybe…"
    r "But that hasn't happened yet so it can't stop me."
    ju "If it works for you I guess."
    scene cafe
    with fade
    m "Ow! Ow!"
    show marie crying at rs
    c "What's wrong!"
    show caleb worried at cen
    m "I hit my head on my desk yesterday."
    show marie fake happy at rs
    m "I was trying to grab my pen but you know me…"
    m "Clumsy Marie… heh."
    show caleb sad at cen
    c "Alright… be more careful for me, please."
    m "Sure."
    with fade
    show rebecca happy at ls
    show marie fake happy at rs
    r "Hey guys!"
    m "Hello."
    show marie fake happy at rs
    c "How was school kid."
    show caleb happy at cen
    r "Great! No homework today too!"
    hide caleb happy at cen
    m "That's nice."
    m "Can I get your order."
    show marie working at rs
    r "You know it already."
    show rebecca suprise at ls
    m "Oh. Yeah-"
    show marie fake happy at rs
    c "One rose red with extra cream and mallows coming right up for you Becca!"
    show caleb working at cen
    with fade
    hide marie fake happy
    r "Thanks for the drink!"
    show rebecca happy at ls
    c "You're welcome."
    show caleb working at rs
    c "…"
    show caleb worried at rs
    c "Sorry about Marie, she's been acting odd all day."
    c "I think she stayed up too late yesterday or something."
    show rebecca sad at ls
    r "Well it's fine I don't mind…"
    c "…"
    r "Really… It's fine."
    stop music
    scene bar with fade
    play music james
    ja "Godammit!"
    show james frustrated at ls
    sa "Dang!"
    show sasha neutral at rs
    ja "Day's over and all we've done is let criminals getaway!"
    sa "Plus those damn kids wouldn't stop mocking us!"
    ja "Stupid brats! I need a damn drink after that!"
    sa "I hear ya bossman."
    ja "Come on."
    scene bar with fade
    sa "They were all like hey piggies."
    show james frustrated at ls
    ja "Those damn kids get so angry over nothing."
    sa "Heh yeah…"
    show sasha drunk at rs
    with fade
    show james sad at ls
    ja "Then' my damn  wife l-leaves me wit' the kid."
    with fade
    show james sad at ls
    ja "*Sob* I just miss her so bad. *hic*"
    with fade
    show james drunk at ls
    ja "Ey' complainin' so much bout mah work*hic*"
    ja "Wha's ey gon' do bout' it then! Nothing!"
    ja "Bunch of *hic* damn *hic* yahoos."
    show sasha drunk at rs
    sa "Yer righto bossman. *hic*"
    with fade
    show james neutral at ls
    ja "gotta go Sasha"
    ja "Someone's waitin' for me at home."
    stop music
    scene black
    with fade
    play music marie
    w "EY!?."
    w "Why ain't dinner ready."
    w "Dad it's 2 am."
    w "Did I' ask?"
    w "I work every fuken day"
    w "Just fer you ta not do wha- I ask"
    w "Dad, please!"
    "*slap*"
    w "Ever since yer mom died ya'v been nothin' but a burden."
    w "Wha- ave' you ever done fer me!"
    w "Nothing, Huh?"
    w "Please, please, please!"
    w "Don't talk back damn it!"
    w "Maybe I should just get rid of you."
    w "Obviously you're worthless"
    w "Right?"
    w "…"
    w "Right! Say it!"
    w "… I-I-I'm worthless."
    w "Say it, girl!"
    w "I'm worthless."
    w "That's better."
    w "I've still got to punish you though"
    w "You know I hate doing this but you still force me to every time."
    w "I know sir."
    w "If you fuken knew…"
    w "You wouldn't have messed it up…"
    "*bang*"
    stop music
    scene mariahouse with fade
    play music james
    show james frustrated at cen
    ja "Headache… again"
    ja "Whatever it doesn't matter as long as breakfast is ready I don't care"
    ja "News is on…"
    ja "These eggs aren't bad"
    ja "That's good after those recent failures"
    tv "Breaking News!"
    tv "Riots have broken out on Mainstreet after the supposed false arrest of Kyan Gray for the killing of Lila Evans"
    ja "I've gotta get going they're gonna need me at the station!"
    scene policestation with fade
    sa "James you're here!"
    sa "It's horrible. Remember that murder from a few days ago"
    ja "Yeah…"

    with fade
    sa "There's been a murder I need you to figure this stuff out."
    sa "I'm totally stumped"
    show james frustrated at ls
    ja "Why didn't you say that FIRST!"
    sa "Oops sorry."
    ja "Welp, let's hear it, Sarah."
    sa "First of all it's Sasha I know you know my name"
    ja "Get on with it."
    show james neutral at ls
    sa "Ok! So there are three suspects."
    sa "The victim was found in her living room surrounded by clears signs of a struggle"
    sa "The autopsy shows that she was beaten to death using a blunt object at around midnight."
    sa "The victim was officer Arnolds daughter"
    show sasha neutral at rs
    sa "and multiple domestic abuse calls were made but never looked into"
    sa ""
    sa "So the first suspect is the neighbour who is known to dislike the victim's family. He doesn't have an alibi for midnight but he claims to have been sleeping. He has to key to the house so he could have gotten in if he wanted to. The interrogation team says that he looked suspicious in questioning."
    sa "The second suspect was walking by the property and claims to have heard loud noises from inside the house that where he found the victim's father crying over the body. His fingerprints were found on the victim but I don't really think that he did it."
    show james frustrated at ls
    ja "Less opinions more facts Serena."
    sa "You KNOW my name damn it."
    ja "Murder case get back to it."
    sa "Ok, Ok, the third and last suspect is the victim's father he was found crying over his daughter's body. His fingerprints were on the victim but he says that he only touched her after the murder because of shock. While he had the opportunity there does not seem to be a motive."
    sa "So what do you think bossman?"
    "flashback end"
    with fade

    show sasha neutral at rs
    sa "People are saying we got the wrong guy"
    sa "there saying it was officer Arnold"
    show james neutral at ls
    ja "Don't be doubting the choice we made newby"
    ja "We made the right choice"
    show james happy at ls
    sa "Yeah sure…"
    sa "By the way…"
    ja "What."
    sa "I've got some bad news."
    ja "Spit it out Newbs"
    sa "We're on protest duty."
    show james frustrated at ls
    ja "Oh Joy of Joy's"
    stop music
    scene classroom with fade
    show rebecca sad at ls
    play music rebecca
    r "Marie was acting odd yesterday"
    show julie thinking at rs
    ju "This again."
    r "Seriously, she was super weird."
    show rebecca suprise at ls
    ju "Really?"
    r "She asked me for my order!!!"
    ju "That IS weird."
    t "Rebecca and Julie, do I need to separate you or will you be alright."
    show rebecca sad at ls
    r "Sorry Mr. Koro."
    t "This is your second warning Rebecca anymore and you'll be penalized."
    r "Yes sir…"
    scene schoolyard
    with fade
    "*RING*"
    show julie happy at rs
    ju "Oh yeah! Schools over!"
    show rebecca happy at ls
    r "I'm gonna head over to Rose again today."
    ju "Two days in a row!?"
    r "I've got to check on Marie."
    show julie sad at rs
    ju "Alright…"
    show julie happy at rs
    ju "Have fun!"
    scene cafe
    with fade
    show caleb worried at rs
    c "You sure you don't wanna take the day off Marie"
    show marie fake happy at ls
    m "I'm fine."
    c "Alright but don't be afraid to take the day off if you need it."
    show marie defiant at ls
    m "I'm. Fine"
    c "Alright. Alright, I got it."
    show caleb sad at rs
    with fade
    r "Hey guys!"
    show rebecca happy at cen
    c "Rebecca you're here"
    show caleb working at rs
    r "Yup!"
    c "So the usual"
    r "Yup again!"
    c "Marie it's usual for Becca."
    m "Got it."
    show marie working at ls
    with fade
    show marie working rs
    hide caleb working
    m "Here you go… honey."
    show rebecca neutral at ls
    r "Are you ok Marie?"
    show marie fake happy at rs
    m "I'm good, really."
    r "I'm not sure about that Marie"
    r "You're shaking"
    m "What?! No! I'm just a bit cold."
    r "You know you can tell me."
    r "My lips are sealed and everythin-"
    show rebecca suprise at ls
    r "Is that blood!?"
    show marie blood at rs
    m "What! No! I- I- I just spilled some of your drink while I was making it."
    m "Sorry to worry you."
    with fade
    hide rebecca surprise
    m "It's getting late…"
    show marie fake happy at ls
    m "I'm gonna turn in early if it's ok with you Caleb."
    show caleb working at rs
    c "Sure! I'm all good here!"
    hide marie fake happy
    m "See you guys later."
    show rebecca neutral at ls
    r "Caleb! Somethings wrong with her!"
    show caleb worried at rs
    c "I know. I know but she won't tell me anything."
    show rebecca sad at ls with vpunch
    r "No! I mean really, really wrong!"
    r "I saw blood! She said it was my drink but I know she was lying!"
    show caleb sad at rs
    c "What!"
    r "Caleb something's happening to her."
    show caleb worried at rs
    c "I know, I know but what is it and how do we find out."
    show rebecca neutral at ls
    r "We'll follow her!"
    c "What No! It could be dangerous."
    show rebecca angry at ls
    r "I'm going alone if you don't come with me."
    c "Rebecca…"
    r "…"
    r "Please."
    c "… fine but if things start going wrong we leave."
    r "Alright."

    with fade
    scene outsidenight
    with fade
    show caleb worried at rs
    c "Where is she going?"
    show rebecca suprise at ls
    r "Quiet dummy she'll hear us."
    c "Sorry."
    show rebecca neutral at ls
    r "Shhhhh."
    c "She's going into that one."
    r "Let's get a little closer."
    stop music
    scene outsidemariahouse with fade
    play music marie
    w "Yer late girl."
    m "Sorry dad."
    w "I've ad' a horrible day ya know tha'."
    w "Damn Protestahs yellin' in mah *hic* face all day."
    w "And then you! I've gotta' come ome' to yer sorry ass every day."
    w "Peice o' crap."
    m "I'm sorr-"
    w "I don' wanna hear it."
    w "It's yer fault yer mother died ya know tha'."
    w "It's all *slap* yer *slap* fault"
    m "Dad!"
    w "You think I care anymore girl!!!"
    w "Every day you find some new way to disappoint."
    w "I'll give ya a day but yer dead tomorrow."
    "*crash*"
    m "AHHHH!"
    m "Dad! Stop! No!"
    with fade
    show caleb sad at rs
    c "What the heck"
    show rebecca neutral
    r "…"
    c "Get it together Caleb."
    c "What do you do now?"
    r "…"
    show caleb worried
    c "Get help."
    c "911 that's it."
    "*ring*"
    "*ring*"
    c "Come on pick-up, pick-up!"
    "Hello?"
    c "Hello! I'm calling for domestic violence."
    "Ok, and where are you right now?"
    "*crash*"
    c "We're on the corner of airam and semaj."
    "Thank you."
    "Please sit tight and the authorities will be there in 5-10 minutes."
    c "Ok."
    show caleb sad at rs
    c "Just five more minutes Rebecca she'll be ok."
    r "…"
    c "Sit tight ok."
    with fade
    show rebecca sad at ls
    r "They're here."
    show caleb happy at rs
    c "See everything will be fine."
    show sasha neutral at cen
    sa "Is this the domestic abuse call."
    c "Yes Mam."
    show sasha attention at cen
    sa "Please wait outside, I will handle the situation."
    "*knock, knock*"
    scene mariahouse with fade
    show sasha neutral at cen
    sa "I'm coming in on suspicion of domestic violence!"
    sa "Sir! You are under arrest please put you-"
    show sasha happy at cen
    sa "Wait James?"
    sa "What are you doing here?"
    show james frustrated at rs
    ja "I live here."
    sa "I must have the wrong house then."
    sa "Some kids outside made a domestic violence call."
    show james drunk at rs
    ja "You guys have definitely *hic* got the wrong house."
    ja "My daughter here is doing fine. *hic*"
    show marie crying at ls
    m "…"
    show james frustrated at rs
    ja "Right Marie?"
    show marie blood at ls
    m "Yes dad…"
    sa "Anyway's how ya doing James"
    ja "I'm good. Busy though *hic*."
    show sasha neutral
    sa "People are really coming after you for that murder case huh."
    show james sad at rs
    ja "Oh- well *hic* yeah I-I guess"
    sa "Well anyways gotta get back to work."
    show sasha attention at cen
    sa "See you at the office, James."
    ja "Yeah *hic* Bye."
    scene outsidemariahouse with fade
    show sasha happy at cen
    sa "It was a false alarm kids."
    show caleb sad at rs
    c "…"
    sa "I'll be taking my leave now."
    show sasha attention at cen
    sa "Stay out of trouble."
    show rebecca sad at ls
    r "…"
    c "…"
    with fade
    show caleb worried at rs
    c "We should get going Rebecca"
    show rebecca sad at ls
    r "Sure."
    stop music
    scene rebeccahouse with fade
    play music rebecca
    show sean sad at rs
    se "Rebecca! Where were you young lady!"
    show jenny at cen
    je "It's alright to stay out late but you have to tell us these things."
    se "Oh we were so worried."
    show rebecca sad at ls
    r "Sorry Mom and Dad."
    je "You alright you seem sad."
    r "I had a bad day today."
    r "Can I go to bed?"
    je "Sure sweetie just make sure to talk to someone about it at some point."
    se "It's bad to keep these things to yourself."
    r "You got it…"
    r "Goodnight."
    stop music
    scene mariahouse with fade
    play music james
    show james frustrated at ls
    ja "God Damn what a night."
    ja "Stupid girl and her friends called the cops on ME."
    ja "Thought I had gotten that out of her years ago."
    ja "Gotta get to the station early today."
    ja "Protesting imbeciles are gonna ruin my day again!"
    ja "Time for another day of dealing with wonderful Sasha."
    scene policestation with fade
    show sasha happy at rs
    sa "James!"
    show james happy at ls
    ja "Hey newby."
    show sasha neutral at rs
    sa "So sadly we are on protest duty…"
    sa "Again"
    show james frustrated at ls
    ja "Well then… Let's go."
    stop music
    scene classroom with fade
    play music rebecca
    show rebecca sad at ls
    r "And that's what happened last night."
    show julie sad at rs
    ju "Oh my god Becca."
    r "I know."
    ju "What are you gonna do next?"
    r "I'm not sure but I think I'll go to Rose after school to talk with Caleb."
    ju "Alright Rebecca, that's a decent plan."
    ju "Be careful though."
    show rebecca neutral at ls
    r "I will."
    scene cafe with fade
    play music marie
    show caleb worried at rs
    c "Rebecca!"
    c "Finally, you're here!"
    show rebecca sad at ls
    r "Caleb! What are we gonna do?"
    r "If we don't help…"
    r "It's our last chance"
    show caleb sad at rs
    c "Calm down Becca. I've got a plan to help Marie."
    c "So what we're gonna do is"
    with fade
    show caleb sad at rs
    c "She's going to be on guard today though so follow my lead."
    show rebecca happy at ls
    r "I'll do my best Caleb!"
    show marie fake happy
    m "Hey! Guys what going on over there!"
    show caleb worried at rs
    c "Nothing much."
    r "I was talking to caleb about…"
    c "Her homework!"
    r "Yes… homework."
    show marie defiant at cen
    m "… Sure."
    show marie happy at cen
    m "Anyways, I'm guessing you want the usual."
    r "Yup!"
    with fade
    show marie fake happy at cen
    m "I'm heading out early today!"
    m "Bye!"
    hide marie fake happy
    with fade
    show caleb happy at rs
    c "Rebecca, it's go time"
    show rebecca happy at ls
    r "Alright."
    scene outsidemariahouse with fade
    show rebecca neutral at ls
    show caleb neutral at rs
    c "Looks like we got here before Marie's dad"
    r "Good."
    r "I think this is gonna work."
    c "It will."
    c "It has to for Marie's sake."
    show rebecca sad at ls
    r "Quiet Caleb, t-there he is."
    hide rebecca sad
    hide caleb neutral
    with fade
    stop music
    play music james
    show james furious at ls
    ja "That daughter of mine better be ready"
    show james neutral at ls
    ja "…"
    ja "After all, it's her last day on earth"
    scene mariahouse with fade
    show james frustrated at ls
    ja "Marie! Marie! Get down here!"
    show marie crying at rs
    m "C-coming dad."
    show james happy at ls
    ja "Good."
    show marie fake happy at rs
    m "h-how was work."
    show james frustrated at ls
    show marie crying at rs
    ja "Shut up!"
    show james furious at ls
    ja "Put your hands up and don't move."
    ja "I've had a bad day and I'm not in the mood for your crying."
    ja "I'm finally going to put you out of your misery"
    show marie fake happy at rs
    m "Ok, dad."
    show james happy at ls
    ja "Good, good."
    show james furious at ls
    ja "Now to end it once and for-"
    show rebecca angry at lcen
    r "I can't let you do that!"
    c "Rebecca wait!"
    ja "If it isn't the brats who called 911 on me."
    show rebecca neutral at lcen
    r "I'm going to stop you!"
    show james neutral at ls
    ja "Oh really."
    ja "You're nothing by yourself and the police are on my side."
    show caleb neutral at rcen
    c "She's not alone."
    show james happy at ls
    ja "Oh no~"
    ja "Two brats."
    ja "What am I to do."
    c "What you're going to do is put down the gun."
    show james frustrated at ls
    ja "And why would I do that?"
    c "Unless you would like to commit first degree murder on live in front of about…"
    c "2000 viewers"
    show james sad at ls
    ja "What?"
    c "You heard me."
    ja "y-You can't do that."
    show caleb happy at rcen
    c "I can and I will."
    c "Now. What your going to do is put down the gun, and let me, Marie and Becca walk right out of here"
    show james frustrated at ls
    ja "You want me to do WHAT?!"
    show james furious at ls
    ja "Marie IS MY DAUGHTER"
    ja "I've provided for that dirty wretch every day since her mom died and she has done NOTHING in return."
    ja "What right do YOU have to stop me taking something for myself"
    show rebecca angry at lcen with vpunch
    r "You're a horrible person! You were going to kill her."
    show james neutral at ls
    ja "Marie! I'm your dad! Tell them!"
    show marie crying at rs
    m "..."
    m "..."
    show marie defiant at rs
    m "I can't dad."
    ja "Marie…"
    show james sad at ls
    ja "You…"
    ja "I can't believe it."
    show marie crying at rs
    m "Please, just stop you'll make things worse"
    ja "Marie"
    ja "My baby, please if I'm such a horrible person…"
    stop music
    ja "Just shoot me."
    show james frustrated at ls
    ja "Do, it"
    show james furious at ls with vpunch
    ja "SHOOT ME!"
    show marie crying at rs
    m "I-"
    m "Dad please stop it!"
    ja "DO IT!"
    ja "You must hate me so why not."
    ja "Shoot me."
    play music marie
    menu:
        "Shoot him":
            with fade
            show marie defiant at rs
            m "I might do it you know."
            m "After everything you've done."
            m "Don't I deserve it James."
            show caleb worried at rcen
            c "Marie, don't! He's not worth it."
            m "For once in my life I'd be able to give you what you want."
            "*bang!*"
            show james neutral at ls
            ja "…"
            ja "You missed."
            show james sad at ls
            m "I couldn't become like you."
            m "I am nothing like you and I never will be"
            m "I don't want to hear from you ever again"
            jump shootingend
        "Don't Shoot":
            with fade
            show marie crying at rs
            m "I can't."
            m "I won't become like you."
            show marie defiant at rs
            m "I-I'm leaving. Don't follow me or try to talk to me again"
            show james sad at ls
            ja "Baby please you know I didn't mean t-"
            m "It's over."
            m "Goodbye."
            jump shootingend
    label shootingend:
    hide james sad with fade
    show caleb neutral at cen
    c "Let's go guys."
    c "…"
    c "We've got a lot to figure out."
    show rebecca sad at ls
    r "Alright…"
    show marie fake happy at rs
    m "…"
    stop music
    scene rebeccahouse
    play music rebecca
    with fade
    show rebecca neutral at ls
    r "Mom, dad I'm home!"
    show jenny at cen
    je "Honey there you are!"
    hide jenny
    show sean sad at cen
    se "Why are you home so late?"
    hide sean sad
    show jenny at cen
    je "We were so worried about you!"
    show rebecca sad at ls
    r "I'm sorry… I had to help Marie!"
    je "The barista at that Cafe??"
    r "I really couldn't just stand by and watch!"
    hide jenny
    show sean sad at cen
    se "Honey slow down and explain…"
    show rebecca neutral
    r "Alright I'll start from the start…"
    hide rebecca neutral with fade
    show marie happy at ls
    m "I am so sorry for the bother…"
    m "I have money, if you don't want me here i'll find somewhere to go…"
    show jenny at rs
    je "Oh, sweetheart we would never do that to someone in need."
    show sean happy at cen
    se "Feel free to stay as long as you want."
    m "Thank you… so much."
    m "Now I just have to get back on my feet and I'll be set."
    je "Don't think you'll be doing that alone."
    je "We'll be with you the whole time."
    m "Thanks…"
    stop music
    scene black
    play music marie
    with fade
    "In the end, the video that Caleb took went viral and the police force couldn't keep James employed."
    "The protesters fought hard and solutions were found to fix the corrupt police force."
    "Marie ended up getting a restraining order and profesional to deal with her trauma through therapy."
    "She went on to become a psycaitrist to help people like her in their times of need."
    show marie blood at cen
    "Girls and Women like Marie are overwhelmingly common and the police force does not take their cases seriously enough."
    "Reach out to people who you think are in need. Don't just be a bystander."
    hide marie blood
    label credits:
        $ credits_speed = 25
        show credits_image at Move((0.5, 1.0), (0.5, -1.0), credits_speed,
                      xanchor=0.5, yanchor=0)
        with Pause(credits_speed+10)
    return
