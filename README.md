# pkmn-guess
Small pokemon guessing game. Built hastily to try out Flask.

main.py shows how the guessing game should work. Loads through a few guesses and allows user to keep guessing until they either type correct pokemon names or run out of guesses.
calls.py has all calls for generating Pokemon data, which culminates in creating an object with 3 fields that is used to generate the hints and name of pokemon.
app.py will import calls.py and use the functions generated there, returning a dictionary constructed using the fields in Pokemon class.
-- to use flask here, run the command:  'python app.py'
-- the required libraries to install would be 'pip install requests',  'pip install Flask' , and 'pip install flask-cors'
-- the pokeAPI called for this does have a small amount of errors. Attempt running twice if everything looks fine and weird errors are still encountered.



once the flask server is up and running, open index.html to test out these calls. 
you enter guesses and hints should be self updating, showing more little by little
-- the corrent number of guesses is off for now, will show one last hint before dissapearing but guessing correctly/incorectly should all still work

paying attention to the terminal we can see when a proper call is executed when it prints out code 200


