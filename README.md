# CPSC-452-Final-Project
In this project you are to implement a system which enables a group of users to chat securely.
All users are registered with the chat server. When the user wants to chat with another reg-
istered user, he first connects to the chat server and enters his/her user name and password.<br>
The server verifies the user name and password, and if correct, the user’s status is changed to
“online“. Next, the user may enter the user ids of users with whom he wishes to chat (could be
more then one). At any given time the user should be able to check what other users are online
and invite them to the ongoing conversation. <br>
Once the user specifies the users with whom he wishes to chat, the server generates a symmetric
key, and securely distributes it to all the specified users and the user who initiated the chat. To
achieve secure key distribution you must encrypt the symmetric key using the public keys of the
respective users (you may assume that server knows the public keys of all users). If one of the
specified users is not online, the requesting user is notified about this. <br>
After the encrypted symmetric key has been distributed to all users, the users decrypt the sym-
metric key using their private keys, and the chat session may begin. All messages exchanged
during the chat must be encrypted using the symmetric key provided by the server and must be
delivered to all users participating in the chat. Any user may choose to leave the conversation. <br>
If the user disconnects from the chat server, his status should be changed to “offline“. All users
who are connected to the server, must have a way to check whether a given user is online. <br>
### Language Used: Python
## Team Members
* Coleman Nugent: colemannugent@csu.fullerton.edu
* Christopher Bos: cbos95@csu.fullerton.edu
* Cameron Mathos: cmathos@csu.fullerton.edu
* Adam Shirley: bsa919adam@csu.fullerton.edu
* Randy Le: randy.l5933@csu.fullerton.edu

## Usage

## Extra Credit
No extra credit was done for this assignment.

## Additional Notes
Nothing special to note.
