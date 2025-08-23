# Exploring Prompt Variations with ChatGPT
**Author:** <Patrik Bobcsok>  
**Date:** 2025-08-23

## Goal  
I tried different prompts with gpt-3.5-turbo to see how it changes the answers. The idea was to test if the way I write the instructions or the temperature makes the bot answer differently.

## Method  
- I made 3 versions:
  1.Friendly tutor (temp 0.7)
  2.Strict coach (temp 0.3)
  3.Italian Restaurant OrderBot (temp 0.6)
- I asked the bot and compared the replies.

## Results  
- **Friendly Tutor:** good explanations, easy to read, sometimes too general.  
- **Strict Coach:** very short and strict, maybe too robotic.  
- **OrderBot:** worked well, followed the menu correctly, no extra items.

## Observations  
- Lower temperature made the bot more serious and repeatable. 
- Higher temperature made the bot more fun but less exact.  
- The system message had a big effect (bullet points, role-play).
- I didn’t see the bot hallucinate in the OrderBot test.

## Conclusion  
I learned that the system prompt really matters. Temperature also changes the style. My favorite was the friendly tutor because it felt natural, but it's not always the best or safer solution. 
