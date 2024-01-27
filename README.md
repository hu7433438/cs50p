# Chat Room
#### Video Demo:  https://youtu.be/QVDurl3Kr6I
#### Description:
This is a sample chat room program developed in Python. You can chat with others in a room you specify or create.  
* server.py is the chat room server file, before chatting you should run it.
  * Server.py contains the main, start, handle_chat, disconnect, and sent_msg methods.
  * The start method starts the asynchronous server listening for user connections.
  * The handle_chat method handles messages sent by the user.
  * The disconnect method is used to remove the user
  * The sent_msg method is used to send a message to the user.
* project.py is the chat room client file.
  * project.py contains the main, send_forever, recv_forever, send_need_code0, send_and_recv, recv_msg, and send_msg methods.
  * The send_forever method keeps asking you to type in a chat message and send the message.
  * The recv_forever method keeps receiving message from the server.
  * The send_need_code0 method requires that the code in the message received after sending a message to the server be equal to 0. Otherwise, it keeps asking for input.
  * The send_and_recv method is used to send a message and receive a message right now.
  * The recv_msg method is used to receive a message.
  * The send_msg method is used to send a message.
* utils.py is a collection of methods common to both client and server.
* enums.py is a collection of values common to both client and server.
#### How to use
* Server:
  * Before running server.py, you should change HOST to server IP and PORT to a free port in enums.py.
* Client:
  * Before running project.py, you should change the HOST and PORT in enums.py to the server's HOST and PORT.
  * After running project.py
    * Input your nickname, it cannot be the same as others.
    * Input the room name and password separated by spaces, the password defaults to an empty string and the password is optional.
    * now you can chat with others in the room.