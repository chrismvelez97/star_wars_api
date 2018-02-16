# star_wars_api
In this little mini project, I reviewed how making API calls in python work, and how to use that data to write to json files.

First, I made a get request to the url variable, which stores the lengthy API url, and from there,
I converted the '<class 'requests.models.Response'>' into a python dictionary object using the .json() method.

After that I then converted the python object into a string, using .dumps(), after which I stored that conversion
into the variable s, for string.

Lastly, I used context manager to open my json file in write mode, and wrote the variable s into my file object.

The last couple of lines are just confirming that my program can also read from the file.

I of course want to leave a little note to myself that, every time I write to this file, it will be overwritten.

If at any point I'd like to add to the information I would have instead used the 'a' mode, otherwise known as append.
