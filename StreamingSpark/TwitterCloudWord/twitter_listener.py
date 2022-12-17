import socket
import tweepy

HOST = '127.0.1.1'
PORT = 9009

s = socket.socket()
s.bind((HOST, PORT))
print(f'Waiting connection at {PORT} port')

s.listen(5)
connection, address = s.accept()
print(f'Receiving request from {address}')

token = 'AAAAAAAAAAAAAAAAAAAAAOH8kQEAAAAAy%2FH5Ecn1bSAArTbO6aOd0ssdpJw%3DmDJBd7Tvd1YnYZ2tIwUsVsSDbcZNSx0HnScJVyPjgDPa7wAx5U'
keyword = 'sus'

class GetTweets(tweepy.StreamingClient):
    def on_tweet(self, tweet):
        print(tweet.text)
        print('='*50)
        connection.send(tweet.text.encode('latin1', 'ignore'))

printer = GetTweets(token)
printer.add_rules(tweepy.StreamRule(keyword))
printer.filter()

connection.close()