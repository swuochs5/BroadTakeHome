### Problem 1 Design
To filter the `/routes` data to only have subway routes, I chose to rely on the server API to handle the filtering.

As a rule of thumb, data processing is usually a task that is best served by the backend of a system. This keeps API payloads more lean, with redundant data being filtered out before it has to be sent to the client. In real-world applications, this also helps to maintain an MVC architecture where the frontend of a system can be ignorant of how data is being served to it.

However, there are situations where you might want to do tasks like filtering on the frontend. Namely, if you have a large amount of data that is all being used in separate places, you might request all necessary data upfront to reduce the number of API requests, and then filter for each individual use-case on the frontend. This was not applicable in Problem 1 due to only one API request being made regardless of where the filtering was occurring.

### Usage
This exercise can be run in Python3 with the following command in the root directory of the repo:

`python3 main.py`

It will then complete the first two problems unprompted, and then ask the user for two inputs designating the origin and destination stations for Problem 3.

The tests for this exercise can be run in Python3 with the following command in the root directory of the repo:

`python3 tests.py`
