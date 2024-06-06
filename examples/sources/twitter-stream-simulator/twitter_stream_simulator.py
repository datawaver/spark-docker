import socket
import random
import time

tweets = [
    '"I\'d far rather be happy than right any day." #HHGTTG',
    '"The Answer to the Great Question... Of Life, the Universe and Everything... Is... Forty-two." #DeepThought',
    '"So long, and thanks for all the fish." #DolphinFarewell',
    'RT @VogonPoetry: "Oh freddled gruntbuggly, Thy micturations are to me..." #VogonPoetry',
    '"Time is an illusion. Lunchtime doubly so." #FordPrefect',
    '"I think you ought to know I\'m feeling very depressed." #MarvinTheParanoidAndroid',
    '"Life? Don\'t talk to me about life." #MarvinQuotes',
    '"I love deadlines. I love the whooshing noise they make as they go by." #DouglasAdams',
    '"In the beginning the Universe was created. This has made a lot of people very angry and been widely regarded as a bad move." #HHGTTG',
    '"It must be Thursday. I never could get the hang of Thursdays." #ArthurDent',
    '"The ships hung in the sky in much the same way that bricks don\'t."',
    '"DON\'T PANIC" #HHGTTG',
    "Check out this amazing fan art of the Heart of Gold spaceship! https://example.com/heartofgold",
]

PORT = 5555

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("0.0.0.0", PORT))
server_socket.listen(5)

print(f"Server is listening on port: {PORT}")

while True:
    # Wait for a client connection
    client_socket, address = server_socket.accept()
    print(f"Connected to client: {address}")

    while True:
        # Randomly select a tweet
        tweet = random.choice(tweets)
        client_socket.send(tweet.encode())
        time.sleep(random.uniform(0.5, 4))
