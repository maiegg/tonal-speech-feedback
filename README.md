# Mandarin Chinese Tone Feedback

## Description 
*Use computer microphone to plot tonal varation of a spoken Mandarin sentence and compare to an instructual example* 

The goal of this project was to provide visual feedback on the pronunciation of various words or phrases by plotting changes in vocal pitch and comparing to an instructional example. Without a library of native-speaker audio examples readily available, I source pronunciation examples from the Google Translate audio API (i.e., the audio file of the computer-generated voice in the Google Translate app). Since this project had the real-life goal of helping me improve my ability to perceive and reproduce tones in spoken Mandarin*, I also include some external research indicating that my understanding of tone and frequency is indeed the right linguistic property to be exploring. 

+ One-weekend project from late 2020
+ After testing, the `googletrans` translator Python API started having [rate-limit issues](https://github.com/ssut/py-googletrans/issues/234) for me. The translation is just hard-coded in the meantime. 

*Unfortunately...no claims can be made about this project's impact on my language learning abilites! :) 

## What is "tone" anyways? 

It's pretty common knowldge that Mandarin has four "tones" that differentiate completely separate words, identical except for tonality. Tones are often described to novice learners as the "falling and rising" voice like when asking a question (rising) or making a firm statement (falling). But is there a property of speech that can somehow encode this information? And if there is, can I use that in this program to give myself feedback on my ability to speak with the intended tone?

From [Gottfried](https://www2.lawrence.edu/fast/gottfrit/Mandmusic.html), we learn that the tone is inferred from "F0" or the fundamental frequency of speech, and that studying it is possible using some simple quantitative analysis on audio waveforms: 
> Because Mandarin Chinese is a tonal language, the pitch contour **(changes in F0)** of syllables is phonemic, differentiating lexical items in the language.

So, extracting the fundamental frequency from an audio waveform should be relatively straightforward, and should tell us what we need to know about the tonality of a given word or syllable. 

Interestingly, the above link and many others in linguistics hits on the same question - why is something so easy for native speakers, so persistently hard for non-natives? 

+ Gottfried, linked above, asks if past musical training is helpful in improving non-native learners' ability to perceive pitch (they find it is, at least for some tonal patterns)
+ [This Nature paper](https://www.nature.com/articles/s41467-021-21430-x) by Li et al. even finds that there are physical brain differences between Mandarin speakers and learners that corrleate with their ability to perceive tone 
    + This was published a whole year after my weekend project, but I was encouraged to see some real linguists using plots very similar to what I produced: 
      
    ![image](https://user-images.githubusercontent.com/48812186/224505767-96b7b7c7-a73f-4ea2-9611-0771b0c864d5.png)
    
## Proof of concept / How to Use 
+ User inputs a sentence and its translation in Mandarin 
  + could also auto-generate a sentence or word or automatically retrieve translation from some API, but this is easier 
+ User executes script and triggers a listening function
+ Once user begins speaking, the function begins recording 
+ The audio file of user's speech is saved 
+ The audio file of the same sentece, but sourced from Google Translate, is retrieved
+ The F0 of these two sources is then calculated using `parselmouth` and plotted for comparison. Waveform and decibel intensity are also plotted.  

**Output for example word "ice cream:":**

![plot](https://user-images.githubusercontent.com/48812186/224507540-47eaa8c2-76d8-43d1-b9bd-64273bf03ebb.png)

## Known Issues: second draft to-do's 
+ x-axis isn't normalized for cases when user and example speak at different paces - for example, in the POC plot, I've replicated the tones pretty well, but you'd have to shift the x-axis to see the lines overlap 
+ input is hard-coded in `collect_user_speech_button_press` for now, but this will work with any Mandarin phrase and its translation 
+ after writing this, I discovered a ready-made website which does basically the same thing: https://mandarintonetrainer.com/
+ needs requirements.txt 
