# legendary-spork
*Use computer microphone to plot pitch of speech and compare to Google Translate audio as real-time instructional feedback* 

:dumpling:   :cn:   :mega:   :hear_no_evil: 

+ Side project from late 2020
+ `googletrans` translator Python API started having [https://github.com/ssut/py-googletrans/issues/234]issues around this time. It used to be easy to fetch automatic translations, and it would be fun to use this with dynamic user inputs, but until we can reliably use this or an equivalent for translation it will be hard 

## TO-DO:
+ Wrap in a front-end (currently trying to learn some Flask) 
+ Normalize time axis of plots to correct for differences in speed of speech  
+ Explore ways to improve the pitch detection algorithm linguistically - are there features other than pitch that matter in tone/meaning perception?
+ Fill out this readme

## Background
Like many a Mandarin/Cantonese learner, with many an exasperated native-speaking significant other, I found myself often asking "what is that tone even *supposed* to sound like?!" - not to mention "that *is* how I pronounce it!" Having no background in linguistics and only sort of a grasp on Mandarin, I tried to use some recorded audio signals of my Mandarin speech and compare various features of the audio signal to examples as a way of obtaining educational feedback. I've focused on tone here, using the literal pitch (maximum-amplitude frequency) of the speech over time.

## Examples 
to-do 

## Useful links 
+ Most of the papers I had found on similar topics are around tone/character classification, e.g.: https://arxiv.org/pdf/1807.02465.pdf
+ Late in the game of writing this, I discovered a website which does basically the same thing: https://mandarintonetrainer.com/
