Testing out the Thumbstick.

I found it difficult to get a nice, smooth signal from the thumbstick (which uses an ADC to get the position of the thumbstick).

First, I played around with establishing Scaling (to include flipping), and Offset.  Additionally, since I was interested in trying to code some games, I figured that I really did not need an "analog" signal and that simply knowing which direction the stick was pushed would be good enough.  So, I added a setting that would control how the output was represented.  Then, I could choose to use the analog signal, or I could have the output reduced to -1, 0, and 1.
