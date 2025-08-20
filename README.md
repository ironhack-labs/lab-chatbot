![logo_ironhack_blue 7](https://user-images.githubusercontent.com/23629340/40541063-a07a0a8a-601a-11e8-91b5-2f13e4e6b441.png)

# Lab | Chatbot

## Getting Started

Follow the instructions provided in the notebook.

Read the instructions for each cell and provide your answers. Make sure to test your answers in each cell and save. Jupyter Notebook should automatically save your work progress. But it's a good idea to periodically save your work manually just in case.

## Deliverables

- Downloaded notebook with your responses to each of the exercises.


## Submission

- Upon completion, add your deliverables to git. 
- Then commit git and push your branch to the remote.
- Make a pull request and paste the PR link in the submission field in the Student Portal.

<br>

**Good luck!**




Report: Findings from Two Prompting Experiments

Pizza OrderBot

This version followed a structured system prompt that outlined the ordering flow (greeting, collecting order details, confirming, and processing payment). The assistant responded in a concise and conversational tone. The model handled clarifications well, such as confirming pizza size, toppings, and drinks. In some runs, the assistant also generated a structured JSON output, which was highly useful for automation since it broke the order into machine-readable components (pizzas, toppings,
drinks, sides, and total price). The only limitation I noticed was occasional formatting issues with the JSON output, such as misplaced commas.

Fantasy Coffee Shop (BaristaBot)

This second experiment replaced the real menu with a fictional one (e.g., “Galaxy Latte” and “Dragon Espresso”). The conversational flow remained smooth, and the assistant adapted to the whimsical theme easily. GPT asked clarifying questions about size, extras, and whether the order was for here or to go. The model produced convincing, friendly responses, showing its flexibility in role-playing. However, when asked for structured outputs like JSON, there were slight inconsistencies in item naming and occasional repetition. Comparison and Observations Both prompts were effective in creating engaging ordering experiences. The Pizza OrderBot was grounded and practical, while the Coffee Shop BaristaBot highlighted GPT’s creativity and adaptability. The key difference was that the pizza example demonstrated structured ordering with price calculations, whereas the coffee example emphasized style and theme over precision. Neither model struggled with the basic task of collecting orders, but structured data outputs required stricter prompting to avoid formatting issues. Lessons Learned

- Clarity matters: Clear, step-by-step instructions in the system prompt helped GPT stick to the expected flow.
- Creativity vs. precision: Creative prompts work well for engaging conversation, but accuracy suffers when real numbers or structured formats are required.
- Structured data: JSON outputs are powerful but need explicit prompting to ensure valid formatting.
- Separation of concerns: For practical applications, it may be best to let GPT handle conversation while an external system validates prices, menus, or nutrition information.

Conclusion
Both experiments demonstrated GPT’s versatility. The pizza bot showed the usefulness of
structured data, while the coffee bot showed adaptability to themed contexts. The main challenge across both examples was ensuring accuracy and consistency when structured outputs were required. 


