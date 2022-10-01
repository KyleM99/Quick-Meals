Quick Meals is a new way of getting ready to cook meals to your front door with a simple click of a button. Quick Meals goal is to help you stay on top of your fitness routine with calorie and macro specific meals to directly help you get the nutrition you need whilst also giving you the correct portion size so that you feel full after every Quick Meal!


### Project Goals
<br>
For this project I have decided to choose the Project Idea 0 and bring my own idea to life. As many companies now adays are making it easily accessible to get healthy and nutritious meals to your door, I have decided to give that a try since I currently am trying to track what I eat. So with that in mind, I know that those website's in mind have had many years in development and I am just a team of one, I still want to try build a very basic design and give it a go and see if I can add certain elements that those other companies have to offer.
<br>
My main goal for this website is for the main function of selecting a meal which would be helpful for someone who is on a strict diet or someone who would like to start taking control of their meals to find a easy solution for choosing appetising meals from a selection of options. My primary intention isnt a make a "fitness community" however a review section for each specific meal choice and perhaps a feedback section would be something that I will be aiming to create once the initial website is functional and everything works up to my standard.

### Design
My main design plan is going to be a initial website splash page with our mission statement and what Quick Meals will be able to offer to subscription members, followed up by a simple and easy navigation bar for every user to be able to find something they are looking for, whether thats what meals we offer to what other people currently think about our products. <br>
Main page layout is how I am currently liking it, and main functions to see the list of products is currently functional with only one bug that I can figure out before the project gets handed in. Not too confident on if all of the sites functionality at this point will be complete but will give it a go! <br>
I was initially planning on adding a sort by price rating etc. dropdown to the top of each page, however after further thought and seeing it in place, and with the lack of products I have for my site I have decided against this. [https://i.imgur.com/hbhvAah.png] <br>



### Bug Testing
I have had some issues with Django when attempting to access the administrator panel but both of the times I ran into that issue was when I saved my file and came back to it the following day, so since I am primarily starting this repository over from scratch I hopefully won't run into this issue further. <br>
This has been incorrect, I am still having the same issue with Django logging into admin however it should all be set up correctly, [https://i.imgur.com/P799yaK.png] <br>
I have fixed the initial bug stopping me from logging into the admin side of the website, and I also ran into another issue where once I put my admin login information into the page it threw another error about CSRF, but I have added one of the addresses from the port section into my settings.py file and it seems to have allowed me to gain access to the admin panel. <br>
Currently I'm running into an issue on the all products page where since I only have a limited amount of products and I want to use some of them only on other pages such as the sample pack or subscription deals. They are all added twice into my products.json file which is why they are coming up twice but I'm not too sure if I can hide the duplicates so I might just have to deal with it showing up twice. [https://i.imgur.com/HKdhhbQ.jpeg] <br>
Currently running into an issue where the Bolognese dish is the only one not to show up twice, however it also isnt going into its correct category page under the sample deals [https://i.imgur.com/tWV0KuH.png]. I cannot seem to get this to work, so unfortunately the "Sample Meals page will not show any items, however it should be showing the Bolognese, however after numerious attempts to change a couple id names around and even add a new product and category to the json files, it still does not want to show up. <br>
So I have fixed the issue mentioned above, where logging into the admin panel, I noticed that it wasnt updating from the json file, so I went in and updated the product to show up in the correct drop down menu. However upon trying to add a certain discount based on the page you were looking at I wasn't able to change it as it would only change over the site so I am thinking of reducing the price of the product for the entire website, so when you are looking in the all products list you can see some of them are a bit cheaper than the rest and hopefully that will make sense when you then click into the deals page and see that it is a lower cost than the rest of the meals on the website. <br>



### Development
In the future if I decide to continue developing this website I would like to get a custom domain for an easy and rememberable URL, however for the time being I will front this website with GitHub's own hosting features. I do not expect many issues with this however in the past I have ran into some issues with pictures not loading but I believe to have found a workaround so I wont fall into the same issues with this project. <br>
( In all my time looking at other peoples project's and even looking at some employment based projects from the likes of senior devs at Google, I have even asked in my readme files as to what goes into this section however I was never told.. not even during my writeup on what the project was lacking before i resubmitted, this is the only place that uses aor even asks for a development section in the readme file and since I do not know what is the main intention for this section at my final project, this is the best I believe I can do since I am still in the dark as to what this section is used for as I don't believe outside of this course it has any purpose. )

### Credits
Initial template taken from Code Institute. <br>
All of the meals and descriptions about the food has been taken from bbcgoodfood. <br>
Websites I took inspiration from : <br>
[https://www.hellofresh.com/] <br>
[https://www.dublinmeatcompany.com/index?l=en&gclid=Cj0KCQjwyt-ZBhCNARIsAKH1177kbNXozyaiPDGL6nIq3M2cAjCJS1ufZiURQjubWcFUR07LYqHb5vYaAn8HEALw_wcB] <br>
[https://cleancutmeals.ie/]<br>
