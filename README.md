# Petr the Motivatr

## Inspiration
We were originally aiming for the Best Health Hack prize category because we discover that plenty of college students do not take proper care of their physical and mental health. And thus we came to the idea of having Petr the Anteater be Petr the Motivatr for our hackathon project. Petr the Motivator is essentially an online personal health trainer that aims to refresh the user's body and mind. 

However, we realized that we had a greater desire for our application to be funnier and more light-hearted than we imagined, so we decided to go all in on having fun with developing our application along with learning the necessary tools and services. One team member wanted to learn how to create an API and the other two wanted to learn how to do web development, so we decided to combine both into our project. Our focus for the prize category shifted to the Best Meme/Joke Hack as Petr is a hilarious figure who takes his role as the user's personal health trainer a bit too seriously.

## What it does
In our website, the user can choose from a variety of workouts to follow: the names of the workouts are UCI-building-themed, so users can click on the respective building to select a workout. Then, Petr the Motivatr will appear on screen and will start working out while matching the proper exercise displayed on screen. The user is expected to follow suit and can move onto the next exercise once the timer is up. 

When the entire workout is completed, the user will be directed to a new page that displays Petr the Motivatr giving the user a random (absurd) compliment that aims to bring a smile or laughs to the user. Therefore, Petr the Motivatr provides both physical and mental support through exercising together and giving a compliment.

## How we built it
The website is built using HTML, CSS, and Javascript and is deployed through GitHub Pages. 

The compliment that Petr the Motivatr offers is actually from a GET request made to the Absurd Compliments API that one of the team members created! The Absurd Compliments API has 3 operations (all GET): get a random compliment, get a compliment by ID, and get a compliment that matches a certain criteria. The Absurd Compliments API was originally created using FastAPI, but after running into issues with deploying it, we were recommended by a mentor to try using Flask instead. So, the Absurd Compliments API has been developed using Flask and deployed using ngrok.

## Challenges we ran into
* All of us had very litle or no experience with creating an API and with using HTML, CSS, and Javascript. So, learning and practicing all that in less than 36 hours caused many small issues, which required to look/listen to many additional resources.
* We had very specific goals in mind for what we wanted to create, so it was hard coming up with an idea that fits all the criteria:
    * Develop a Petr-themed website that calls a unique API that we create ourselves
    * The idea has to be fun, so that we can enjoy creating our application within a short timeframe
* As we have a lot of images and gifs due to using original designs (shoutout to the teammate who's a very talented artist), we kept experiencing various bugs on accesing those images and gifs. Sometimes, the files wouldn't appear on page; other times, the files weren't structured the way we styled them to be.
* As briefly mentioned before, unknown errors blocked us from deploying our Absurd Compliments API using deta, a tool that FastAPI recommended. So, after talking to a mentor, he suggested switching to Flask; after making the (thankfully) easy switch, our API has been deployed using ngrok.
* We also faced a CORS error when connecting our frontend (HTML) and backend (API deployed on ngrok) using Javascript. So, we had to use a CORS proxy to make the connection work, which took a lot of researching as this error was entirely new to us.
* Deploying our website to GitHub pages proved to be difficult as the website was not looking like the preview we saw locally. After speaking with a mentor, we realized that index.html needed to be put on the same root level as the main branch, so once we updated our code as necessary, we were able to resolve the issue and get the website to look the way we intended.

## Accomplishments that we're proud of
* Coming up with original Petr designs (specifically the gifs of Petr exercising)
* Creating a new API
* Everyone in the team now learned the basics of HTML, CSS, and Javascript from this hackathon

## What we learned
* HTML
* CSS
* Javascript
* FastAPI
* deta
* Flask
* ngrok
* Git

## What's next for Petr the Motivatr
In addition to polishing our code, we would like to add more functionality to our website such as having more user interaction and to make the transitions smoother. It would be nice to deploy the website to a new platform as we transition away from static websites. 

For the Absurd Compliments API, we want to transfer all the compliments from a hardcoded "database" to an actual external database. We also would like to deploy the API onto an actual platform that generates a permanent URL for the API and to incorporate more of the newly created API into Petr the Motivatr.